file_path = ["tests", "shared", "spark_test_session.py"]


template = """
import pyspark
import pytest
from delta import pip_utils

\"""
{doc}
\"""


def create_pyspark_delta_session(session_name):
    from jobsworthy.util import session

    session.build_spark_session(
        session_name=session_name,
        create_fn=spark_delta_session,
        config_adder_fn=spark_session_config,
    )


def spark_delta_session(session_name):
    return pip_utils.configure_spark_with_delta_pip(delta_builder(session_name)).getOrCreate()


def delta_builder(session_name):
    return (
        pyspark.sql.SparkSession.builder.appName(session_name)
        .config('spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension')
        .config(
            'spark.sql.catalog.spark_catalog',
            'org.apache.spark.sql.delta.catalog.DeltaCatalog',
        )
    )


def spark_session_config(spark):
    spark.conf.set('hive.exec.dynamic.partition', 'true')
    spark.conf.set('hive.exec.dynamic.partition.mode', 'nonstrict')

"""

doc = """"""