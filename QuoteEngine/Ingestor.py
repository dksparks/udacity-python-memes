from typing import List
from .IngestorInterface import IngestorInterface, IngestionError
from .PdfIngestor import PdfIngestor
from .DocxIngestor import DocxIngestor
from .CsvIngestor import CsvIngestor
from .TextIngestor import TextIngestor
from .QuoteModel import QuoteModel

class Ingestor(IngestorInterface):
    """A class to ingest quotes from various types of files."""

    ingestors = [PdfIngestor, DocxIngestor, CsvIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file at the given path.

        This method will attempt to use the appropriate ingestor based
        on the extension of the file provided. It will raise an
        IngestionError if no appropriate ingestor is found.

        :param path: The path of the file to parse.
        :return:
            A list of QuoteModel objects parsed from the lines of the
            file.
        """
        try:
            for ingestor in cls.ingestors:
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)
            raise IngestionError
        except IngestionError:
            print(f'The file {path} could not be ingested.')
