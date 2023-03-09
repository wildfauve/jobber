from typing import List
import re
from functools import partial
from . import value, config
from jobber.util import file_manager, fn, monad, cli_helpers, error


# curried
def file_object(cfg, template_module, path_args, template_args) -> value.FileTemplate:
    return value.FileTemplate(file_path=apply_path_template(cfg, template_module.file_path, path_args),
                              rendered_template=templater(cfg, template_module, template_args))


def create_python_files(file_object: value.FileTemplate) -> monad.EitherMonad:
    cli_helpers.echo(f"Creating Python file: {'.'.join(file_object.file_path)}")
    result = file_manager.write_file(file_object)
    if result.is_left():
        cli_helpers.echo(f"Failure: Creating Python file: {'.'.join(file_object.file_path)} with error: {result.error().message}")
        return result
    cli_helpers.echo(f"Creating Python file: {'.'.join(file_object.file_path)}")
    return result


def apply_path_template(cfg, path: List, arg_dict):
    return list(map(partial(format_path, cfg, arg_dict), path))


def format_path(cfg, arg_dict, fragment):
    result = try_format(cfg, arg_dict, fragment)
    if result.is_left():
        cli_helpers.echo(f"Failure: Formatting Path: Found {result.error().message} for frgment {fragment}")
        return None
    return result.value


@monad.monadic_try(error_cls=error.TemplateFormattingError)
def try_format(_cfg, arg_dict, fragment):
    return fragment.format(**arg_dict)


def templater(cfg, template, template_args):
    doc = template.doc if hasattr(template, "doc") else ""
    return re.sub('^\n', '', template.template.format(**{**template_args, **{'doc': doc}}
))
