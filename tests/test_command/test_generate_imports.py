from pathlib import Path

from jobber.command import generate_imports

from tests.shared import cli, folder_helpers

def test_creates_imports_file(mocker):
    cli.mock_cli(mocker)
    folder_helpers.mock_file_manager_write_file(mocker)

    result =generate_imports.run(imports_location="tests/fixtures/template_imports.py")

    assert result.is_right()

    file_commands = folder_helpers.FileManagerSpy.commands

    assert len(file_commands) == 1

    assert file_commands[0].file_path == Path("tests/fixtures/template_imports.py")
    assert "templates = [" in file_commands[0].rendered_template

