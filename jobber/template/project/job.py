file_path = ["{project}", "job.py"]

template = """
from jobsworth import spark_job
from jobsworth.util import monad, logger, env

@spark_job.job(initialiser_module='{project}.initialisers')
def execute(args=None) -> monad.EitherMonad:
    pass
"""


