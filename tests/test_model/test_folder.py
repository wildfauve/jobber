from jobber.model import folder

from tests.shared import folder_helpers

def test_creates_all_folders(jobber_config, mocker):
    folder_helpers.mock_file_manager(mocker)

    result = folder.create_folders(jobber_config)

    assert len(result) == 8

    expected_folder_paths = [
        ['my_job', 'command'],
        ['tests', 'test_command'],
        ['my_job', 'model'],
        ['tests', 'test_model'],
        ['my_job', 'repo'],
        ['tests', 'test_repo'],
        ['my_job', 'util'],
        ['tests', 'test_util']]

    assert folder_helpers.FileManagerSpy().commands == expected_folder_paths
