template = """
from dependency_injector import containers, providers
from jobsworth.repo import spark_db, hive_repo
from jobsworth.util import session

from {project}.util import config as cfg
from {project}.repo import db


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    session = providers.Callable(session.build_spark_session,
                                 "{project}_session",
                                 session.create_session)

    job_config = providers.Callable(cfg.build_job_config)

    database = providers.Factory(spark_db.Db,
                                 session,
                                 job_config)
"""

def to_template(cfg):
    return template.format(project=cfg.project)