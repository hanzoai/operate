class ToolError(Exception):
    """Raised when a tool encounters an error."""

    def __init__(self, message):
        self.message = message


class OperatorError(Exception):
    """Base exception for all Operator errors"""


class TokenLimitExceeded(OperatorError):
    """Exception raised when the token limit is exceeded"""
