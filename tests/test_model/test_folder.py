from pathlib import Path
from jobber.model import folder
from jobber.util import monad

from tests.shared import folder_helpers


def test_creates_all_folders(jobber_new_job_config, mocker):
    folder_helpers.mock_file_manager_create_folder(mocker)

    result = folder.create_folders(jobber_new_job_config)

    expected_folder_paths = {
        ('jobber', 'repo'),
        ('jobber', 'util'),
        ('jobber', 'model'),
        ('tests', 'test_util'),
        ('tests', 'test_command'),
        ('jobber', 'command'),
        ('jobber', 'initialiser'),
        ('tests', 'shared'),
        ('tests', 'test_repo'),
        ('tests', 'test_job'),
        ('tests', 'test_model')}

    create_folder_paths = {path.parts for path in folder_helpers.FileManagerSpy.commands}

    assert create_folder_paths == expected_folder_paths


def test_build_python_templates(jobber_new_job_config, mocker):
    folder_helpers.mock_file_manager_write_file(mocker)

    result = folder.build_python_templates(jobber_new_job_config)

    assert all(map(monad.maybe_value_ok, result))

    cmds = folder_helpers.FileManagerSpy.commands

    expected_paths = {('tests', 'conftest.py'), ('tests', 'shared', 'di.py'), ('jobber', 'initialiser', '__init__.py'),
                      ('tests', 'test_util', 'test_secret.py'), ('tests', 'test_job', 'test_job.py'),
                      ('jobber', 'repo', '__init__.py'), ('tests', 'shared', 'spark_test_session.py'),
                      ('jobber', 'util', 'config.py'), ('jobber', 'repo', 'db.py'),
                      ('jobber', 'initialiser', 'observer_initialiser.py'),
                      ('tests', 'shared', 'config_for_testing.py'), ('tests', 'shared', '__init__.py'),
                      ('jobber', 'initialiser', 'container.py'), ('jobber', 'repo', 'table.py'),
                      ('jobber', 'repo', 'vocab.py'), ('jobber', 'dependencies.py'), ('jobber', 'repo', 'schema.py'),
                      ('tests', 'test_util', 'test_session.py'), ('jobber', 'di_container.py'),
                      ('tests', 'shared', 'db_setup.py')}

    assert {r.value[0].parts for r in result} == expected_paths

    assert {Path(*c.file_path).parts for c in cmds} == expected_paths
