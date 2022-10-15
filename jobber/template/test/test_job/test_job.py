file_path = ["tests", "test_job", "test_job.py"]

template = """
import pytest

from {project} import job

from tests.shared import *

\"""
{doc}
\"""


def test_job_completes_successfully(test_container, init_db):
    result = job.execute()

    assert result.is_right()    
"""

doc = """"""