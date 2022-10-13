import sys
import json

from . import actions
from jobber.model import config
from jobber.util import cli_helpers, monad, error, env


def run(pyproject_location='pyproject.toml'):
    """
    Scaffolds a new job project
    """
    cli_helpers.echo(f"Scaffolding job for project")

    result = (configure(pyproject_location)
              >> install_dependencies
              >> create_folders)

    cli_helpers.echo("Success: Job Scaffolding Complete")

    if env.Env().env == "test":
        return result
    if result.is_left():
        sys.exit(1)
    sys.exit(0)

def configure(pyproject_location):
    result = actions.build_config(pyproject_location)
    if result.is_right():
        cli_helpers.echo(f"Building project at location {config.project_name(result.value)}")
        return result

    cli_helpers.echo(f"FAILURE: Project configuration failure")
    return result


def install_dependencies(cfg):
    cli_helpers.echo("Adding Standard Job Dependencies")

    actions.add_library_dependencies(cfg)

    cli_helpers.echo("Success: Create Standard Job Dependencies")
    return monad.Right(cfg)

def create_folders(cfg):
    cli_helpers.echo("Creating Folders")

    actions.create_folders(cfg)

    cli_helpers.echo("Success: Create Folders")
    return monad.Right(cfg)
