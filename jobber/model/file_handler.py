from typing import List
import re
from functools import partial
from . import value, config
from jobber.util import file_manager, fn, monad, cli_helpers


# curried
def file_object(cfg, template_module, path_args, template_args) -> value.FileTemplate:
    return value.FileTemplate(file_path=apply_path_template(cfg, template_module.file_path, path_args),
                              rendered_template=templater(cfg, template_module, template_args))


def create_python_files(file_object: value.FileTemplate) -> monad.EitherMonad:
    cli_helpers.echo(f"Creating Python file: {'.'.join(file_object.file_path)}")
    return file_manager.write_file(file_object)


def apply_path_template(cfg, path: List, arg_dict):
    return list(map(partial(format_path, cfg, arg_dict), path))


def format_path(cfg, arg_dict, fragment):
    return fragment.format(**arg_dict)


def templater(cfg, template, template_args):
    doc = template.doc if hasattr(template, "doc") else ""
    return re.sub('^\n', '', template.template.format(**{**template_args, **{'doc': doc}}
))
