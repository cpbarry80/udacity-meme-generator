"""Ingests a .txt file."""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TxtIngestor(IngestorInterface):
    """Class for create qoute models out of a .txt file."""

    ingestable_file_types = ["txt"]

    @classmethod
    def parse(cls, path):
        """Parse a .txt file and returns a list of QuoteModel objects."""
        quote_models_list = []
        f = open(path, "r", encoding="utf-8-sig")
        for line in f.readlines():
            try:
                body, author = line.rstrip('\n').split(" - ")
            except ValueError:
                continue
            else:
                quote_models_list.append(QuoteModel(f"'{body}'", author))
        f.close()
        return quote_models_list
