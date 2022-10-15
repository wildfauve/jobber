file_path = ["tests", "test_job", "test_job.py"]

template = """
import pytest

from {project} import job


def test_job_completes_successfully(test_container, init_db):
    result = job.execute()

    assert result.is_right()
    
"""