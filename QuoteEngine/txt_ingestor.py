from typing import List

from .interface import IngestorInterface, IngestionError
from .model import QuoteModel


class TxtIngestor(IngestorInterface):
    """XXXXXXXXXXXXXXXXXXXX"""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """XXXXXXXXXXXXXXX"""
        if not cls.can_ingest(path):
            raise IngestionError
        quotes = []
        with open(path) as file:
            for line in file:
                if not line:
                    continue
                body, author = [x.strip('\n') for x in line.split('-')]
                body = body.strip(cls.strip_chars['body'])
                author = author.strip(cls.strip_chars['author'])
                quotes.append(QuoteModel(body, author))
        return quotes
