file_path = ["tests", "shared", "di.py"]

template = """
import pytest

from dependency_injector import containers, providers
from jobsworthy import repo as jwrepo
from jobsworthy.util import session as spark_session
from jobsworthy.util import secrets, databricks

from {project}.initialiser import container

from tests.shared import spark_test_session, config_for_testing, db_setup

from {project} import repo

\"""
{doc}
\"""



class OverridingContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    session = providers.Callable(spark_session.build_spark_session,
                                 "test_spark_session",
                                 spark_test_session.spark_delta_session,
                                 spark_test_session.spark_session_config)


    job_config = providers.Callable(config_for_testing.build_job_config)

    secrets_provider = providers.Factory(
        secrets.Secrets,
        session,
        job_config,
        databricks.DatabricksUtilMockWrapper(
            load_secrets={{
                f"{{config_for_testing.SECRETS_SCOPE}}": {{"<a-secret-name>": "<a-secret>"}}
            }}
        ),
        config_for_testing.SECRETS_SCOPE)
        
    project_repo_table_model = providers.Callable(repo.table_factory)
    
    database = providers.Factory(repo.ProjectDb,
                                 session,
                                 job_config,
                                 repo.DbNamingConventionDomainBased)
    
    project_repo = providers.Singleton(repo.ProjectRepo,
                                       database,                     # database
                                       jwrepo.HiveTableReader,       # reader
                                       jwrepo.DeltaTableReader,      # delta_table_reader
                                       None,                         # stream_reader
                                       jwrepo.StreamFileWriter)      # stream_writer



@pytest.fixture
def test_container():
    di = container.init_container()
    over = OverridingContainer()
    over.config.from_dict(config_for_testing.config)
    di.override(over)
    return over
"""

doc = """
"""