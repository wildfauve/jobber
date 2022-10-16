from jobber.util import monad, singleton


class CliCommandSpy(singleton.Singleton):
    commands = []


def cli_success_returner(cmd):
    return monad.Right(['file1', 'file2'])


def cli_failure_returner(_cmd):
    return monad.Left(None)


def cli_spy_wrapper(returner_fn=cli_success_returner):
    def cli_spy(cmd: list, message: str = "", return_result: bool = False, result_parser=None):
        CliCommandSpy().commands.append({'cmd': cmd,
                                         'message': message,
                                         'result_result': return_result,
                                         'result_parser': result_parser})
        return returner_fn(cmd)

    CliCommandSpy.commands = []
    return cli_spy


def mock_cli(mocker):
    mocker.patch('jobber.util.cli_helpers.run_command', cli_spy_wrapper())
