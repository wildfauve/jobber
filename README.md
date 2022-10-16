# Jobber

Jobber is a Spark/Databricks scaffolding utility.  It builds a basic Spark python job structure which is ready to deploy on a Databricks cluster.  Once scaffolded the job has the following:

+ A folder structure for a basic job containing various layers.
+ A DI container, a test version which overrides the main container, and dependency modules for accessing the container. 
+ Access to a Spark session (from the container).
+ Job configuration.
+ An initialisers layer for pre-job initialisation (the container initialiser is also here).
+ The ability to constructa Spark session for testing.
+ A secrets utility based on the Databricks dbutils secrets APIs.
+ A few tests which ensure the job has been scaffolded correctly.

## Setting Up a Job with Jobber

Firstly create a Python project using poetry.

```shell
poetry new my_job_project
```

Then add jobber as a dev dependency.

```shell
poetry add git+https://github.com/wildfauve/jobber.git#main --group dev
```

Then add the jobber CLI to your `pyproject.toml`

```toml
[tool.poetry.scripts]
jobber = "jobber.cli:cli"
```


Finally, run the `new-job` command.  Provide the following options:
+ `--domain`: The domain the job exists in.
+ `--service`: The service (bounded context) the job is part of.  The job can be a unique, standalone, service.
+ `--dataproduct`: The data product the job is part of.

These options will help define conventions for database names and dbfs file locations, as well as secret scopes.

```shell
 poetry run jobber new-job --domain my_domain --service my_service --dataproduct my_dp
```

Expect the following output.

```shell
[Jobber][2022-10-16 12:07:40.401] Scaffolding job for project
[Jobber][2022-10-16 12:07:40.402] SUCCESS: Build project at location my_project
[Jobber][2022-10-16 12:07:40.402] Adding Standard Job Dependencies
[Jobber][2022-10-16 12:07:43.083] SUCCESS: Adding git+https://github.com/wildfauve/jobsworth#main
[Jobber][2022-10-16 12:07:43.828] SUCCESS: Adding dependency-injector
[Jobber][2022-10-16 12:07:44.558] SUCCESS: Adding pyspark
[Jobber][2022-10-16 12:07:45.324] SUCCESS: Adding delta-spark
[Jobber][2022-10-16 12:07:46.053] SUCCESS: Adding pytest to dev
[Jobber][2022-10-16 12:07:46.779] SUCCESS: Adding pytest-env to dev
[Jobber][2022-10-16 12:07:47.502] SUCCESS: Adding pytest-mock to dev
[Jobber][2022-10-16 12:07:48.264] SUCCESS: Adding pdbpp to dev
[Jobber][2022-10-16 12:07:48.265] Success: Create Standard Job Dependencies
[Jobber][2022-10-16 12:07:48.265] Adding pytest configure to pyproject
[Jobber][2022-10-16 12:07:48.265] Success: pyproject updated
[Jobber][2022-10-16 12:07:48.265] Creating Folders
[Jobber][2022-10-16 12:07:48.265] Success: Create Folders
[Jobber][2022-10-16 12:07:48.266] Building Python Files
[Jobber][2022-10-16 12:07:48.267] Creating Python file: my_project.di_container.py
[Jobber][2022-10-16 12:07:48.267] Creating Python file: my_project.job.py
[Jobber][2022-10-16 12:07:48.267] Creating Python file: my_project.initialiser.__init__.py
[Jobber][2022-10-16 12:07:48.268] Creating Python file: my_project.initialiser.container.py
[Jobber][2022-10-16 12:07:48.268] Creating Python file: my_project.repo.dependencies.py
[Jobber][2022-10-16 12:07:48.268] Creating Python file: my_project.repo.db.py
[Jobber][2022-10-16 12:07:48.269] Creating Python file: my_project.util.config.py
[Jobber][2022-10-16 12:07:48.269] Creating Python file: my_project.util.dependencies.py
[Jobber][2022-10-16 12:07:48.269] Creating Python file: tests.conftest.py
[Jobber][2022-10-16 12:07:48.270] Creating Python file: tests.shared.__init__.py
[Jobber][2022-10-16 12:07:48.270] Creating Python file: tests.shared.config_for_testing.py
[Jobber][2022-10-16 12:07:48.271] Creating Python file: tests.shared.db_setup.py
[Jobber][2022-10-16 12:07:48.272] Creating Python file: tests.shared.di.py
[Jobber][2022-10-16 12:07:48.272] Creating Python file: tests.shared.spark_test_session.py
[Jobber][2022-10-16 12:07:48.272] Creating Python file: tests.test_job.test_job.py
[Jobber][2022-10-16 12:07:48.273] Creating Python file: tests.test_util.test_secret.py
[Jobber][2022-10-16 12:07:48.273] Creating Python file: tests.test_util.test_session.py
[Jobber][2022-10-16 12:07:48.273] SUCCESS: Adding python files
[Jobber][2022-10-16 12:07:48.273] Running Tests
[Jobber][2022-10-16 12:07:54.301] SUCCESS: 

tests/test_job/test_job.py::test_job_completes_successfully PASSED       [ 33%]
tests/test_util/test_secret.py::test_returns_secret PASSED               [ 66%]
tests/test_util/test_session.py::test_session_in_container PASSED        [100%]

============================== 3 passed in 5.08s ===============================
```

The resulting folder structure is as follows:

```shell
.
├── README.md
├── dir.txt
├── poetry.lock
├── pyproject.toml
├── my_project
│   ├── __init__.py
│   ├── command
│   ├── di_container.py
│   ├── initialiser
│   │   ├── __init__.py
│   │   └── container.py
│   ├── job.py
│   ├── model
│   ├── repo
│   │   ├── db.py
│   │   └── dependencies.py
│   └── util
│       ├── config.py
│       └── dependencies.py
└── tests
    ├── conftest.py
    ├── shared
    │   ├── __init__.py
    │   ├── config_for_testing.py
    │   ├── db_setup.py
    │   ├── di.py
    │   └── spark_test_session.py
    ├── test_command
    ├── test_job
    │   └── test_job.py
    ├── test_model
    ├── test_repo
    └── test_util
        ├── test_secret.py
        └── test_session.py
```