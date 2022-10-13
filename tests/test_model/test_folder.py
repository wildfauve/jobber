from jobber.model import folder

from tests.shared import folder_helpers

def test_creates_all_folders(jobber_config, mocker):
    folder_helpers.mock_file_manager(mocker)

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

    assert folder_helpers.FileManagerSpy().commands == expected_folder_paths
