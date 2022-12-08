from development_district import district
from development_district import wards
from development_district import coordinates

import numpy as np
import json
import matplotlib.pyplot as plt


# based on whether there is burglary data, may want toask user if data is available first.


#may want to do this in the api. Code originally fromfile schoolratings.py. Needs to be adapted.
#need to load 

    def __init__(self):
        self.dataset_file = "Data View Download _Full Data_data.csv"
        self.dataset_helper = "constituency_to_local_authority_mapping.csv"
        self.dataset_dest = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', 'data', 'external', 'school_ratings'))
        self.dataset_file_path = os.path.join(self.dataset_dest, self.dataset_file)
        self.dataset_helper_path = os.path.join(self.dataset_dest, self.dataset_helper)

        self.district_school_values = defaultdict(list)
        self.constituency_local_authority_dict = defaultdict(list)

        # Check if csv exists
        if not os.path.exists(self.dataset_file_path):
            raise Exception("Error:", self.dataset_file_path, "not found at", self.dataset_dest)
        
        # Load helper.csv file
        with open(self.dataset_helper_path) as csv_file:
            csv_results = csv.reader(csv_file, delimiter=',')
            next(csv_results, None)
            
            self.constituency_local_authority_dict = {k: v for k, v in csv_results}

        # Load data.csv file
        with open(self.dataset_file_path) as csv_file:
            csv_results = csv.reader(csv_file, delimiter=',')
            next(csv_results, None)

            # For each row in the csv file
            for row in csv_results:

                self.district_school_values[
                    self.constituency_local_authority_dict[row[10]]
                ].append(
                    (
                        row[20],
                        row[19],
                        row[16],
                        row[2]
                    )
                )

