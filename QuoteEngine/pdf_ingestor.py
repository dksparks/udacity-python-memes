from typing import List
import subprocess

from .interface import IngestorInterface, IngestionError
from .model import QuoteModel


class PdfIngestor(IngestorInterface):
    """A class to ingest quotes from pdf files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the pdf file at the given path.

        If the file at the given path does not have a .pdf extension,
        an IngestionError will be raised.

        :param path: The path of the pdf file to parse.
        :return:
            A list of QuoteModel objects parsed from the lines of the
            pdf file.
        """
        if not cls.can_ingest(path):
            raise IngestionError
        quotes = []
        proc = subprocess.run(['pdftotext', path, '-'], stdout=subprocess.PIPE)
        text = proc.stdout.decode('utf-8')
        lines = [x.strip('\f') for x in text.split('\n')]
        for line in lines:
            if not line:
                continue
            try:
                body, author = line.split('-')
            except ValueError:
                print('Quote cannot be separated into body and author.')
                continue
            body = body.strip(cls.strip_chars['body'])
            author = author.strip(cls.strip_chars['author'])
            quotes.append(QuoteModel(body, author))
        return quotes
