from pathlib import Path
from jobber.util import monad, singleton


class FileManagerSpy:
    commands = []

    def __init__(self):
        self.__class__.commands = []

    def create_folder(self, path_components):
        path = Path(*path_components)
        self.__class__.commands.append(path)
        return path

    def write_file(self, file_object):
        self.__class__.commands.append(file_object)
        path = file_object.file_path if isinstance(file_object.file_path, Path) else Path(*file_object.file_path)
        return monad.Right((path, len(file_object.rendered_template)))


def file_manager_spy(mock_fn):
    return getattr(FileManagerSpy(), mock_fn)


def mock_file_manager_create_folder(mocker):
    mocker.patch('jobber.util.file_manager.create_folder', file_manager_spy('create_folder'))


def mock_file_manager_write_file(mocker):
    mocker.patch('jobber.util.file_manager.write_file', file_manager_spy('write_file'))
