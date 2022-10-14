file_path = ["{project}", "util", "config.py"]

template = """
from jobsworth import config as job_config
from jobsworth.util import env

JOB_URN_BASE = 'urn:sparkjob:<job_name>'
TABLE_FORMAT = 'delta'
DATABASE_NAME = '<hive_db_name>'
DOMAIN_NAME = '<domain_name>'
DATA_PRODUCT_NAME = '<data_product_name>'
SERVICE_NAME = '<owning_service>'
COSMOS_ACCOUNT_KEY = '<account key defined under keyvault scope>'
COSMOS_ENDPOINT = '<cosmos_db_endpoint>'
COSMOS_DB_NAME = '<cosmos_db_name>'
COSMOS_CONTAINER_NAME '<cosmos_container_name>'



config = {{
    'env': env.Env().env,
}}


def build_job_config():
    return (job_config.JobConfig(domain_name=DOMAIN_NAME,
                                 service_name=SERVICE_NAME,
                                 data_product_name=DATA_PRODUCT_NAME)
            .configure_hive_db(db_name=DATABASE_NAME)
            .configure_cosmos_db(account_key_name=COSMOS_ACCOUNT_KEY,
                                endpoint=COSMOS_ENDPOINT,
                                db_name=COSMOS_DB_NAME,
                                container_name=COSMOS_CONTAINER_NAME)))

"""


