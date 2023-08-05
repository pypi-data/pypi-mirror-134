from typing import Optional

import requests

class AkinonCLIError(Exception):
    """Generic errors."""

    def __init__(self, message: str, *, response: Optional[requests.Response] = None):
        super().__init__(message, response)
        self.message = message
        self.response = response
