file_path = ["tests", "test_util", "test_session.py"]

template = """
from pyspark.sql import session
from {project}.util import dependencies

\"""
{doc}
\"""


def test_session_in_container(test_container):
    assert isinstance(test_container.session(), session.SparkSession)
    assert isinstance(dependencies.spark(), session.SparkSession)
"""

doc = """"""