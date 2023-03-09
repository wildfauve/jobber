import click

from jobber.command import (
    new_job as new_job_command,
    new_table as new_table_command
)


@click.group()
def cli():
    pass


@click.command()
@click.option("--domain", "-d", required=True,
              help="The name of the domain within which the job is defined.")
@click.option("--service", "-s", required=True,
              help="The name of the service the job is attached to.")
@click.option("--dataproduct", "-p", required=True,
              help="The name of the data product served by the job")
@click.option('--overwrite/--no-overwrite', default=False)
def new_job(domain, service, dataproduct, overwrite):
    """
    Scaffolds a new job project.  The project name comes from the pyproject.toml tool.poetry.name key
    """
    new_job_command.run(domain, service, dataproduct, overwrite)
    pass


@click.command()
@click.option("--table", "-t", required=True, help="The name of the table to create")
@click.option("--cls", "-c", required=True, help="The name of the Table Class")
@click.option("--prefix", "-p", required=True, help="The Table Property prefix")
@click.option('--table-type', '-y', type=click.Choice(['hive']), required=True)
@click.option('--managed/--unmanaged', required=True, default=False)
def new_table(table_type, table, cls, managed, prefix):
    """
    Create a new table
    """
    new_table_command.run(table_type=table_type,
                          table_name=table,
                          cls_name=cls,
                          managed=managed,
                          prop_prefix=prefix)


cli.add_command(new_job)
cli.add_command(new_table)
