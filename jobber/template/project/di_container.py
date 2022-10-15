file_path = ["{project}", "di_container.py"]

template = """
from dependency_injector import containers, providers
from jobsworth.repo import cosmos_repo, hive_repo, spark_db
from jobsworth.util import databricks, secrets
from jobsworth.util import session as spark_session

from {project}.util import config as cfg
from {project}.repo import db


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    session = providers.Callable(session.build_spark_session,
                                 "{project}_session",
                                 session.create_session)

    job_config = providers.Callable(cfg.build_job_config)
    
    secrets_provider = providers.Factory(
        secrets.Secrets, session, job_config, databricks.DatabricksUtilsWrapper(), cfg.SECRETS_SCOPE
    )

    database = providers.Factory(spark_db.Db,
                                 session,
                                 job_config)
"""


