import click


from jobber.command import new_job


@click.group()
def cli():
    pass


@click.command()
@click.argument('project')
def new_job(project):
    """
    Scaffolds a new job project.  Provide the project name.
    """
    new_job.run(project)
    pass


cli.add_command(new_job)
