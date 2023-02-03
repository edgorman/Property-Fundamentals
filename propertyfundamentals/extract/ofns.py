import os
import io
import csv
import zipfile
import regex as re
import pandas as pd

from propertyfundamentals.extract._api import API
from propertyfundamentals.extract._response import Status


class OFNS(API):
    '''
        The OFNS class handles all web requests (API and scraping) to the Office for National Statistics website.
    '''

    def __init__(self):
        super().__init__("https://www.ons.gov.uk")

    def _get_house_price(self, dataset_path: str, endpoint: str, zip_filename: str,):
        # Check if the parent directory exists and create if not
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)

        # Extract the list of datasets available at the endpoint
        web_response = self.get(endpoint, {})
        assert web_response.status == Status.SUCCESS, web_response.error

        # Select the most recent dataset (will be the first one found)
        dataset_list = re.findall(r'(\w*)\/\w*\.zip" class', web_response.value.text)
        assert len(dataset_list) > 0, f"No zip files could be found at '{os.path.join(self.url, endpoint)}'"
        
        # Check if the csv filename exists for the most recent dataset
        latest_dataset = dataset_list[0]
        csv_path = os.path.join(dataset_path, latest_dataset)
        csv_filename = csv_path + ".csv"
        if not os.path.exists(csv_filename):

            # Download the dataset as a zip file 
            zip_response = self.get(f"/file/?uri={os.path.join(endpoint, latest_dataset, zip_filename)}")
            assert zip_response.status == Status.SUCCESS, zip_response.error

            # Extract the dataset and save the contents
            zip_file = zipfile.ZipFile(io.BytesIO(zip_response.value.content))
            zip_file.extractall(csv_path)
            
            # Read the excel file into a pandas dataframe
            xls_filename = os.path.join(csv_path, os.listdir(csv_path)[0])
            xls_dict = pd.read_excel(xls_filename, sheet_name=['1a', '1b', '1c', '1d', '1e'], header=5)

            # Create a new dataframe with each housing type value per ward code
            # The sheet names correspond directly to the housing types: 'all','detached','semi','terraced','flats'
            xls_dict = pd.DataFrame(
                data = {
                    'ward': xls_dict['1a'].dropna(axis='columns', how='all').iloc[:, 0],
                    'all': xls_dict['1a'].dropna(axis='columns', how='all').iloc[:, -1],
                    'detached': xls_dict['1b'].dropna(axis='columns', how='all').iloc[:, -1],
                    'semi': xls_dict['1c'].dropna(axis='columns', how='all').iloc[:, -1],
                    'terraced': xls_dict['1d'].dropna(axis='columns', how='all').iloc[:, -1],
                    'flats': xls_dict['1e'].dropna(axis='columns', how='all').iloc[:, -1]
                }
            ).dropna(axis='rows', how='all')

            # Save the new dataframe as a csv file
            xls_dict.to_csv(csv_filename, index=False)

        # Assert that the output file now exists
        assert os.path.exists(csv_filename), f"Output file could not be found at '{out_filename}'"
    
    def get_mean_house_price(self):
        self._get_house_price(
            "/tmp/propertyfundamentals/data/extract/ofns/median_house_price",
            "/peoplepopulationandcommunity/housing/datasets/medianpricepaidbywardhpssadataset37/",
            "hpssadataset37medianpricepaidbyward1.zip"
        )

    def get_median_house_price(self):
        self._get_house_price(
            "/tmp/propertyfundamentals/data/extract/ofns/median_house_price",
            "/peoplepopulationandcommunity/housing/datasets/medianpricepaidbywardhpssadataset37/",
            "hpssadataset37medianpricepaidbyward1.zip"
        )
