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


def config_value(domain, service, dataproduct, pyproject="pyproject.toml", overwrite=False) -> Config:
    return add_project_toml(Config(domain=domain,
                                   service=service,
                                   dataproduct=dataproduct,
                                   pyproject_location=pyproject,
                                   overwrite=overwrite))


def project_name(cfg):
    return cfg.project_name()


def add_project_toml(cfg):
    return cfg.replace('pyproject_toml',
                       tomli.loads(Path().joinpath(cfg.pyproject_location).read_text(encoding="utf-8")))
