from typing import List
from pathlib import Path

from jobber.model import value
from . import monad, error

def create_folder(path: List) -> None:
    Path(*path).mkdir(parents=True, exist_ok=True)
    pass

@monad.monadic_try(error_cls=error.FileWritingError)
def write_file(file_object: value.FileTemplate) -> monad.EitherMonad:
    return Path(*file_object.file_path).write_text(file_object.rendered_template)
