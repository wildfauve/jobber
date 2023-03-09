file_path = ["{project}", "dependencies.py"]

template = """
from dependency_injector.wiring import Provide, inject
from {project}.di_container import Container

\"""
{doc}
\"""


from dependency_injector.wiring import Provide, inject
from {project}.di_container import Container

@inject
def table_model(table=Provide[Container.project_repo_table_model]):
    return table


@inject
def db(repo=Provide[Container.database]):
    return repo


@inject
def project_repo(repo=Provide[Container.project_repo]):
    return repo



@inject
def di_config(cfg=Provide[Container.config]):
    return cfg


@inject
def job_config(cfg=Provide[Container.job_config]):
    return cfg


@inject
def spark(session=Provide[Container.session]):
    return session

    
"""

doc = """"""


