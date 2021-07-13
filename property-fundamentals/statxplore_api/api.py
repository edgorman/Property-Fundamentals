import os
import json
from json.decoder import JSONDecodeError
import urllib
import requests

class API:
    '''
    The class for managing Stat-Xplore API endpoints. 
    
    The following Stat-Xplore API is used:

    https://stat-xplore.dwp.gov.uk/webapi/online-help/Open-Data-API.html.

    '''        
    
    
    def __init__(self, key=None, key_path=None):
        self.url = 'https://stat-xplore.dwp.gov.uk/webapi/rest/v1'
        self.output = 'json'

        if key != None:
            self.key = key
        elif key_path != None:
            with open(key_path, 'r') as key_file:
                self.key = key_file.readline()
        else:
            raise Exception("Error: Need to specify a key or path to file containing key.")



    def get_universal_credit(self, endpoint, ward_codes) -> dict:
        '''
        Returns the API request for the 'Table' endpoint.

        https://stat-xplore.dwp.gov.uk/webapi/rest/v1/table

                Parameters:
                    ward_codes (str): Restricts the google api to a type of location.
                
                Returns:
                    result (json): JSON formatted response.

        '''
        data = {
        "database" : "str:database:UC_Households",
        "measures" : ["str:count:UC_Households:V_F_UC_HOUSEHOLDS"],
        "recodes": {
          "str:field:UC_Households:V_F_UC_HOUSEHOLDS:WARD_CODE": {
            "map": [
              [
                "str:value:UC_Households:V_F_UC_HOUSEHOLDS:WARD_CODE:V_C_MASTERGEOG11_WARD_TO_LA:" + ward_codes
              ],
            ],
            "total": True
          },
          "str:field:UC_Households:F_UC_DATE:DATE_NAME": {
            "map": [
              [
                "str:value:UC_Households:F_UC_DATE:DATE_NAME:C_UC_DATE:202102"
              ]
            ],
            "total": False
          }
        },
        "dimensions": [
          [
            "str:field:UC_Households:F_UC_DATE:DATE_NAME"
          ],
          [
            "str:field:UC_Households:V_F_UC_HOUSEHOLDS:WARD_CODE"
          ]
        ]
        }
        headers = {'Content-type': 'application/json', 'apikey':self.key}
        r = requests.post(self.url + '/' + endpoint, data=json.dumps(data), headers=headers)
        json_object = json.loads(r.content)
        return json_object["cubes"]["str:count:UC_Households:V_F_UC_HOUSEHOLDS"]['values'][0][0]
        
    # def request(self, endpoint, parameters={}):
        # '''
        # Performs the request to the endpoint at self.url.

                # Parameters:
                    # endpoint (str): The endpoint to request from the api.
                    # parameters (dict): The parameters to pass to the endpoint.
                
                # Returns:
                    # result (json): JSON formatted response.
        # '''
        # params = urllib.parse.urlencode(parameters)
        # request = f"{self.url}/{endpoint}?{params}"
        # result = json.load(urllib.request.urlopen(request))

        # return result
        
        
        
        

    # def get_housing_benefit(ward_codes) -> dict:
        # '''
        # Returns the API request for the 'Table' endpoint.

        # https://stat-xplore.dwp.gov.uk/webapi/rest/v1/table

                # Parameters:
                    # ward_codes (str): Restricts the google api to a type of location.
                
                # Returns:
                    # result (json): JSON formatted response.

        # '''
        # data2 = {
        # "database" : "str:database:UC_Households",
        # "measures" : ["str:count:UC_Households:V_F_UC_HOUSEHOLDS"],
        # "recodes": {
          # "str:field:UC_Households:V_F_UC_HOUSEHOLDS:WARD_CODE": {
            # "map": [
              # [
                # "str:value:UC_Households:V_F_UC_HOUSEHOLDS:WARD_CODE:V_C_MASTERGEOG11_WARD_TO_LA:" + ward_codes
              # ],
            # ],
            # "total": True
          # },
          # "str:field:UC_Households:F_UC_DATE:DATE_NAME": {
            # "map": [
              # [
                # "str:value:UC_Households:F_UC_DATE:DATE_NAME:C_UC_DATE:202102"
              # ]
            # ],
            # "total": False
          # }
        # },
        # "dimensions": [
          # [
            # "str:field:UC_Households:F_UC_DATE:DATE_NAME"
          # ],
          # [
            # "str:field:UC_Households:V_F_UC_HOUSEHOLDS:WARD_CODE"
          # ]
        # ]
        # }
        # url = 'https://stat-xplore.dwp.gov.uk/webapi/rest/v1/table'
        # headers2 = {'Content-type': 'application/json','apikey':'65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a7063334d694f694a7a644849756333526c6247786863694973496e4e3159694936496e646b5a323979625746755147647459576c734c6d4e7662534973496d6c68644349364d5459794e5451354e5449334d5377695958566b496a6f69633352794c6d396b59534a392e664e67356b71762d506763346a376a3274496a67394d535f5f384748547833315251456c6330342d58586f'}
        # r2 = requests.post(url, data=json.dumps(data2), headers=headers2)
        # json_object2 = json.loads(r2.content)
        # return json_object2["cubes"]["str:count:hb_new:V_F_HB_NEW"]['values'][0][0]

