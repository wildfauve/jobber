file_path = ["{project}", "di_container.py"]

template = """
from dependency_injector import containers, providers
from jobsworthy import repo
from jobsworthy.util import databricks, secrets
from jobsworthy.util import session as spark_session

from {project}.util import config as cfg
from {project}.repo import db

\"""
{doc}
\"""


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    session = providers.Callable(spark_session.build_spark_session,
                                 "{project}_session",
                                 spark_session.create_session)

    job_config = providers.Callable(cfg.build_job_config)
    
    secrets_provider = providers.Factory(
        secrets.Secrets, session, job_config, databricks.DatabricksUtilsWrapper(), cfg.SECRETS_SCOPE
    )

    database = providers.Factory(repo.Db,
                                 session,
                                 job_config,
                                 repo.DbNamingConventionDomainBased)
"""

doc = """"""
