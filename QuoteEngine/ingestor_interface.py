"""Base class the all ingestors should inherit from."""

from typing import List
from abc import ABC, abstractmethod
from .quote_model import QuoteModel


class IngestorInterface:
    """Base class the all ingestors should inherit from."""

    ingestable_file_types = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Is file type able to be parsed."""
        file_type = path.split(".")[-1]
        is_ingestable = file_type in cls.ingestable_file_types
        return is_ingestable

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a string."""
        pass
