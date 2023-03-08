from typing import Dict
from dataclasses import dataclass
import tomli
from pathlib import Path

from jobber.util import fn
from jobber.model import value


@dataclass
class ConfigBase(value.DataClassAbstract):
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


@dataclass
class NewProject(value.DataClassAbstract):
    config_base: ConfigBase
    domain: str
    service: str
    dataproduct: str


@dataclass
class NewTable(value.DataClassAbstract):
    config_base: ConfigBase
    table_type: str
    cls_name: str
    table_name: str
    managed: bool
    prop_prefix: str


def new_project_config_value(domain,
                             service,
                             dataproduct,
                             pyproject_location="pyproject.toml",
                             overwrite=False) -> NewProject:
    return NewProject(config_base=config_base(pyproject_location=pyproject_location,
                                              overwrite=overwrite),
                      domain=domain,
                      service=service,
                      dataproduct=dataproduct)


def build_new_table_config(table_type,
                           table_name,
                           cls_name,
                           managed,
                           prop_prefix,
                           pyproject_location) -> NewTable:
    return NewTable(table_type=table_type,
                    table_name=table_name,
                    cls_name=cls_name,
                    managed=managed,
                    prop_prefix=prop_prefix,
                    config_base=config_base(pyproject_location))


def project_name(cfg):
    return cfg.project_name()


def project_location(cfg):
    return cfg.config_base.project_location()


def add_project_toml_to_cfg(cfg):
    return cfg.replace('pyproject_toml',
                       tomli.loads(Path().joinpath(cfg.pyproject_location).read_text(encoding="utf-8")))


def config_base(pyproject_location, overwrite) -> ConfigBase:
    return ConfigBase(pyproject_toml=tomli.loads(Path().joinpath(pyproject_location).read_text(encoding="utf-8")),
                      pyproject_location=pyproject_location,
                      overwrite=overwrite)


def normalise(token):
    if not token:
        return token
    return normalise_pattern.sub('_', token).lower()
