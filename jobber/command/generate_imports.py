import sys

from . import actions

from jobber.util import cli_helpers, env, monad


def run(imports_location: str):
    """
    Utility Function that generates dynamic template imports
    """
    cli_helpers.echo(f"Generating imports")

    result = (monad.Right((imports_location,))
              >> build_imports_file)

    if result.is_right():
        cli_helpers.echo("Success: Building Template Imports Complete")
    else:
        cli_helpers.echo("Failure: Building Template Imports Complete")

    if env.Env().env == "test":
        return result
    if result.is_left():
        sys.exit(1)
    sys.exit(0)


def build_imports_file(imports_tuple):
    cli_helpers.echo("Building Python Files")

    location, *_ = imports_tuple

    result = actions.build_template_locations(location)

    if result.is_right():
        cli_helpers.echo(f"SUCCESS: Building Template")
        return monad.Right((location, result.value))

    cli_helpers.echo(f"FAILURE: Building Templates")

    return result
