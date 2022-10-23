from pathlib import Path
from jobber.util import monad, cli_helpers
from jobber.model import library, folder, config, project, tester

def build_config(domain, service, dataproduct, pyproject_location, overwrite) -> monad.EitherMonad[str]:
    cfg = config.config_value(domain, service, dataproduct, pyproject_location, overwrite)
    return monad.Right(cfg)


def pyproject_to_cfg(cfg):
    config.add_project_toml_to_cfg(cfg)
    project_root = config.project_location(cfg)
    if project_root and Path(project_root).exists():
        return monad.Right(cfg)
    return monad.Left(f"""Project Root: {project_root} not found.  Check pyproject.toml configuration.
    + pyproject.toml must include the root package in [tool.poetry.packages]
    """)

    return config.add_project_toml(cfg)

def add_library_dependencies(cfg):
    results = list(map(lambda dep: library.add_dependency(dep), library.deps))

    return monad.Right(results)

def add_pytest_ini_to_pyproject(cfg):
    """
    As we've updated the pyproject.toml file when installing dependencies, we re-read it into cfg
    before updating it with the pytest config.
    :param cfg:
    :return:
    """
    pyproject_to_cfg(cfg)
    result = project.add_pytest_ini(cfg)

    return monad.Right(result)

def create_folders(cfg):
    result = folder.create_folders(cfg)

    return monad.Right(cfg)

def build_python_files_from_templates(cfg):
    result = folder.build_python_templates(cfg)

    return monad.Right(cfg)

def run_all_tests(cfg):
    result = tester.run_all_tests()
    cli_helpers.echo(msg=result)
    return cfg
