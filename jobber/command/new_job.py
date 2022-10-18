import sys
import json

from . import actions
from jobber.model import config
from jobber.util import cli_helpers, monad, error, env


def run(domain: str,
        service: str,
        dataproduct: str,
        overwrite: bool = False,
        pyproject_location: str = 'pyproject.toml'):
    """
    Scaffolds a new job project
    """
    cli_helpers.echo(f"Scaffolding job for project")

    result = (configure(domain, service, dataproduct, pyproject_location, overwrite)
              >> install_dependencies
              >> update_project_with_pytest
              >> create_folders
              >> build_python_files_from_templates
              >> run_tests)

    cli_helpers.echo("Success: Job Scaffolding Complete")

    if env.Env().env == "test":
        return result
    if result.is_left():
        sys.exit(1)
    sys.exit(0)

def configure(domain, service, dataproduct, pyproject_location, overwrite):
    result = actions.build_config(domain, service, dataproduct, pyproject_location, overwrite)
    if result.is_right():
        cli_helpers.echo(f"SUCCESS: Build project at location {config.project_name(result.value)}")
        return result

    cli_helpers.echo(f"FAILURE: Project configuration failure")
    return result


def install_dependencies(cfg):
    cli_helpers.echo("Adding Standard Job Dependencies")

    actions.add_library_dependencies(cfg)

    cli_helpers.echo("Success: Create Standard Job Dependencies")
    return monad.Right(cfg)

def update_project_with_pytest(cfg):
    cli_helpers.echo("Adding pytest configure to pyproject")

    actions.add_pytest_ini_to_pyproject(cfg)

    cli_helpers.echo("Success: pyproject updated")
    return monad.Right(cfg)


def create_folders(cfg):
    cli_helpers.echo("Creating Folders")

    actions.create_folders(cfg)

    cli_helpers.echo("Success: Create Folders")
    return monad.Right(cfg)

def build_python_files_from_templates(cfg):
    cli_helpers.echo("Building Python Files")

    result = actions.build_python_files_from_templates(cfg)

    if result.is_right():
        cli_helpers.echo(f"SUCCESS: Adding python files")
        return result

    cli_helpers.echo(f"FAILURE: Some File files failed")
    return result


def run_tests(cfg):
    cli_helpers.echo("Running Tests")

    result = actions.run_all_tests(cfg)

    return monad.Right(cfg)

