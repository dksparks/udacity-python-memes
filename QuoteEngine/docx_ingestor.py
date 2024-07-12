from typing import List
import docx

from .interface import IngestorInterface, IngestionError
from .model import QuoteModel


class DocxIngestor(IngestorInterface):
    """XXXXXXXXXXXXXXXXXXXX"""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """XXXXXXXXXXXXXXX"""
        if not cls.can_ingest(path):
            raise IngestionError
        quotes = []
        doc = docx.Document(path)
        for p in doc.paragraphs:
            if not p.text:
                continue
            body, author = [x.strip('"\' \n') for x in p.text.split('-')]
            quotes.append(QuoteModel(body, author))
        return quotes
