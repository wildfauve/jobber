import click


from jobber.command import generate_imports


@click.group()
def cli():
    pass


@click.command()
@click.option("--location", "-l", required=True,
              help="The location for the generated file")
def generate_template_imports(location):
    """
    Generates the template imports python file
    """
    generate_imports.run(location)
    pass


cli.add_command(generate_template_imports)
