import csv
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
        self.district_ward_dict = {}

        # Load admin_areas.csv file
        with open('../data/external/admin_areas.csv') as csv_file:
            csv_results = list(csv.reader(csv_file, delimiter=','))[1:]

            # For each row in the csv file
            for county_code, county, district_code, district, ward_code, ward, _, _ in csv_results:
                if district not in self.district_ward_dict.keys():
                    self.district_ward_dict[district] = {}
                self.district_ward_dict[district][ward] = ward_code


    def get_districts(self):
        '''
        Returns the districts that are present in admin_areas.csv.

                Parameters:
                    None
                
                Returns:
                    districts (list): List of districts in alphabetical order.
        '''
        return sorted(list(self.district_ward_dict.keys()))
    

    def get_ward(self, district):
        '''
        Returns the wards that are present within a given district.

                Parameters:
                    None
                
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
            raise Exception("Error: Could not find district '" + district + "' in the csv.")

        ward_id = self.district_ward_dict[district][ward]

        parameters = {
            "where": "wd17cd='" + ward_id + "'",
            "geometryType": "esriGeometryPolygon",
            "f": self.output
        }

        response = self.request('query', parameters)
        polygon = response['features'][0]['geometry']['rings'][0]
        return polygon
