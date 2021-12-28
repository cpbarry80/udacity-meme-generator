"""Ingests a .pdf file."""

import os
import subprocess
from .ingestor_interface import IngestorInterface
from .txt_ingestor import TxtIngestor
from abc import abstractmethod


class PDFIngestor(IngestorInterface):
    """Class for create qoute models out of a .pdf file."""

    ingestable_file_types = ["pdf"]

    @classmethod
    def parse(cls, path):
        """Subprocess pdf to .txt, parse the .txt, produce QuoteModels list."""
        text_file = 'temp_text_from_pdf.txt'
        try:
            subprocess.call(['pdftotext', '-layout', '-nopgbrk', path, text_file])
        except OSError:
            print("Error on subprocess call - try change ./pdftotext to pdftotext")
            exit(1)
        except FileNotFoundError:
            print("Error on subprocess call - try change ./pdftotext to pdftotext")
            exit(1)
        else:
            quote_models_list = TxtIngestor.parse(text_file)
            os.remove(text_file)
        return quote_models_list
