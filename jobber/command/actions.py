from jobber.util import monad
from jobber.model import library

def add_library_dependencies(cfg):
    to_add = [library.pyspark, library.jobsworth, library.di, library.delta]

    results = list(map(lambda dep: dep(cfg), to_add))

    return monad.Right(results)


