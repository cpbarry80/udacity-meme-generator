"""Select the appropriate helper class to parse the file."""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from .csv_ingestor import CSVIngestor
from .pdf_ingestor import PDFIngestor
from .docx_ingestor import DocxIngestor
from .txt_ingestor import TxtIngestor


class Ingestor(IngestorInterface):
    """Class for selecting the right ingestor to use."""
    try:
        ingestors = [CSVIngestor, PDFIngestor, DocxIngestor, TxtIngestor]
    except NameError as e:
        print(f"{e}....check out ingestor.py line 15")
        exit(1)

    @classmethod
    def parse(cls, path):
        """Parse a file to return a list of QuoteModel objects."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

