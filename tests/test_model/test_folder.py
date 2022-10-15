from jobber.model import folder
from jobber.util import monad

from tests.shared import folder_helpers


def test_creates_all_folders(jobber_config, mocker):
    folder_helpers.mock_file_manager_create_folder(mocker)

    result = folder.create_folders(jobber_config)

    expected_folder_paths = [
        ['jobber', 'initialiser'],
        ['jobber', 'command'],
        ['tests', 'test_command'],
        ['jobber', 'model'],
        ['tests', 'test_model'],
        ['jobber', 'repo'],
        ['tests', 'test_repo'],
        ['jobber', 'util'],
        ['tests', 'shared'],
        ['tests', 'test_job'],
        ['tests', 'test_util']
    ]

    assert folder_helpers.FileManagerSpy.commands == expected_folder_paths


def test_build_python_templates(jobber_config, mocker):
    folder_helpers.mock_file_manager_write_file(mocker)
    result = folder.build_python_templates(jobber_config)

    assert all(map(monad.maybe_value_ok, result))

    cmds = folder_helpers.FileManagerSpy.commands

    expected_paths = [
        ['jobber', 'di_container.py'],
        ['jobber', 'job.py'],
        ['jobber', 'initialiser', '__init__.py'],
        ['jobber', 'initialiser', 'container.py'],
        ['jobber', 'repo', 'dependencies.py'],
        ['jobber', 'repo', 'db.py'],
        ['jobber', 'util', 'config.py'],
        ['jobber', 'util', 'dependencies.py'],
        ['tests', 'shared', 'config_for_testing.py'],
        ['tests', 'shared', 'db_setup.py'],
        ['tests', 'shared', 'di.py'],
        ['tests', 'shared', 'spark_test_session.py'],
        ['tests', 'test_job', 'test_job.py'],
        ['tests', 'test_util', 'test_secret.py'],
        ['tests', 'test_util', 'test_session.py']]


    assert [f.file_path for f in cmds] == expected_paths
