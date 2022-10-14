file_path = ["{project}", "util", "dependencies.py"]

template = """
from typing import List
from dependency_injector.wiring import Provide, inject
from jobsworth.util import fn
from {project}.di_container import Container


def config_for(elements: List):
    return fn.deep_get(di_config(), elements)


@inject
def di_config(cfg=Provide[Container.config]):
    return cfg


@inject
def spark(session=Provide[Container.session]):
    return session

"""


