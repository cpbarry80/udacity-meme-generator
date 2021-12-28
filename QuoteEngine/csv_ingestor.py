"""Ingests a .csv file."""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
import pandas as pd


class CSVIngestor(IngestorInterface):
    """Class for create qoute models out of a .csv file."""

    ingestable_file_types = ["csv"]

    @classmethod
    def parse(cls, path):
        """Parse a .csv file and returns a list of QuoteModel objects."""
        quote_models_list = []
        df = pd.read_csv(path, header=0)
        try:
            qoute_tuple = zip(df["body"], df["author"])
        except KeyError:
            print("cant find whats the body and whats the author...quitting")
            exit(1)
        else:
            for body, author in qoute_tuple:
                quote_models_list.append(QuoteModel(f"'{body}'", author))
        return quote_models_list
