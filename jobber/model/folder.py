from typing import List
import re
from functools import reduce, partial
from pymonad.tools import curry
from pathlib import Path
from importlib import import_module

from . import folder_spec, scaffold_template_imports, file_handler, config
from jobber.util import file_manager, fn, monad, cli_helpers
from . import value

scaffold_template_path = Path(".") / "jobber" / "template" / "scaffold"
test_folder_location = 'tests'
template_pattern = "**/template__*.py"


def build_template_locations(location):
    file = generate_imports_file(list(map(template_to_import_path, scaffold_template_path.glob(template_pattern))))
    return file_manager.write_file(file_object=value.FileTemplate(file_path=Path(location), rendered_template=file))


def generate_imports_file(files):
    file_strs = ",\n    ".join([f"'{file}'" for file in files])
    imports_module = f"""
templates = [
    {file_strs}
]      
    """
    return imports_module


def template_to_import_path(path):
    return ".".join(path.parts).replace('.py', '')


def create_folders(cfg):
    return list(map(create_folder, folder_locations(cfg)))


def folder_locations(cfg):
    return reduce(partial(folder_locations_for_layer, cfg), folder_spec.folders.items(), [])


def build_python_templates(cfg):
    return list(map(file_handler.create_python_files, template_locations(cfg)))


def template_locations(cfg):
    return reduce(partial(build_template_locations, cfg), scaffold_template_imports.templates, [])


def folder_locations(cfg):
    return reduce(partial(folder_locations_for_layer, cfg), folder_spec.folders.items(), [])


def folder_locations_for_layer(cfg, list_of_folders, layer):
    return list_of_folders + fn.remove_none([main_folder(cfg, layer)] + [test_folder(cfg, layer)])


def main_folder(cfg, layer):
    layer_name, layer_def = layer
    if not layer_def.get('location', None):
        return None
    return [cfg.config_base.project_location()] + layer_def.get('location')


def test_folder(cfg, layer):
    layer_name, layer_def = layer
    if not layer_def.get('test_location', None):
        return None
    return [test_folder_location] + layer_def.get('test_location', [])


def create_folder(path: List[str]):
    return file_manager.create_folder(path)


def build_template_locations(cfg, list_of_templates, layer):
    template_module = import_module(layer)
    if not template_module.template or not template_module.file_path:
        breakpoint()

    template_for_layer = file_handler.file_object(cfg,
                                                  template_module,
                                                  path_args(cfg),
                                                  template_args(cfg, template_module.doc))
    return list_of_templates + [template_for_layer]


def path_args(cfg):
    return {'project': config.project_location(cfg)}


def template_args(cfg, doc):
    return {'domain': cfg.domain,
            'service': cfg.service,
            'dataproduct': cfg.dataproduct,
            'project': config.project_location(cfg),
            'doc': doc}
    
    