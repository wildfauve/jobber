import click


from jobber.command import new_job


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
def new_job(domain, service, dataproduct):
    """
    Scaffolds a new job project.  The project name comes from the pyproject.toml tool.poetry.name key
    """
    new_job.run(domain, service, dataproduct)
    pass


cli.add_command(new_job)
