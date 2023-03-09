file_path = ["{project}", "repo", "table.py"]

template = """
from functools import partial
from jobsworthy import structure as S
from jobsworthy.util import fn
from pyspark.sql import types as T

from .vocab import vocab

def table_factory() -> S.Table:
    return (
        S.Table(vocab=vocab, vocab_directives=[S.VocabDirective.RAISE_WHEN_TERM_NOT_FOUND])
        )
"""

doc = """"""

