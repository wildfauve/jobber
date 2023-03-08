from typing import List
from pathlib import Path

from jobber.model import value
from . import monad, error

def create_folder(path_components: List[str]) -> None:
    path = Path(*path_components)
    path.mkdir(parents=True, exist_ok=True)
    return path

@monad.monadic_try(error_cls=error.FileWritingError)
def write_file(file_object: value.FileTemplate) -> monad.EitherMonad:
    path = file_object.file_path if isinstance(file_object.file_path, Path) else Path(*file_object.file_path)
    result = path.write_text(file_object.rendered_template)
    return (path, result)
