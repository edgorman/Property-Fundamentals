import math
import urllib.error
import urllib.parse
import urllib.request

from propertyfundamentals.extract._response import Status
from propertyfundamentals.extract._response import Response


class API:
    '''
        The API class is inherited by all other extractors using APIs and implements basic request functionality.
    '''

    def __init__(self, url: str) -> None:
        self.url = url

    def request(self, params: dict) -> Response:
        # Encode the parameters and form the URL
        params = urllib.parse.urlencode(params)
        request = f"{self.url}?{params}"

        # Perform the request and return the appropriate Response object
        try:
            response = urllib.request.urlopen(request)
            value = response.read().decode('utf-8')
            
            return Response(value, Status.SUCCESS)
        except urllib.error.HTTPError as e:
            return Response(None, Status.FAILURE, str(e))
        except urllib.error.URLError as e:
            return Response(None, Status.FAILURE, str(e))
        except Exception as e:
            return Response(None, Status.FAILURE, str(e))
