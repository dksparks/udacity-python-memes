from typing import List
import csv

from .interface import IngestorInterface, IngestionError
from .model import QuoteModel


class CsvIngestor(IngestorInterface):
    """A class to ingest quotes from csv files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the csv file at the given path.

        If the file at the given path does not have a .csv extension,
        an IngestionError will be raised.

        :param path: The path of the csv file to parse.
        :return:
            A list of QuoteModel objects parsed from the lines of the
            csv file.
        """
        if not cls.can_ingest(path):
            raise IngestionError
        quotes = []
        with open(path) as file:
            reader = csv.DictReader(file)
            for line in reader:
                if 'body' not in line or 'author' not in line:
                    print('Quote cannot be separated into body and author.')
                    continue
                stripped = {x: line[x].strip(cls.strip_chars[x]) for x in line}
                quotes.append(QuoteModel(stripped['body'], stripped['author']))
        return quotes
