class QuoteModel:
    """A quotation, with body and author."""

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __str__(self):
        """Return `str(self)`."""
        return f'"{self.body}" - {self.author}'

    def __repr__(self):
        """Return `repr(self)`."""
        return f'QuoteModel(body={self.body!r}, author={self.author!r})'
