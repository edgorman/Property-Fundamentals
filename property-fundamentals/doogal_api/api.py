import os
import csv
import json
import urllib, urllib.parse, urllib.request
from collections import defaultdict
from xml.etree.ElementTree import fromstring
import certifi
import ssl

class API:
    '''
    The class for managing Doogal API endpoints. 
    
    https://www.doogal.co.uk/
    '''

    def __init__(self):
        self.url = 'http://www.doogal.co.uk'
        self.district_ward_dict = {}
        self.dataset_dest = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'data', 'external', 'admin_areas', 'data.csv'))

        # Load admin_areas folder
        with open(self.dataset_dest) as csv_file:
            csv_results = list(csv.reader(csv_file, delimiter=','))[1:]

            # Create dictionaries for district data
            self.district_code_dict = {}
            self.district_ward_dict = defaultdict(dict)

            # For each row in the csv file
            for row in csv_results:
                self.district_code_dict[row[3]] = row[2]
                self.district_ward_dict[row[3]][row[5]] = row[4]
    

    def get_districts(self):
        '''
        Returns the districts that are present in admin_areas.csv.

                Parameters:
                    None
                
                Returns:
                    districts (list): List of districts in alphabetical order.
        '''
        return sorted(list(self.district_ward_dict.keys()))


    def get_wards_from_district(self, district):
        '''
        Returns the wards that are present within a given district.

                Parameters:
                    district (str): The district to search.
                
                Returns:
                    wards (list): List of wards in alphabetical order.
        '''
        if district not in self.district_ward_dict.keys():
            raise Exception("Error: Could not find district '" + district + "' in the csv.")
        
        return sorted(list(self.district_ward_dict[district].keys()))
            

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
        result = urllib.request.urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))
        
        return result


    def get_postcode_info(self, postcode):
        '''
        Get the postcode information for a given postcode.

        https://www.doogal.co.uk/GetPostcode.ashx

                Parameters:
                    postcode (str): Postcode to search (required).
                
                Returns:
                    info (dict): Info about postcode.
        '''
        if postcode == None:
            raise Exception("Error: No postcode was passed to the API.")
        
        parameters = {
            "postcode": postcode
        }

        return self.request('GetPostcode.ashx', parameters).read().decode('utf-8').split('\t')


    def get_ward_polygon(self, district, ward):
        '''
        Returns the API request for retrieving ward polygons.

        https://www.doogal.co.uk/GetAreaKml.ashx

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

        parameters = {
            "postcodes": self.district_ward_dict[district][ward]
        }

        kml_file = self.request('GetAreaKml.ashx', parameters).read().decode('utf-8')
        kml_object = fromstring(kml_file)
        polygon_object = kml_object.find('{http://www.opengis.net/kml/2.2}Document').find('{http://www.opengis.net/kml/2.2}Placemark').find('{http://www.opengis.net/kml/2.2}Polygon')
        coordinates_string = polygon_object[0][0][0].text.replace(',0', '')

        coordinates = []
        for c_string in coordinates_string.split(' '):
            if c_string == '':
                continue
            coordinates.append(
                list(map(float, c_string.split(',')))
            )
        return coordinates

