import re
import math
import json
import urllib
import geopy
from geopy import distance

class API:
    '''
    The class for managing Police API endpoints. 
    
    The following Police API are used:

    https://data.police.uk/docs/
    '''

    def __init__(self):
        self.url = 'https://data.police.uk/api'
    

    def request(self, endpoint, parameters={}):
        '''
        Performs the request to the endpoint at self.url.

                Parameters:
                    endpoint (str): The endpoint to request from the api.
                    parameters (dict): The parameters to pass to the endpoint.
                
                Returns:
                    result (json): JSON formatted response.
        '''
        params = urllib.parse.urlencode(parameters)
        request = f"{self.url}/{endpoint}?{params}"
        result = json.load(urllib.request.urlopen(request))

        return result


    def get_street_level_crimes(self, lat, lon, radius, date=None):
        '''
        Returns the API request for the 'street level crimes' endpoint.

        https://data.police.uk/docs/method/crime-street/

                Parameters:
                    lat (float): The latitude of the circle (required).
                    lon (float): The longitude of the circle (required).
                    radius (float): The radius of the circle (required).
                    date (str): The latest data to return. Format YYYY-MM (required).
                
                Returns:
                    result (json): JSON formatted response.
        '''
        coordinate_list = []

        # Calculate the coordinates of a circle originating around lat, lon at radius
        centre = geopy.Point(lat, lon)
        chord = distance.distance(kilometers=radius / 1000)
        for bearing in range(0, 360, 36):
            a, b = chord.destination(point=centre, bearing=bearing).format_decimal().split(", ")
            coordinate_list.append((round(float(a), 3), round(float(b), 3)))

        coordinate_str = ":".join([f"{a},{b}" for a, b in coordinate_list])
        parameters = {
            "poly": coordinate_str
        }

        if date is not None:
            if re.match("[0-9]{4}-[0-9]{2}", date):
                parameters["date"] = date
            else:
                raise Exception("Error: Date for API request was in the inccorect format, expecting YYYY-MM.")

        return self.request('crimes-street/all-crime', parameters)



    def get_burglary_street_level_crimes(self, lat, lon, radius, date=None):
        '''
        Returns the API request for the 'street level crimes' endpoint.

        https://data.police.uk/docs/method/crime-street/

                Parameters:
                    lat (float): The latitude of the circle (required).
                    lon (float): The longitude of the circle (required).
                    radius (float): The radius of the circle (required).
                    date (str): The latest data to return. Format YYYY-MM (required).
                
                Returns:
                    result (json): JSON formatted response.
        '''
        coordinate_list = []

        # Calculate the coordinates of a circle originating around lat, lon at radius
        centre = geopy.Point(lat, lon)
        chord = distance.distance(kilometers=radius / 1000)
        for bearing in range(0, 360, 36):
            a, b = chord.destination(point=centre, bearing=bearing).format_decimal().split(", ")
            coordinate_list.append((round(float(a), 3), round(float(b), 3)))

        coordinate_str = ":".join([f"{a},{b}" for a, b in coordinate_list])
        parameters = {
            "poly": coordinate_str
        }

        if date is not None:
            if re.match("[0-9]{4}-[0-9]{2}", date):
                parameters["date"] = date
            else:
                raise Exception("Error: Date for API request was in the inccorect format, expecting YYYY-MM.")

        return self.request('crimes-street/burglary', parameters)