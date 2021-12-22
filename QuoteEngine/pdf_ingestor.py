"""Ingest a .pdf file."""

from typing import List
import subprocess
import os
import random
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    """Ingest a .pdf file."""

    ingestable_file_types = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file to return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []

        os.makedirs("./tmp", exist_ok=True)
        tmp = f"./tmp/{random.randint(0, 10000000)}.txt"

        try:
            call = subprocess.call(["pdftotext", path, tmp])
        except FileNotFoundError:
            print(path, "not found!")

        with open(tmp, "r") as f:
            for line in f.readlines():
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    body, author = line.split(" - ")
                    quotes.append(QuoteModel(body, author))

        if os.path.exists(tmp):
            os.remove(tmp)
        return quotes
