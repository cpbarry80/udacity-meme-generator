"""Ingest a .docx file."""

from typing import List
import docx
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """Class for create qoute models out of a .docx file."""

    ingestable_file_types = ["docx"]

    @classmethod
    def parse(cls, path):
        """Parse a .docx file and returns a list of QuoteModel objects."""
        quote_models_list = []
        doc = docx.Document(path)

        for line in doc.paragraphs:
            if line.text:
                body, author = line.text.split(" - ")
                quote_models_list.append(QuoteModel(body, author))
        return quote_models_list
