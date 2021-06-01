import os
import csv
import json
from collections import defaultdict
import urllib, urllib.parse, urllib.request

class API:
    '''
    The class for managing OFNS API endpoints. 
    
    The following OFNS APIs are used:

    https://ons-inspire.esriuk.com/arcgis/rest/services/Administrative_Boundaries/WGS84_UK_Wards_December_2017_Boundaries/MapServer/0
    '''

    def __init__(self):
        self.url = 'https://ons-inspire.esriuk.com/arcgis/rest/services/Administrative_Boundaries/WGS84_UK_Wards_December_2017_Boundaries/MapServer/0'
        self.output = 'pjson'
        self.county_district_dict = defaultdict(set)
        self.district_ward_dict = defaultdict(dict)

        # Load data.csv file
        with open(__file__ + '\\..\\..\\..\\..\\data\\external\\admin_areas\\data.csv') as csv_file:
            csv_results = list(csv.reader(csv_file, delimiter=','))[1:]

            # For each row in the csv file
            for county_code, county, district_code, district, ward_code, ward, _, _ in csv_results:
                self.county_district_dict[county].add(district)
                self.district_ward_dict[district][ward] = ward_code


    def get_counties(self):
        '''
        Returns the counties that are present in data.csv.

                Parameters:
                    None
                
                Returns:
                    counties (list): List of counties in alphabetical order.
        '''
        return sorted(list(self.county_district_dict.keys()))


    def get_districts(self):
        '''
        Returns the districts that are present in data.csv.

                Parameters:
                    None
                
                Returns:
                    districts (list): List of districts in alphabetical order.
        '''
        return sorted(list(self.district_ward_dict.keys()))
    

    def get_districts_from_county(self, county):
        '''
        Returns the districts that belong to the county passed.

                Parameters:
                    county (str): The county to search.
                
                Returns:
                    districts (list): List of districts in alphabetical order.
        '''
        if county == None:
            raise Exception("Error: Need to specify a county.")
        elif county not in self.county_district_dict.keys():
            raise Exception("Error: Could not find county '" + county + "' in the csv.")

        return sorted(list(self.county_district_dict[county]))
    

    def get_wards_from_district(self, district):
        '''
        Returns the wards that are present within a given district.

                Parameters:
                    district (str): The district to search.
                
                Returns:
                    wards (list): List of wards in alphabetical order.
        '''
        if district == None:
            raise Exception("Error: Need to specify a district.")
        elif district not in self.district_ward_dict.keys():
            raise Exception("Error: Could not find district '" + district + "' in the csv.")
        
        return sorted(list(self.district_ward_dict[district].keys()))
    

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


    def get_ward_polygon(self, district, ward) -> dict:
        '''
        Returns the API request for retrieving ward polygons.

        https://geoportal.statistics.gov.uk/datasets/7193daa99995445aa84a0b23352e56a1_0/geoservice.

                Parameters:
                    district (str): The district to find (required).
                    ward (str): The ward to find (required).
                
                Returns:
                    result (list): List of point for the ward polygon.

        '''
        if district == None:
            raise Exception("Error: Need to specify a district.")
        elif district not in self.district_ward_dict.keys():
            raise Exception("Error: Could not find district '" + district + "' in the csv.")

        if ward == None:
            raise Exception("Error: Need to specify a ward.")
        elif ward not in self.district_ward_dict[district].keys():
            raise Exception("Error: Could not find ward '" + ward + "' from district '" + district + "'.")

        ward_id = self.district_ward_dict[district][ward]

        parameters = {
            "where": "wd17cd='" + ward_id + "'",
            "geometryType": "esriGeometryPolygon",
            "f": self.output
        }

        response = self.request('query', parameters)

        if len(response['features']) == 0:
            # raise Exception("Error: The OFNS server has no coordinate data for ward '" + ward + "' from district '" + district + "'.")
            print("The OFNS server has no coordinate data for ward '" + ward + "' from district '" + district + "'.")
            return None

        polygon = response['features'][0]['geometry']['rings'][0]
        return polygon
