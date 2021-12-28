"""Base class the all ingestors should inherit from."""

from typing import List
from abc import ABC, abstractmethod
from .quote_model import QuoteModel


class IngestorInterface:
    """Parent class for ingestors so they are consistent."""

    ingestable_file_types = []

    @classmethod
    def can_ingest(cls, path):
        """Is file type able to be parsed."""
        file_type = path.split(".")[-1]
        is_ingestable = file_type in cls.ingestable_file_types
        return is_ingestable

    @classmethod
    @abstractmethod
    def parse(cls, path):
        """Parse a string."""
        pass
