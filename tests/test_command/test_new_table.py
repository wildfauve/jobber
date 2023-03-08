from jobber.command import new_table

from tests.shared import cli, folder_helpers


def test_creates_new_table(mocker):
    cli.mock_cli(mocker)
    folder_helpers.mock_file_manager_create_folder(mocker)
    folder_helpers.mock_file_manager_write_file(mocker)

    result = new_table.run(table_type="hive",
                           table_name="my_table",
                           cls_name="MyTable",
                           managed=True,
                           prop_prefix="myPrefix")

    assert result.is_right()

    assert result.value.file_path == ['jobber', 'repo', 'my_table.py']
