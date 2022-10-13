import pytest
from jobber.model import config

@pytest.fixture
def jobber_config():
    return config.Config(project="my_job")
