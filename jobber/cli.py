import click


from jobber.command import new_job


@click.group()
def cli():
    pass


@click.command()
def scaffold_new_job():
    """
    Scaffolds a new job project.  The project name comes from the pyproject.toml tool.poetry.name key
    """
    new_job.run()
    pass


cli.add_command(scaffold_new_job)
