from pathlib import Path
from jobber.util import monad
from jobber.model import library, folder, config

def build_config(pyproject_location) -> monad.EitherMonad[str]:
    cfg = config.config_value(pyproject_location)
    project_root = config.project_name(cfg)
    if project_root and Path(project_root).exists():
        return monad.Right(cfg)
    return monad.Left(f"Project Root: {project_root} not found.  Check pyproject.toml configuration")


def add_library_dependencies(cfg):
    results = list(map(lambda dep: library.add_dependency(dep), library.deps))

    return monad.Right(results)


def create_folders(cfg):
    result = folder.create_folders(cfg)

    return monad.Right(cfg)

def build_python_files_from_templates(cfg):
    result = folder.build_python_templates(cfg)

    return monad.Right(cfg)