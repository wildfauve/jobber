from jobber.template.project import di_container
from jobber.model import config

def test_templated_di_container():
    di_code = di_container.to_template(job_config())
    breakpoint()
    pass


#
# helpers
#
def job_config():
    return config.Config(project="test_job")
