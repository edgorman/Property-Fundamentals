import os
import csv
from collections import defaultdict


class SchoolRatings:
    '''
    The class for managing the School Ratings dataset from Ofsted. 
    
    The following Ofsted dataset is used:

    https://public.tableau.com/profile/ofsted#!/vizhome/DataViewGetTheData/Getthedata
    '''

    def __init__(self):
        self.dataset_file = "Data_View_Download__Full_Data_data.csv"
        self.dataset_dest = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', 'data', 'external', 'school_ratings'))
        self.dataset_path = os.path.join(self.dataset_dest, self.dataset_file)

        self.district_school_values = defaultdict(list)

        # Check if csv exists
        if not os.path.exists(self.dataset_path):
            raise Exception("Error:", self.dataset_file, "not found at", self.dataset_dest)
        
        # Load data.csv file
        with open(self.dataset_path) as csv_file:
            csv_results = list(csv.reader(csv_file, delimiter=','))[1:]

            # For each row in the csv file
            for row in csv_results:
                # Ignore redacted rows
                if row[18] == 'REDACTED':
                    continue

                self.district_school_values[row[9]].append(
                    (
                        row[18],
                        row[17],
                        row[14]
                    )
                )
        
        # Load doogal api



    def get_districts(self):
        '''
        Returns the districts that are present in data.csv.

                Parameters:
                    None
                
                Returns:
                    districts (list): List of districts in alphabetical order.
        '''
        return sorted(list(self.district_school_values.keys()))


    def get_schools_from_district(self, district):
        '''
        Returns the schools that are present within a given district.

                Parameters:
                    district (str): The district to search. 
                
                Returns:
                    schools (list): List of schools as tuples <name, postcode, score>.
        '''
        if district == None:
            raise Exception("Error: Need to specify a district.")
        elif district not in self.district_school_values.keys():
            raise Exception("Error: Could not find district '" + district + "' in the csv.")
        
        return self.district_school_values[district]
    

    def get_schools_with_coordinates_from_district(self, doogal_api, district):
        '''
        Returns the schools that are present within a given district.

                Parameters:
                    doogal_api (api): Initialised Doogal api object.
                    district (str): The district to search. 
                
                Returns:
                    schools (list): List of schools as tuples <name, postcode, score, ward, coords>.
        '''
        district_schools = self.get_schools_from_district(district)
        
        schools_with_coords = []
        for s in district_schools:
            i = doogal_api.get_postcode_info(s[1])
            c = i[6]
            k = [float(i[1]), float(i[2])]
            schools_with_coords.append((s[0], s[1], s[2], c, k))
        
        return schools_with_coords
