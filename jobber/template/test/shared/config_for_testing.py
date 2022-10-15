file_path = ["tests", "shared", "config_for_testing.py"]


template = """
from jobsworth import config as cfg
from jobsworth.util import env

\"""
{doc}
\"""


JOB_URN_BASE = 'urn:sparkjob:<job_name>'
TABLE_FORMAT = 'delta'
DATABASE_NAME = '<hive_db_name>'
DOMAIN_NAME = '{domain}'
DATA_PRODUCT_NAME = '{dataproduct}'
SERVICE_NAME = '{service}'
COSMOS_ACCOUNT_KEY = '<account key defined under keyvault scope>'
COSMOS_ENDPOINT = '<cosmos_db_endpoint>'
COSMOS_DB_NAME = '<cosmos_db_name>'
COSMOS_CONTAINER_NAME = '<cosmos_container_name>'
SECRETS_SCOPE = '<secret_scope>'  # delete if you want the default: <domain>.<service>.<env>

DB_FILE_SYSTEM_PATH_ROOT = "spark-warehouse"
CHECKPOINT_ROOT = "tests/db"


config = {{"env": env.Env().env}}


def build_job_config():
    return (
        cfg.JobConfig(
            data_product_name=DATA_PRODUCT_NAME,
            domain_name=DOMAIN_NAME,
            service_name=SERVICE_NAME,
        )
        .configure_hive_db(
            db_name=DATABASE_NAME,
            db_file_system_path_root=DB_FILE_SYSTEM_PATH_ROOT,
            checkpoint_root=CHECKPOINT_ROOT,
        )
        .configure_cosmos_db(account_key_name=COSMOS_ACCOUNT_KEY,
                                endpoint=COSMOS_ENDPOINT,
                                db_name=COSMOS_DB_NAME,
                                container_name=COSMOS_CONTAINER_NAME))
"""

doc = """"""