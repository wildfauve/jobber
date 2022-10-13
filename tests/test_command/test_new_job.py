from jobber.command import new_job

from tests.shared import cli, folder_helpers

def test_creates_new_job(mocker):
    cli.mock_cli(mocker)
    folder_helpers.mock_file_manager_create_folder(mocker)
    folder_helpers.mock_file_manager_write_file(mocker)

    result = new_job.run()

    assert result.is_right()