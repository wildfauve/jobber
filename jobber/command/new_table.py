import sys
import json

from . import actions
from jobber.model import config
from jobber.util import cli_helpers, monad, error, env


def run(table_type,
        table_name,
        cls_name,
        managed,
        prop_prefix,
        pyproject_location: str = 'pyproject.toml'):
    """
    Scaffolds a new job project
    """
    cli_helpers.echo(f"Create Table {table_name}")

    result = (configure(table_type, table_name, cls_name, managed, prop_prefix, pyproject_location)
              >> build_table)

    if result.is_left():
        cli_helpers.echo("FAILURE: Create Table Complete")
    else:
        cli_helpers.echo("SUCCESS: Create Table Complete")

    if env.Env().env == "test":
        return result
    if result.is_left():
        sys.exit(1)
    sys.exit(0)


def configure(table_type,
              table_name,
              cls_name,
              managed,
              prop_prefix,
              pyproject_location):
    return actions.build_new_table_config(table_type,
                                          table_name,
                                          cls_name,
                                          managed,
                                          prop_prefix,
                                          pyproject_location)


def build_table(cfg):
    result = actions.build_table(cfg)
    if result.is_right():
        cli_helpers.echo(f"SUCCESS: Build Table {cfg.table_name}")
        return result

    return result
