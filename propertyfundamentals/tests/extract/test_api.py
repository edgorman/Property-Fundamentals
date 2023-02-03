from propertyfundamentals.extract._api import API
from propertyfundamentals.extract._response import Status
from propertyfundamentals.extract._response import Response


def test_get():
    api = API("https://google.com")
    response = api.get()

    assert isinstance(response, Response)
    assert response.status == Status.SUCCESS
    assert isinstance(response.value.text, str)
