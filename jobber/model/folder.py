from typing import List
import re
from functools import reduce
from pymonad.tools import curry

from .folder_spec import root, initialiser, command, model, repo, util, test_root, shared, test_job, test_util
from jobber.util import file_manager, fn, monad, cli_helpers
from . import value

test_folder_location = 'tests'
layer_fns = [root, initialiser, command, model, repo, util, test_root, shared, test_job, test_util]


def create_folders(cfg):
    return list(map(create_folder, reduce(folder_locations_for_layer(cfg), layer_fns, [])))


def build_python_templates(cfg):
    return list(map(create_python_files, reduce(template_locations(cfg), layer_fns, [])))


@curry(3)
def folder_locations_for_layer(cfg, list_of_folders, layer):
    return list_of_folders + fn.remove_none([main_folder(cfg, layer)] + [test_folder(cfg, layer)])


def main_folder(cfg, layer):
    return [cfg.project_location()] + layer.location if hasattr(layer, 'location') else None


def test_folder(cfg, layer):
    return [test_folder_location] + layer.test_location if hasattr(layer, 'test_location') else None


def create_folder(path):
    return file_manager.create_folder(path)


@curry(3)
def template_locations(cfg, list_of_templates, layer):
    templates_for_layer = templates(cfg, layer)
    return list_of_templates + templates_for_layer if templates_for_layer else list_of_templates


def templates(cfg, layer):
    if not hasattr(layer, 'templates'):
        return None
    return list(map(file_object(cfg), layer.templates))


@curry(2)
def file_object(cfg, template) -> value.FileTemplate:
    return value.FileTemplate(file_path=apply_path_template(cfg, template.file_path),
                              rendered_template=templater(cfg, template))


def create_python_files(file_object: value.FileTemplate) -> monad.EitherMonad:
    cli_helpers.echo(f"Creating Python file: {'.'.join(file_object.file_path)}")
    return file_manager.write_file(file_object)


def apply_path_template(cfg, path: List):
    return list(map(format_path(cfg), path))


@curry(2)
def format_path(cfg, fragment):
    return fragment.format(project=cfg.project_location())


def templater(cfg, template):
    doc = template.doc if hasattr(template, "doc") else ""
    return re.sub('^\n', '', template.template.format(domain=cfg.domain,
                                                      service=cfg.service,
                                                      dataproduct=cfg.dataproduct,
                                                      project=cfg.project_location(),
                                                      doc=doc))
