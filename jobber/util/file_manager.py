from typing import List
from pathlib import Path

def create_folder(path: List) -> None:
    Path(*path).mkdir(parents=True, exist_ok=True)
    pass
