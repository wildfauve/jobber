from jobber.model import folder
from jobber.util import monad

from tests.shared import folder_helpers


def test_creates_all_folders(jobber_config, mocker):
    folder_helpers.mock_file_manager_create_folder(mocker)

    result = folder.create_folders(jobber_config)

    assert len(result) == 10

    expected_folder_paths = [
        ['jobber', 'initialiser'],
        ['jobber', 'command'],
        ['tests', 'test_command'],
        ['jobber', 'model'],
        ['tests', 'test_model'],
        ['jobber', 'repo'],
        ['tests', 'test_repo'],
        ['jobber', 'util'],
        ['tests', 'test_util'],
        ['tests', 'shared']]

    assert folder_helpers.FileManagerSpy.commands == expected_folder_paths


def test_build_python_templates(jobber_config, mocker):
    folder_helpers.mock_file_manager_write_file(mocker)
    result = folder.build_python_templates(jobber_config)

    assert all(map(monad.maybe_value_ok, result))

    cmds = folder_helpers.FileManagerSpy.commands

    expected_paths = [['jobber', 'initialiser', 'a_container.py'], ['jobber', 'repo', 'dependencies.py'],
                      ['jobber', 'repo', 'db.py'], ['jobber', 'util', 'config.py'],
                      ['jobber', 'util', 'dependencies.py'], ['tests', 'shared', 'di.py']]

    assert [f.file_path for f in cmds] == expected_paths
