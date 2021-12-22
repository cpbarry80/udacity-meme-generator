"""Stores body and author of a provided quote."""


class QuoteModel:
    """Stores body and author of a provided quote."""

    def __init__(self, body, author):
        """Instantiae Qoute with qoute and author."""
        self.body = body
        self.author = author

    def __str__(self):
        """Print the quote."""
        return f"{self.body} - {self.author}"
