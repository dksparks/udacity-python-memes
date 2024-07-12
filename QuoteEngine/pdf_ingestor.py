from typing import List
import subprocess

from .interface import IngestorInterface, IngestionError
from .model import QuoteModel


class PdfIngestor(IngestorInterface):
    """XXXXXXXXXXXXXXXXXXXX"""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """XXXXXXXXXXXXXXX"""
        if not cls.can_ingest(path):
            raise IngestionError
        quotes = []
        proc = subprocess.run(['pdftotext', path, '-'], stdout=subprocess.PIPE)
        text = proc.stdout.decode('utf-8')
        lines = [x.strip('\f') for x in text.split('\n')]
        for line in lines:
            if not line:
                continue
            body, author = line.split('-')
            body = body.strip(cls.strip_chars['body'])
            author = author.strip(cls.strip_chars['author'])
            quotes.append(QuoteModel(body, author))
        return quotes
