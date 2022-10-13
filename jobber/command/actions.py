from jobber.util import monad
from jobber.model import library, folder

def add_library_dependencies(cfg):
    results = list(map(lambda dep: library.add_dependency(dep), library.deps))

    return monad.Right(results)


def create_folders(cfg):
    result = folder.create_folders(cfg)

    return monad.Right(cfg)