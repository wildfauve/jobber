from pathlib import Path
from jobber.util import monad, cli_helpers
from jobber.model import library, folder, config, project, tester, table


def build_new_job_config(domain, service, dataproduct, pyproject_location, overwrite) -> monad.EitherMonad[str]:
    cfg = config.new_project_config_value(domain,
                                          service,
                                          dataproduct,
                                          pyproject_location,
                                          overwrite)
    return monad.Right(cfg)


def build_new_table_config(table_type,
                           table_name,
                           cls_name,
                           managed,
                           prop_prefix,
                           pyproject_location) -> monad.EitherMonad:
    cfg = config.build_new_table_config(table_type,
                                        table_name,
                                        cls_name,
                                        managed,
                                        prop_prefix,
                                        pyproject_location)
    return monad.Right(cfg)


def build_table(cfg):
    return monad.Right(table.build(cfg))



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
    result = project.add_pytest_ini(cfg)

    return monad.Right(result)


def create_folders(cfg):
    result = folder.create_folders(cfg)

    return monad.Right(cfg)


def build_python_files_from_templates(cfg):
    result = folder.build_python_templates(cfg)

    return monad.Right(cfg)


def build_template_locations(location):
    return folder.build_template_locations(location)


def run_all_tests(cfg):
    result = tester.run_all_tests()
    cli_helpers.echo(msg=result)
    return cfg
