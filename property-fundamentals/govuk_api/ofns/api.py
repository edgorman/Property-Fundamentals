import json
import urllib

class API:
    '''
    The class for managing OFNS API endpoints. 
    
    The following OFNS APIs are used:

    https://ons-inspire.esriuk.com/arcgis/rest/services/Administrative_Boundaries/WGS84_UK_Wards_December_2017_Boundaries/MapServer/0
    '''

    def __init__(self):
        self.url = 'https://ons-inspire.esriuk.com/arcgis/rest/services/Administrative_Boundaries/WGS84_UK_Wards_December_2017_Boundaries/MapServer/0'
        self.output = 'pjson'
    

    def request(self, endpoint, parameters={}) -> dict:
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


    def query(self, location) -> dict:
        '''
        Returns the API request for the query endpoint.

        https://geoportal.statistics.gov.uk/datasets/7193daa99995445aa84a0b23352e56a1_0/geoservice.

                Parameters:
                    where (str): The location to search (required).
                
                Returns:
                    result (json): JSON formatted response.

        '''
        if location == None:
            raise Exception("Error: Need to specify a location for 'query' endpoint.")

        parameters = {
            "where": "wd17nm='" + location + "'",
            "geometryType": "esriGeometryPolygon",
            "f": self.output
        }

        return self.request('query', parameters)
