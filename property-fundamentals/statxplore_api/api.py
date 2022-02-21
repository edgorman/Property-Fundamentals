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
        #self.output = 'json'

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
                    endpoint (str): The endpoint to request from the api.
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
                "str:value:UC_Households:F_UC_DATE:DATE_NAME:C_UC_DATE:202111"
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


    def get_universal_credit_date(self, endpoint, ward_codes) -> dict:
        '''
        Returns the API request for the 'Table' endpoint.

        https://stat-xplore.dwp.gov.uk/webapi/rest/v1/table

                Parameters:
                    endpoint (str): The endpoint to request from the api.
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
                "str:value:UC_Households:F_UC_DATE:DATE_NAME:C_UC_DATE:202111"
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
        return json_object["fields"][0]["items"][0]["labels"][0]
        
        
      

    def get_housing_benefit(self, endpoint, ward_codes) -> dict:
        '''
        Returns the API request for the 'Table' endpoint.

        https://stat-xplore.dwp.gov.uk/webapi/rest/v1/table

                Parameters:
                    endpoint (str): The endpoint to request from the api.
                    ward_codes (str): Restricts the google api to a type of location.
                
                Returns:
                    result (json): JSON formatted response.

        '''
        data2= {
            "database" : "str:database:hb_new",
            "measures" : ["str:count:hb_new:V_F_HB_NEW"],
            "recodes": {
              "str:field:hb_new:V_F_HB_NEW:WARD_CODE": {
                "map": [
                  [
                    "str:value:hb_new:V_F_HB_NEW:WARD_CODE:V_C_MASTERGEOG11_WARD_TO_LA:" + ward_codes
                  ],
                ],
                "total": True
              },
              "str:field:hb_new:F_HB_NEW_DATE:NEW_DATE_NAME": {
                "map": [
                  [
                    "str:value:hb_new:F_HB_NEW_DATE:NEW_DATE_NAME:C_HB_NEW_DATE:202111"
                  ]
                ],
                "total": False
              }
            },
            "dimensions": [
              [
                "str:field:hb_new:F_HB_NEW_DATE:NEW_DATE_NAME"
              ],
              [
                "str:field:hb_new:V_F_HB_NEW:WARD_CODE"
              ]
            ]
        }
        headers = {'Content-type': 'application/json', 'apikey':self.key}
        r2 = requests.post(self.url + '/' + endpoint, data=json.dumps(data2), headers=headers)
        json_object2 = json.loads(r2.content)
        return json_object2["cubes"]["str:count:hb_new:V_F_HB_NEW"]['values'][0][0]



    def get_housing_benefit_date(self, endpoint, ward_codes) -> dict:
        '''
        Returns the API request for the 'Table' endpoint.

        https://stat-xplore.dwp.gov.uk/webapi/rest/v1/table

                Parameters:
                    endpoint (str): The endpoint to request from the api.
                    ward_codes (str): Restricts the google api to a type of location.
                
                Returns:
                    result (json): JSON formatted response.

        '''
        data2= {
            "database" : "str:database:hb_new",
            "measures" : ["str:count:hb_new:V_F_HB_NEW"],
            "recodes": {
              "str:field:hb_new:V_F_HB_NEW:WARD_CODE": {
                "map": [
                  [
                    "str:value:hb_new:V_F_HB_NEW:WARD_CODE:V_C_MASTERGEOG11_WARD_TO_LA:" + ward_codes
                  ],
                ],
                "total": True
              },
              "str:field:hb_new:F_HB_NEW_DATE:NEW_DATE_NAME": {
                "map": [
                  [
                    "str:value:hb_new:F_HB_NEW_DATE:NEW_DATE_NAME:C_HB_NEW_DATE:202111"
                  ]
                ],
                "total": False
              }
            },
            "dimensions": [
              [
                "str:field:hb_new:F_HB_NEW_DATE:NEW_DATE_NAME"
              ],
              [
                "str:field:hb_new:V_F_HB_NEW:WARD_CODE"
              ]
            ]
        }
        headers = {'Content-type': 'application/json', 'apikey':self.key}
        r2 = requests.post(self.url + '/' + endpoint, data=json.dumps(data2), headers=headers)
        json_object2 = json.loads(r2.content)
        return json_object2["fields"][0]["items"][0]["labels"][0]