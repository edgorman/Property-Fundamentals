import enum
from dataclasses import dataclass


class Status(enum.Enum):
    '''
        The Status class is an enumerable object to indicate the outcome of a Response object.
    '''

    FAILURE = 0
    WARNING = 1
    SUCCESS = 2
    DEBUG = 3


@dataclass
class Response:
    '''
        The Response class handles all responses from extractor classes into a single unified output.
    '''

    value: object
    status: Status
    error: str = ""
