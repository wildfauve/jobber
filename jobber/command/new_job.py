import sys
import json

from . import actions
from jobber.model import config
from jobber.util import cli_helpers, monad, error, env


def run(project):
    """
    Scaffolds a new job project
    """
    result = (monad.Right(config.config_value(project))
              >> install_dependencies)

    if env.Env().env == "test":
        return result
    if result.is_left():
        sys.exit(1)
    sys.exit(0)


def install_dependencies(cfg):
    actions.add_library_dependencies(cfg)
    cli_helpers.echo("Success: Create Standard Job Dependencies")
    return monad.Right(cfg)