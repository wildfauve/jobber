file_path = ["{project}", "repo", "db.py"]

template = """
from jobsworthy import repo, performance

from . import table


\"""
{doc}
\"""

# This is a stubbed in database class.  Refer to the jobsworthy repo documentation for more information.
class ProjectDb(repo.Db):
    pass

# This is a stubbed in Hive Table class.  Refer to the jobsworthy repo documentation for more information.
class ProjectRepo(repo.HiveRepo):
    table_name = "enter-table-name-here"

"""

doc = """"""

