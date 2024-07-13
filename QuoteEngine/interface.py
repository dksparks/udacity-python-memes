from typing import List
from string import whitespace
from abc import ABC, abstractmethod
from .model import QuoteModel


class IngestorInterface(ABC):
    """An abstract base class for quote ingestors."""

    allowed_extensions = []
    strip_chars = {'body': whitespace + '"\'', 'author': whitespace}

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether the file at the given path can be ingested.

        This method only checks the filename extension and thus assumes
        that the extension matches the format of the file itself.

        :param path: The path of the file to check.
        :return: A boolean containing the result of the check.
        """
        path_split = path.split('.')
        if len(path_split) < 2:
            raise IngestionError
        return path_split[-1] in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file at the given path.

        This method will be overridden as appropriate in each subclass.

        :param path: The path of the file to parse.
        :return:
            A list of QuoteModel objects parsed from the lines of the
            file.
        """
        pass

    @classmethod
    def split_fail(cls):
        """This method will be called if a quote cannot be split."""
        print('[Quote cannot be separated into body and author.]')


class IngestionError(Exception):
    """An exception to raise if a file cannot be ingested."""
    pass
