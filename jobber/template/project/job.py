file_path = ["{project}", "job.py"]

template = """
from jobsworth import spark_job
from jobsworth.util import monad, logger, env
from {project} import initialiser

\"""
{doc}
\"""


@spark_job.job(initialiser_module=initialiser)
def execute(args=None) -> monad.EitherMonad:
    pass
"""

doc = """"""
