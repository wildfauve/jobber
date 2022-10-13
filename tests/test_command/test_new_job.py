from jobber.command import new_job

from tests.shared import cli

def test_creates_new_job(mocker):
    cli.mock_cli(mocker)

    result = new_job.run('job-project')

    breakpoint()