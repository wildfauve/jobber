file_path = ["{project}", "initialiser", "a_container.py"]

template = """
from jobsworth import spark_job
from jobsworth.util import env

from cbor_streamer import di_container
from cbor_streamer.util import config

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
