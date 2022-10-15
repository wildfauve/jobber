from jobber.util import cli_helpers

def run_all_tests():
    return cli_helpers.run_command(cmd=["poetry", "run", "python", "-m", "pytest", "tests"],
                                   return_result=True,
                                   result_parser=cli_helpers.as_string)
