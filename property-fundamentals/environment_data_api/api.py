import os
import requests
import json
from json.decoder import JSONDecodeError

class API:
    '''
    The class for managing Environment Data API endpoints. 
    
    The following Environment Data API is used:

    https://environment.data.gov.uk/flood-monitoring/doc/reference
    '''

    def __init__(self):
        self.url = 'https://environment.data.gov.uk/flood-monitoring/id/floodAreas'
    
    
    def get_flood_data(self, lat, lon, distance) -> dict:
        '''
        Returns the API request for the 'FloodAreas' endpoint.

        http://environment.data.gov.uk/flood-monitoring/id/floodAreas'

                Parameters:
                    lat (float): The latitude of the circle centre point.
                    lon (float): The longitude of the circle centre point.
                    diameter (float): The diameter of the circle to search from (in kilometres).
                
                Returns:
                    result (json): JSON formatted response.

        '''
       
        r = requests.get(self.url + '?lat=' + str(lat) + '&long=' + str(lon) + '&dist=' + str(distance))
        json_object = json.loads(r.content)
        flood_HTTP = []
        for a in range(0,len(json_object["items"])):
            flood_HTTP.insert(a,json_object["items"][a]["polygon"])
        
        coordinates = []
        for b in range(0,len(json_object["items"])):
            r2 = requests.get(flood_HTTP[b])
            json_object2 = json.loads(r2.content)
            json_formatted_str2 = json.dumps(json_object2, indent=2)
            coordinates.insert(b,json_object2["features"][0]["geometry"]["coordinates"])
        return coordinates
