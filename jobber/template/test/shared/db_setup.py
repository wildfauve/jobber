file_path = ["tests", "shared", "db_setup.py"]

template = """
import shutil

import pytest

from {project}.repo import dependencies as repo_deps

\"""
{doc}
\"""

@pytest.fixture
def init_db():
    repo_deps.db().create_db_if_not_exists()
    yield
    repo_deps.db().drop_db()

    # When using spark streaming, a _checkpoint location will be required during tests.
    # This will need to be deleted to after a test to clear out test data.  
    # Not required unless using streaming with checkpoint location.
    #
    # shutil.rmtree(repo_deps.<repo>.table_location(), ignore_errors=True, onerror=None,)
"""


doc = """
A test multi-line doc 
In the code
"""