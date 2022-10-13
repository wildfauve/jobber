from jobber.command import actions
from jobber.util import fn

from tests.shared import cli


def test_adds_dependencies(jobber_config, mocker):
    cli.mock_cli(mocker)

    result = actions.add_library_dependencies(jobber_config)

    assert result.is_right()

    cmds = cli.CliCommandSpy.commands

    expected_deps = ['git+https://github.com/wildfauve/jobsworth#main', 'dependency-injector', 'pyspark', 'delta-spark',
                     'pytest', 'pytest-env', 'pytest-mock', 'pdbpp']

    assert [cmd['cmd'][2] for cmd in cmds] == expected_deps

def test_adds_dev_dependencies(jobber_config, mocker):
    cli.mock_cli(mocker)

    result = actions.add_library_dependencies(jobber_config)

    assert result.is_right()

    cmds = cli.CliCommandSpy.commands

    assert len(list(filter(lambda cmd: "dev" in cmd['cmd'], cmds))) == 4

