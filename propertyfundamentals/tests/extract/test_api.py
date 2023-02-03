import pytest
import urllib.request

from propertyfundamentals.extract._api import API
from propertyfundamentals.extract._response import Status
from propertyfundamentals.extract._response import Response


def test_request():
    api = API("https://google.com")
    response = api.request({})

    assert type(response) == Response
    assert response.status == Status.SUCCESS
    assert type(response.value) == str
