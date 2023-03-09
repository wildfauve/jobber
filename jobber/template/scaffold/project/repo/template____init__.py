file_path = ["{project}", "repo", "__init__.py"]

template = """
from .db import (
    projectDb,
    ProjectRepo
)

from .schema import (
    some_schema
)

from .table import (
    table_factory
)

from .vocab import (
    vocab
)

from jobsworthy.repo import (
    CosmosStreamReader,
    DbNamingConventionDomainBased,
    HiveTableReader,
    StreamHiveWriter
)
"""

doc = """"""