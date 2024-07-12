class QuoteModel:
    """A quotation, with body and author."""

    def __init__(self, body: str, author: str):
        """Create a new QuoteModel object.

        :param body: The body of the quote.
        :param author: The author of the quote.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return `str(self)`."""
        return f'"{self.body}" - {self.author}'

    def __repr__(self):
        """Return `repr(self)`."""
        return f'QuoteModel(body={self.body!r}, author={self.author!r})'
