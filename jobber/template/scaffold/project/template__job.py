file_path = ["{project}", "job.py"]

template = """
from jobsworthy import spark_job
from jobsworthy.util import monad, logger, env
from {project} import initialiser

\"""
{doc}
\"""


@spark_job.job(initialiser_module=initialiser)
def execute(args=None) -> monad.EitherMonad:
    return monad.Right(None)
"""

doc = """"""
