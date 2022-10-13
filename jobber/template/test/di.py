from pathlib import Path

file_path = ["tests", "shared", "di.py"]


template = """
import pytest

from dependency_injector import containers, providers
from jobsworth.repo import spark_db, hive_repo
from jobsworth.util import session

from {project}.initialisers import a_container

from tests.shared import spark_test_session, config_for_testing, db_setup

from {project}.repo import db


class OverridingContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    session = providers.Callable(session.build_spark_session,
                                 "test_spark_session",
                                 spark_test_session.spark_delta_session,
                                 spark_test_session.spark_session_config)


    job_config = providers.Callable(config_for_testing.build_job_config)

    database = providers.Factory(spark_db.Db,
                                 session,
                                 job_config)


@pytest.fixture
def test_container():
    di = a_container.init_container()
    over = OverridingContainer()
    over.config.from_dict(config_for_testing.config)
    di.override(over)
    return over
"""

def render(cfg):
    return template.format(project=cfg.project_name())