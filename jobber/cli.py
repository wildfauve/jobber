import click


from jobber.command import new_job as new_job_command


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
@click.option("--table", "-t", required=True,
              help="The name of the table to create")
def new_table(table):
    """
    Create a new table
    """

cli.add_command(new_job)
cli.add_command(new_table)
