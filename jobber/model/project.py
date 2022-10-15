import tomli_w


def add_pytest_ini(cfg):
    if has_pytest_configured(cfg.pyproject_toml):
        return cfg
    return update_pyproject_with_pytest(cfg)


def update_pyproject_with_pytest(cfg):
    cfg.pyproject_toml['tool']['pytest'] = pytest_ini_opt()
    write_pyproject_toml(cfg.pyproject_location, cfg.pyproject_toml)
    return cfg


def write_pyproject_toml(location: str, toml: dict):
    with open(location, mode="wb") as fp:
        tomli_w.dump(toml, fp)


def has_pytest_configured(pyproject):
    return 'pytest' in pyproject['tool'].keys()


def pytest_ini_opt():
    return {'ini_options': {
        'minversion': '6.0',
        'addopts': '-ra -q',
        'python_classes': ['*Test', 'Test*', 'Describe*'],
        'python_functions': ['test_*', 'it_*'],
        'xfail_strict': True,
        'log_cli': True,
        'log_cli_level': 20,
        'env': ['ENVIRONMENT=test'],
        'testpaths': ['tests', 'integration']}}
