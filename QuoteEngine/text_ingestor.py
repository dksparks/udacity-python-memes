from typing import List

from .interface import IngestorInterface, IngestionError
from .model import QuoteModel


class TextIngestor(IngestorInterface):
    """A class to ingest quotes from text files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the text file at the given path.

        If the file at the given path does not have a .txt extension,
        an IngestionError will be raised.

        :param path: The path of the text file to parse.
        :return:
            A list of QuoteModel objects parsed from the lines of the
            text file.
        """
        if not cls.can_ingest(path):
            raise IngestionError
        quotes = []
        with open(path) as file:
            for line in file:
                if not line:
                    continue
                try:
                    body, author = [x.strip('\n') for x in line.split('-')]
                except ValueError:
                    cls.split_fail()
                    continue
                body = body.strip(cls.strip_chars['body'])
                author = author.strip(cls.strip_chars['author'])
                quotes.append(QuoteModel(body, author))
        return quotes
