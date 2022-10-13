import sys
import json

from . import actions
from jobber.model import config
from jobber.util import cli_helpers, monad, error, env


def run(project):
    """
    Scaffolds a new job project
    """
    cli_helpers.echo(f"Scaffolding job for project: {project}")

    result = (monad.Right(config.config_value(project))
              >> install_dependencies
              >> create_folders)

    cli_helpers.echo("Success: Job Scaffolding Complete")

    if env.Env().env == "test":
        return result
    if result.is_left():
        sys.exit(1)
    sys.exit(0)


def install_dependencies(cfg):
    actions.add_library_dependencies(cfg)
    cli_helpers.echo("Success: Create Standard Job Dependencies")
    return monad.Right(cfg)

def create_folders(cfg):
    actions.create_folders(cfg)
    cli_helpers.echo("Success: Create Folders")
    return monad.Right(cfg)
