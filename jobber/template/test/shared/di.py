file_path = ["tests", "shared", "di.py"]

template = """
import pytest

from dependency_injector import containers, providers
from jobsworth.repo import spark_db, hive_repo
from jobsworth.util import session as spark_session
from jobsworth.util import secrets, databricks

from {project}.initialiser import container

from tests.shared import spark_test_session, config_for_testing, db_setup

from {project}.repo import db

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

    
    

    database = providers.Factory(spark_db.Db,
                                 session,
                                 job_config)


@pytest.fixture
def test_container():
    di = container.init_container()
    over = OverridingContainer()
    over.config.from_dict(config_for_testing.config)
    di.override(over)
    return over
"""

doc = """"""