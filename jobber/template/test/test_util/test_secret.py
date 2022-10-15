file_path = ["tests", "test_util", "test_secret.py"]

template = """

from tests.shared import *

\"""
{doc}
\"""


def test_returns_secret(test_container):
    secret = test_container.secrets_provider().get_secret('<a-secret-name>')
    assert secret.value == "<a-secret>"
    
"""

doc = """"""