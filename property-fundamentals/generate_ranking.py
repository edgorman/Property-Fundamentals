from development_district import district
from development_district import wards
from development_district import coordinates

import numpy as np
import json
import matplotlib.pyplot as plt

burglary_data = input("Is there a full set of burglary data available (Y/N)?")


if burglary_data =='Y':
    # need to load the CSV files. Suggest call api file here for this.
    # after reading the csv files, need to assign them to temp variables
    # for weighting,
    # property price ranking * 0.5
    # burglary ranking * 0.1
    # school ranking * 0.1
    # flooding ranking * 0.1
    # universal credit ranking * 0.1
    # housing benefit ranking * 0.1
    
    
elif burglary_data =='N':
    # need to load the CSV files. Suggest call api file here for this.
    # after reading the csv files, need to assign them to temp variables
    # for weighting,
    # property price ranking * 0.5
    # school ranking * 0.125
    # flooding ranking * 0.125
    # universal credit ranking * 0.125
    # housing benefit ranking * 0.125

else
    print("input error")



#may want to do this in the api. Code originally from file schoolratings.py. Needs to be adapted.


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

