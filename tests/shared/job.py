import pytest
from jobber.model import config

@pytest.fixture
def jobber_config():
    return config.config_value(domain="my_domain", service="my_service", dataproduct="my_data_product")
