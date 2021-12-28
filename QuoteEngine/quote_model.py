"""Stores body and author of a provided quote."""


class QuoteModel():
    """Structures the qoute into 2 clear parts - body and author."""

    def __init__(self, body, author):
        """Construct Qoute with qoute and author."""
        self.body = body
        self.author = author

    def __str__(self):
        """Print the quote."""
        return f"{self.body} - {self.author}"
