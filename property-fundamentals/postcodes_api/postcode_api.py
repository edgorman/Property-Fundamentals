import re
import math
import requests
import json
import urllib
import geopy
from geopy import distance

class API:
    '''
    The class for managing Ppstcode.io API endpoints. 
    
    The following Postcode.io API is used:

    https://postcodes.io/
    '''

    def __init__(self):
        self.url = 'https://api.postcodes.io/postcodes?lon='
    

    def get_postcode(self, lon, lat) -> dict:
        '''
        Returns the API request for the 'postcodes?' endpoint.

        https://api.postcodes.io/postcodes?lon=

                Parameters:
                    lon (str): The longitude
                    lat (str): The latitude
                
                Returns:
                    result (json): JSON formatted response.

        '''

        headers = {'Content-type': 'application/json'}
        r = requests.get(self.url + lon + '&lat=' + lat, headers=headers)
        json_object = json.loads(r.content)
        for j in range (0,len(json_object)):
            #if not isinstance (json_object["result"][j]["postcode"], type(None)):
            if json_object["result"] is not None:
                return json_object["result"][j]["admin_ward"]
                j=len(json_object) 
