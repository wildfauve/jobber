from jobber.util import cli_helpers

deps = [
    ("jobsworthy", 'project'),
    ("dependency-injector", "project"),
    ("pyspark", "project"),
    ("delta-spark", "project"),
    ("pytest", "dev"),
    ("pytest-env", "dev"),
    ("pytest-mock", "dev"),
    ("pdbpp", "dev")
]


def add_dependency(dep):
    dependency, group = dep
    if group == "project":
        return cli_helpers.run_command(["poetry", "add", dependency], message=f"Adding {dependency}")
    return cli_helpers.run_command(["poetry", "add", dependency, "--group", "dev"],
                                   message=f"Adding {dependency} to dev")
