from jobber.util import cli_helpers

def jobsworth(cfg):
    return add_dependency("git+https://github.com/wildfauve/jobsworth#main")

def di(cfg):
    return add_dependency("dependency-injector")

def pyspark(cfg):
    return add_dependency("pyspark")

def delta(cfg):
    return add_dependency("delta-spark")

def add_dependency(dep):
    return cli_helpers.run_command(["poetry", "add", dep], message=f"Adding {dep}")
