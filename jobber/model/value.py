from dataclasses import dataclass

@dataclass
class DataClassAbstract:
    def replace(self, key, value):
        setattr(self, key, value)
        return self


@dataclass
class FileTemplate(DataClassAbstract):
    file_path: str
    rendered_template: str
