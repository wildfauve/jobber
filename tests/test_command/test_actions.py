from jobber.command import actions

from tests.shared import cli

def test_adds_dependencies(job_config, mocker):
    cli.mock_cli(mocker)

    result = actions.add_library_dependencies(job_config)

    assert result.is_right()

    cmds = cli.CliCommandSpy.commands

    expected_deps = ['pyspark', 'git+https://github.com/wildfauve/jobsworth#main', 'dependency-injector', 'delta-spark']

    assert [cmd['cmd'][0] for cmd in cmds] == expected_deps
