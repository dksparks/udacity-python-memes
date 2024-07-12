from typing import List
from interface import IngestorInterface, IngestionError
from pdf_ingestor import PdfIngestor
from docx_ingestor import DocxIngestor
from csv_ingestor import CsvIngestor
from txt_ingestor import TxtIngestor
from model import QuoteModel

class Ingestor(IngestorInterface):
    """A class to ingest quotes from various types of files."""

    ingestors = [PdfIngestor, DocxIngestor, CsvIngestor, TxtIngestor]

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
