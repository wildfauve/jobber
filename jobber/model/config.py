from dataclasses import dataclass

@dataclass
class Config:
    project: str


def config_value(project) -> Config:
    return Config(project=project)
