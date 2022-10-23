from typing import Dict
from dataclasses import dataclass
import tomli
from pathlib import Path

from jobber.util import fn
from jobber.model import value


@dataclass
class Config(value.DataClassAbstract):
    domain: str
    service: str
    dataproduct: str
    pyproject_location: str
    overwrite: bool
    pyproject_toml: Dict = None

    def project_name(self):
        return fn.deep_get(self.pyproject_toml, ['tool', 'poetry', 'name'])

    def project_location(self):
        packages = fn.deep_get(self.pyproject_toml, ['tool', 'poetry', 'packages'])
        if not packages or len(packages) != 1:
            return None
        return packages[0].get('include', None)


def config_value(domain, service, dataproduct, pyproject="pyproject.toml", overwrite=False) -> Config:
    return Config(domain=domain,
                  service=service,
                  dataproduct=dataproduct,
                  pyproject_location=pyproject,
                  overwrite=overwrite)


def project_name(cfg):
    return cfg.project_name()


def project_location(cfg):
    return cfg.project_location()


def add_project_toml_to_cfg(cfg):
    return cfg.replace('pyproject_toml',
                       tomli.loads(Path().joinpath(cfg.pyproject_location).read_text(encoding="utf-8")))


def normalise(token):
    if not token:
        return token
    return normalise_pattern.sub('_', token).lower()
