file_path = ["{project}", "initialiser", "container.py"]

template = """
from jobsworthy import spark_job
from jobsworthy.util import env

from {project} import di_container
from {project}.util import config

\"""
{doc}
\"""


mods = ['{project}.util.dependencies',
        '{project}.repo.dependencies']

@spark_job.register()
def build_container():
    if "test" not in env.Env().env:
        init_container()


def init_container():
    di = di_container.Container()
    di.config.from_dict(config.config)
    di.wire(modules=mods)
    return di

"""


doc = """"""