import json
import urllib

class API:
    '''
    The class for manaing Google API endpoints. 
    
    The following Google APIs are used:

    https://developers.google.com/maps/documentation/places/web-service/overview.

    https://developers.google.com/maps/documentation/geocoding/overview.
    '''

    def __init__(self, key=None, key_path=None):
        self.url = 'https://maps.googleapis.com/maps/api'
        self.output = 'json'

        if key != None:
            self.key = key
        elif key_path != None:
            with open(key_path, 'r') as key_file:
                self.key = key_file.readline()
        else:
            raise Exception("Error: Need to specify a key or path to file containing key.")
    

    def request(self, endpoint, parameters={}) -> dict:
        '''
        Performs the request to the endpoint at self.url.

                Parameters:
                    endpoint (str): The endpoint to request from the api.
                    parameters (dict): The parameters to pass to the endpoint.
                
                Returns:
                    result (json): JSON formatted response.
        '''
        parameters["key"] = self.key
        params = urllib.parse.urlencode(parameters)
        request = f"{self.url}/{endpoint}/{self.output}?{params}"
        result = json.load(urllib.request.urlopen(request))

        if result["status"] in ["OK", "ZERO_RESULTS"]:
            return result
        raise Exception(result["error_message"])


    def find_place_from_text(self, input_, input_type='textquery', fields='', location_bias='', location_area='') -> dict:
        '''
        Returns the API request for the 'find place from text' endpoint.

        https://developers.google.com/maps/documentation/places/web-service/search.

                Parameters:
                    input_ (str): The location to search (required).
                    input_type (str): The type of input, can be either text or phone number.
                    fields (str): List of fields to return separated by commas.
                    location_bias (str): Prefer results in a specific area.
                    location_area (str): Additional location information.
                
                Returns:
                    result (json): JSON formatted response.

        '''
        if input_ == None:
            raise Exception("Error: Need to specify an input for 'find_place_from_text' endpoint.")

        parameters = {
            "input": input_,
            "inputtype": input_type,
        }

        if fields != "": parameters["fields"] = fields
        if location_bias != "": 
            parameters["locationbias"] = location_bias
            if location_bias != "ipbias":
                parameters["location_area"] = location_area
        
        return self.request('place/findplacefromtext', parameters)
