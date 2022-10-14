file_path = ["{project}", "repo", "dependencies.py"]

template = """
from dependency_injector.wiring import Provide, inject
from {project}.di_container import Container

@inject
def db(repo=Provide[Container.database]):
    return repo

"""


