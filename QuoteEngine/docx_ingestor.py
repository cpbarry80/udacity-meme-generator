"""Ingest a .docx file."""

from typing import List
import docx
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """Ingest a .docx file."""

    ingestable_file_types = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file to return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                body, author = para.text.split(" - ")
                quotes.append(QuoteModel(body, author))
        return quotes
