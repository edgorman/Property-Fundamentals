import requests

from propertyfundamentals.extract._response import Status
from propertyfundamentals.extract._response import Response


class API:
    '''
        The API class is inherited by all other extractors using APIs and implements basic request functionality.
    '''

    def __init__(self, url: str) -> None:
        self.url = url

    def get(self, endpoint: str = "", params: dict = {}) -> Response:
        try:
            response = requests.get(f"{self.url}{endpoint}", data=params)
            assert response.status_code == 200, f"{response.reason} - {response.url}"
            return Response(response, Status.SUCCESS)
        except Exception as e:
            return Response(None, Status.FAILURE, str(e))
