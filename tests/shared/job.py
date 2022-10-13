import pytest
from jobber.model import config

@pytest.fixture
def jobber_config():
    return config.config_value()
