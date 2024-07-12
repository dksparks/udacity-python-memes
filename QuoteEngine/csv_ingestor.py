from typing import List
import csv

from .interface import IngestorInterface, IngestionError
from .model import QuoteModel


class CsvIngestor(IngestorInterface):
    """XXXXXXXXXXXXXXXXXXXX"""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """XXXXXXXXXXXXXXX"""
        if not cls.can_ingest(path):
            raise IngestionError
        quotes = []
        with open(path) as file:
            reader = csv.DictReader(file)
            for line in reader:
                quote = QuoteModel(line['body'].strip('"\' '), line['author'])
                quotes.append(quote)
        return quotes
