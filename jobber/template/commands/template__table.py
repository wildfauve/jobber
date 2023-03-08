file_path = ["{project}", "repo", "{table_name}.py"]

template = """
from jobsworthy import repo, performance

\"""
{doc}
\"""

class {table_cls_name}(repo.HiveRepo):
    table_name = "{table_name}"

    table_creation_protocol = repo.{table_create_protocol}

    table_properties = [
        repo.TableProperty(repo.DataAgreementType.DATA_PRODUCT, "", "{prop_prefix}"),
        repo.TableProperty(repo.DataAgreementType.SCHEMA_VERSION, "", "{prop_prefix}"),
        repo.TableProperty(repo.DataAgreementType.PARTITION_COLUMNS, "", "{prop_prefix}"),
        repo.TableProperty(repo.DataAgreementType.PRUNE_COLUMN, "", "{prop_prefix}"),
        repo.TableProperty(repo.DataAgreementType.PORT, "", "{prop_prefix}"),
        repo.TableProperty(repo.DataAgreementType.UPDATE_FREQUENCY, "", "{prop_prefix}"),
        repo.TableProperty(repo.DataAgreementType.DESCRIPTION,
                           "", "{prop_prefix}"),
    ]

    partition_columns = ("column1",)

    pruning_column = "column1"

    # A schema can be specified for the table in 2 ways.  The first is to provide a schema class property 
    # which returns a StructType object.  This can also be achieved using the Jobsworthy Structure module via the 
    # table DSL.
    #
    # schema = table.table_factory().hive_schema()
    #
    # The second way is to implement the method schema_as_dict() which returns a dictionary version of the StructType.
    # 
    # def schema_as_dict():
    #     return {{}}

    # The following lifecycle events are supported.  Use these to perform functions like executing the table creation
    # protocol, creating the table properties, or any other function that is required.  Delete if not required.
    def after_initialise(self):
        self.perform_table_creation_protocol()
        pass
    
    def after_append(self):
        # Called after the `write_append` function has completed.
        pass

    def after_upsert(self):
        # Called after `upsert` has completed.
        pass
        
    def after_stream_write_via_delta_upsert(self):
        # Called after `stream_write_via_delta_upsert.
        pass


"""

doc = """"""

