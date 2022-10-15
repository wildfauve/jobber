from jobber.util import cli_helpers

def run_all_tests():
    return cli_helpers.run_command(["poetry", "run", "python", "-m", "pytest", "tests"])