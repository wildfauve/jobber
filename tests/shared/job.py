import pytest
from jobber.model import config

@pytest.fixture
def job_config():
    return config.Config(project="test_job")
