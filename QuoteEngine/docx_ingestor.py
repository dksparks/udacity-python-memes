from typing import List
import docx

from .interface import IngestorInterface, IngestionError
from .model import QuoteModel


class DocxIngestor(IngestorInterface):
    """A class to ingest quotes from csv files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the docx file at the given path.

        If the file at the given path does not have a .docx extension,
        an IngestionError will be raised.

        :param path: The path of the docx file to parse.
        :return:
            A list of QuoteModel objects parsed from the lines of the
            docx file.
        """
        if not cls.can_ingest(path):
            raise IngestionError
        quotes = []
        doc = docx.Document(path)
        for p in doc.paragraphs:
            if not p.text:
                continue
            try:
                body, author = [x.strip('\n') for x in p.text.split('-')]
            except ValueError:
                print('Quote cannot be separated into body and author.')
                continue
            body = body.strip(cls.strip_chars['body'])
            author = author.strip(cls.strip_chars['author'])
            quotes.append(QuoteModel(body, author))
        return quotes
