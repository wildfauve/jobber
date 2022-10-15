file_path = ["tests", "conftest.py"]

template = """
import pytest

from tests.shared import *

\"""
{doc}
\"""
"""

doc = """"""
