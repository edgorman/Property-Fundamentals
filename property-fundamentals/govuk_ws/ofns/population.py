import os
import re
import io
import sys
import csv
import zipfile
import requests
from glob import glob
import openpyxl
import pandas as pd


class Population:
    '''
    The class for managing the Population dataset from OFNS. 
    
    The following OFNS dataset is used:

    https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/wardlevelmidyearpopulationestimatesexperimental
    '''

    def __init__(self):
        self.dataset_dest = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', 'data', 'external', 'population'))
        self.dataset_path = 'peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/wardlevelmidyearpopulationestimatesexperimental'
        self.zippage_url = 'https://www.ons.gov.uk/file?uri=/' + self.dataset_path
        self.webpage_url = 'https://www.ons.gov.uk/' + self.dataset_path

        self.dataset_fold = self._update_dataset()
        self.ward_code_values = {}

        # Load data.csv file
        with open(os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', 'data', 'external', 'population', self.dataset_fold, 'data.csv'))) as csv_file:
            csv_results = list(csv.reader(csv_file, delimiter=','))[1:]

            # For each row in the csv file
            for ward_code, ward_name, population in csv_results:
                if ward_code not in self.ward_code_values.keys():
                    self.ward_code_values[ward_code] = {}

                self.ward_code_values[ward_code] = population

    def _update_dataset(self):
        webpage = requests.get(self.webpage_url)
        dataset1 = re.search('(\w*)\/(\w*)\.zip" class', webpage.text).group(1)[2:]
        dataset2 = re.search('(\w*)\/(\w*)\.zip" class', webpage.text).group(2)

        # Check if parent folder exists
        if not os.path.exists(self.dataset_dest):
            os.mkdir(self.dataset_dest)

        # If this dataset hasn't been seen before
        if dataset1 not in os.listdir(self.dataset_dest):
            print("[INFO]", "Starting collecting the most recent population dataset")
            print("[INFO]", "This will take about half a minute to complete...")
            
            response = requests.get(self.zippage_url + "/" + dataset1 + "/" + dataset2 + '.zip')
            print("[DONE]", "Downloaded most recent zip:\t", dataset1)

            zip_file = zipfile.ZipFile(io.BytesIO(response.content))
            zip_file.extractall(os.path.join(self.dataset_dest, dataset1))
            print("[DONE]", "Extracted zip folder to:\t\t", os.path.join(self.dataset_dest, dataset1))
            
            path = glob(os.path.join(self.dataset_dest, dataset1) + "/*.xlsx")[0]
            data = pd.read_excel(path, engine='openpyxl', sheet_name=3, header=4)
            data = data[['Ward Code 1', 'Ward Name 1', 'All Ages']]
            data.to_csv(os.path.join(self.dataset_dest, dataset1, "data.csv"), index=False, index_label=False)
            print("[DONE]", "Finished creating csv at:\t", os.path.join(self.dataset_dest, dataset1))

        return dataset1


    def get_population(self, ward_code):
        '''
        Returns the population that are present within a given ward.

                Parameters:
                    ward_code (str): The ward code to get the population for.
                
                Returns:
                    population (list): Population for the ward.
        '''
        if ward_code == None:
            raise Exception("Error: Need to specify a ward code.")
        elif ward_code not in self.ward_code_values.keys():
            raise Exception("Error: Could not find ward code '" + ward_code + "' in the csv.")
        
        return self.ward_code_values[ward_code]
    
