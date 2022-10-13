from jobber.template.project import di_container
from jobber.model import config

def test_templated_di_container(jobber_config):
    di_code = di_container.to_template(jobber_config)
    pass


#
# helpers
#
