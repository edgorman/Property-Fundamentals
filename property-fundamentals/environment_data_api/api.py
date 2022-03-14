import requests
import json

class API:
    '''
    The class for managing Environment Data API endpoints. 
    
    The following Environment Data API is used:

    https://environment.data.gov.uk/flood-monitoring/doc/reference
    '''

    def __init__(self):
        self.url = 'http://environment.data.gov.uk/flood-monitoring/id/floodAreas'
    
    
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
       
        r = requests.get(self.url + '?lat=' + lat + '&lon=' + lon + '&dist=' + distance)
        json_object = json.loads(r.content)
        
        for a in range(0,len(json_object["items"])):
            r2 = requests.get(json_object["items"][a]["polygon"])
            json_object2 = json.loads(r2.content)
        return json_object2["features"][0]["geometry"]["coordinates"]
