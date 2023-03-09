file_path = ['{project}', 'initialiser', 'observer_initialiser.py']

template = """
from jobsworthy import spark_job, observer

\"""
{doc}
\"""


@spark_job.register()
def init_observer_namespaces():
    define_namespaces()


def define_namespaces():
    observer.define_namespace(observer.Hive, 'https://nzsuperfund.co.nz/resource-for-hive-table-lineage')
    observer.define_namespace(observer.SparkJob, "https://nzsuperfund.co.nz/resource-for-this-spark-job/")

"""

doc = """
Configure the observer module with the root URLs (namespaces) for lineage.  Each of the inputs and outputs of the Job
can be added to a observer table via the jobsworthy observer module.  For each type of input/output, the root type
requires a resource (in URL form) to provide the root of its identity. 
"""