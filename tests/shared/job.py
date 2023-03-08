import pytest
from jobber.model import config


@pytest.fixture
def jobber_new_job_config():
    return config.new_project_config_value(domain="my_domain", service="my_service", dataproduct="my_data_product")
