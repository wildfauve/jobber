import pytest
from jobber.model import config


@pytest.fixture
def jobber_config():
    return config.add_project_toml_to_cfg(
        config.config_value(domain="my_domain", service="my_service", dataproduct="my_data_product"))
