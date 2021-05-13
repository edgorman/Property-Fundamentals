import os
import csv
import json
import urllib
from collections import defaultdict

class API:
    '''
    The class for managing Doogal API endpoints. 
    
    https://www.doogal.co.uk/
    '''

    def __init__(self):
        self.url = 'https://www.doogal.co.uk'
        self.district_ward_dict = {}

        # Load admin_areas.csv file
        with open('../data/external/admin_areas/data.csv') as csv_file:
            csv_results = list(csv.reader(csv_file, delimiter=','))[1:]

            # Create dictionaries for district data
            self.district_code_dict = defaultdict(str)
            self.district_ward_dict = defaultdict(list)

            # For each row in the csv file
            for row in csv_results:
                self.district_code_dict[row[3]] = row[2]
                self.district_ward_dict[row[3]].append((row[5], row[4]))
    

    def get_districts(self):
        '''
        Returns the districts that are present in admin_areas.csv.

                Parameters:
                    None
                
                Returns:
                    districts (list): List of districts in alphabetical order.
        '''
        return sorted(list(self.district_ward_dict.keys()))
            

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
        result = urllib.request.urlopen(request)
        
        return result


    def get_postcodes(self, postcodes) -> dict:
        '''
        Get the KML for individual postcodes for individual postcodes.

        https://www.doogal.co.uk/GetAreaKml.ashx

                Parameters:
                    postcodes (list): List of postcodes to get (required).
                
                Returns:
                    result (kml): KML formatted response.
        '''
        if postcodes == None:
            raise Exception("Error: No postcodes were passed to the API.")
        
        parameters = {
            "topLevel": "false",
            "postcodes": postcodes
        }

        return self.request('GetAreaKml.ashx', parameters).read()


    def get_kml(self, district) -> dict:
        '''
        Contacts several endpoints and save the kml file for the wards within.

        https://www.doogal.co.uk/AdministrativeAreasCSV.ashx

                Parameters:
                    district (str): The district to search (required).
                
                Returns:
                    result (kml): KML formatted response.
        '''
        if district == None:
            raise Exception("Error: Need to specify a district to identify postcodes for.")
        
        if district not in self.district_code_dict.keys():
            raise Exception("Error: Could not find district '" + district + "' within district_code_dict keys.")

        if district not in self.district_ward_dict.keys():
            raise Exception("Error: Could not find district '" + district + "' within district_ward_dict keys.")

        # Check if district folder exists in interim data
        if district not in os.listdir('../data/interim/'):
            # Create district directory
            os.mkdir('../data/interim/' + district)

            district_code = self.district_code_dict[district]
            ward_list = self.district_ward_dict[district]
            ward_kmls = []

            # For each ward in the district
            for ward_name, ward_code in ward_list:
                # Create ward directory
                os.mkdir('../data/interim/' + district + '/' + ward_name)

                postcodes = []

                # Make API request for postcode list
                parameters = {
                    "district": district_code,
                    "ward": ward_code
                }

                postcodes_results = self.request('AdministrativeAreasCSV.ashx', parameters).read().decode().split('\n')

                # Parse postcodes returned
                for postcode_line in postcodes_results[1:-1]:
                    postcodes.append(postcode_line.split(',')[0])
                
                # Split postcodes into upper levels
                postcodes_dict = defaultdict(list)
                for postcode in postcodes:
                    postcodes_dict[postcode[:postcode.index(' ') + 2]].append(postcode)
                
                # For each upper postcode level
                for key, values in postcodes_dict.items():

                    # Get postcode areas
                    postcodes_kml = self.get_postcodes(', '.join(values))

                    # Save kml files to interim folder
                    with open('../data/interim/' + district + '/' + ward_name + '/' + key + '.kml', "w", encoding="utf-8") as kml_file:
                        kml_file.write(postcodes_kml.decode("utf-8"))

        else:
            print("didn't have to load")
