file_path = ["tests", "test_util", "test_secret.py"]

template = """

\"""
{doc}
\"""


def test_returns_secret(test_container):
    secret = test_container.secrets_provider().get_secret('<name-of-key-secret>')
    assert secret.value == "a-secret"
    
"""

doc = """"""