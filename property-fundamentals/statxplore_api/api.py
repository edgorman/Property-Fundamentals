import os
import json
from json.decoder import JSONDecodeError
import urllib

class API:
    '''
    The class for managing Stat-Xplore API endpoints. 
    
    The following Stat-Xplore API is used:

    https://stat-xplore.dwp.gov.uk/webapi/online-help/Open-Data-API.html.

    '''        
        
    def __init__(self, key=None, key_path=None):
        self.url = 'https://stat-xplore.dwp.gov.uk/webapi/rest/v1'
        self.output = 'json'
        self.valid_types = ['Attendance Allowance', 'Benefit Cap', 'Carer's Allowance', 'Disability Living Allowance', 
                            'Employment and Support Allowance', 'Housing Benefit', 'NINo Registrations', 
                            'Pension Credit', 'Personal Independence Payment', 'Sanction Decisions', 
                            'State Pension', 'Universal Credit', 'Work Programme']

        if key != None:
            self.key = key
        elif key_path != None:
            with open(key_path, 'r') as key_file:
                self.key = key_file.readline()
        else:
            raise Exception("Error: Need to specify a key or path to file containing key.")
        
        self.cache_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'interim', 'google_requests')
        self.cache_file = os.path.join(self.cache_path, 'data.json')
        if not os.path.exists(self.cache_file):
            open(self.cache_file, "x")
        with open(self.cache_file) as json_file:
            try: 
                self.cache_dict = json.load(json_file)
            except JSONDecodeError:
                self.cache_dict = {}
    
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


    def check_cache(self, request):
        '''
        Checks whether the request has been made previously, and returns the cached version.

                Parameters:
                    request (str): The request being made.
                
                Returns:
                    response (dict): Dict of api response (or None).
        '''
        if request in self.cache_dict:
            return self.cache_dict[request]
        else:
            return None
    

    def store_cache(self, request, response):
        '''
        Stores the response from the API in the cache.

                Parameters:
                    request (str): The request being made.
                    response (dict): The response being stored in cache.
                
                Returns:
                    None
        '''
        self.cache_dict[request] = response
        with open(self.cache_file, 'w') as json_file:
            json.dump(self.cache_dict, json_file)


