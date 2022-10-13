from jobber.util import monad, singleton

class FileManagerSpy(singleton.Singleton):
    commands = []


def file_manager_spy_wrapper():
    def file_spy(path):
        FileManagerSpy().commands.append(path)
        return None
    FileManagerSpy.commands = []
    return file_spy


def mock_file_manager(mocker):
    mocker.patch('jobber.util.file_manager.create_folder', file_manager_spy_wrapper())
