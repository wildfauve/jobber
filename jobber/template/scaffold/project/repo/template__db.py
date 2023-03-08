file_path = ["{project}", "repo", "db.py"]

template = """
from jobsworthy import repo, performance

from . import table


\"""
{doc}
\"""

class ProjectDb(repo.Db):
    db_properties = [
        repo.DbProperty(repo.DataAgreementType.DATA_PRODUCT, "", ""),
        repo.DbProperty(repo.DataAgreementType.DESCRIPTION,
                        "", ""),
    ]


class ProjectRepo(repo.HiveRepo):
    table_name = "enter-table-name-here"

    table_creation_protocol = repo.CreateManagedDeltaTableSQL

    table_properties = [
        repo.TableProperty(repo.DataAgreementType.DATA_PRODUCT, "", ""),
        repo.TableProperty(repo.DataAgreementType.SCHEMA_VERSION, "", ""),
        repo.TableProperty(repo.DataAgreementType.PARTITION_COLUMNS, "", ""),
        repo.TableProperty(repo.DataAgreementType.PRUNE_COLUMN, "", ""),
        repo.TableProperty(repo.DataAgreementType.PORT, "", ""),
        repo.TableProperty(repo.DataAgreementType.UPDATE_FREQUENCY, "", ""),
        repo.TableProperty(repo.DataAgreementType.DESCRIPTION,
                           "", ""),
    ]

    partition_columns = ("column1",)

    pruning_column = "column1"

    schema = table.table_factory().hive_schema()

    def after_initialise(self):
        self.perform_table_creation_protocol()
        pass

"""

doc = """"""

