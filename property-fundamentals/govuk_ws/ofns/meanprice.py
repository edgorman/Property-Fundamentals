import os
import re
import io
import sys
import csv
import zipfile
import requests

import xlrd

class MeanPrice:
    '''
    The class for managing the Mean Price dataset from OFNS. 
    
    The following OFNS dataset is used:

    https://www.ons.gov.uk/peoplepopulationandcommunity/housing/datasets/meanpricepaidbywardhpssadataset38
    '''
    

    def __init__(self):
        self.dataset_dest = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', 'data', 'external', 'mean_price_per_ward'))
        self.dataset_path = 'peoplepopulationandcommunity/housing/datasets/meanpricepaidbywardhpssadataset38/'
        self.zippage_url = 'https://www.ons.gov.uk/file?uri=/' + self.dataset_path
        self.webpage_url = 'https://www.ons.gov.uk/' + self.dataset_path

        self.dataset_fold = self._update_dataset()
        self.district_ward_values = {}

        # Load data.csv file
        with open(os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', 'data', 'external', 'mean_price_per_ward', self.dataset_fold, 'data.csv'))) as csv_file:
            csv_results = list(csv.reader(csv_file, delimiter=','))[1:]

            # For each row in the csv file
            for _, district, _, ward, a, d, s, t, f in csv_results:
                if district not in self.district_ward_values.keys():
                    self.district_ward_values[district] = {}

                if ward not in self.district_ward_values[district].keys():
                    self.district_ward_values[district][ward] = {}

                self.district_ward_values[district][ward]["all"] = a
                self.district_ward_values[district][ward]["detached"] = d
                self.district_ward_values[district][ward]["semi-detached"] = s
                self.district_ward_values[district][ward]["terraced"] = t
                self.district_ward_values[district][ward]["flats"] = f


    def _update_dataset(self):
        webpage = requests.get(self.webpage_url)
        #dataset = re.search('(\w*)\/(\w*)\.zip', webpage.text).group(2)
        #dataset = re.search('(\w*)\/(\w*)\.zip" class', webpage.text).group(1)[2:]
        dataset = re.search('(\w*)\/(\w*)\.zip" class', webpage.text).group(1)[:]

        # Check if parent folder exists
        if not os.path.exists(self.dataset_dest):
            os.mkdir(self.dataset_dest)

        # If this dataset hasn't been seen before
        if dataset not in os.listdir(self.dataset_dest):
            print("[INFO]", "Starting collecting the most recent mean price ward dataset")
            print("[INFO]", "This will take about half a minute to complete...")
            
            response = requests.get(self.zippage_url + "/" + dataset + "/hpssadataset38meanpricepaidbyward.zip")
            #response = requests.get(self.zippage_url + "/" + dataset + "/hpssadataset38meanpricepaidbyward1.zip")
            print("[DONE]", "Downloaded most recent zip:\t", dataset)

            zip_file = zipfile.ZipFile(io.BytesIO(response.content))
            zip_file.extractall(os.path.join(self.dataset_dest, dataset))
            print("[DONE]", "Extracted zip folder to:\t\t", os.path.join(self.dataset_dest, dataset))

            xls_file = xlrd.open_workbook(os.path.join(self.dataset_dest, dataset, "HPSSA Dataset 38 - Mean price paid by ward.xls"), on_demand=True)
            usable_sheets = ['1a', '1b', '1c', '1d', '1e']
            
            # Write data to csv in folder
            with open(os.path.join(self.dataset_dest, dataset, "data.csv"), mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(['District code', 'District', 'Ward code', 'Ward', 'all', 'detached', 'semi', 'terraced', 'flats'])
                sheet_data = [xls_file.sheet_by_name(u) for u in usable_sheets]

                # For each row in sheets
                for row_idx in range(6, sheet_data[0].nrows):
                    row = [
                        sheet_data[0].cell_value(row_idx, 0),
                        sheet_data[0].cell_value(row_idx, 1),
                        sheet_data[0].cell_value(row_idx, 2),
                        sheet_data[0].cell_value(row_idx, 3)
                    ]
                    for data in sheet_data:
                        row.append(data.cell_value(row_idx, data.ncols - 4))
                        #row.append(data.cell_value(row_idx, data.ncols - 2))
                    
                    csv_writer.writerow(row)
            print("[DONE]", "Finished creating csv at:\t", os.path.join(self.dataset_dest, dataset))

        return dataset


    def get_districts(self):
        '''
        Returns the districts that are present in data.csv.

                Parameters:
                    None
                
                Returns:
                    districts (list): List of districts in alphabetical order.
        '''
        return sorted(list(self.district_ward_values.keys()))
    

    def get_wards(self, district):
        '''
        Returns the wards that are present within a given district.

                Parameters:
                    disctrict (str): The district to get wards for.
                
                Returns:
                    wards (list): List of wards in alphabetical order.
        '''
        if district == None:
            raise Exception("Error: Need to specify a district.")
        elif district not in self.district_ward_values.keys():
            raise Exception("Error: Could not find district '" + district + "' in the csv.")
        
        return sorted(list(self.district_ward_values[district].keys()))
    

    def get_house_types(self):
        '''
        Returns the types of housing that is present within data.csv.

                Parameters:
                    None
                
                Returns:
                    types (list): List of house types.
        '''
        return ['all', 'detached', 'semi-detached', 'terraced', 'flats']


    def get_ward_data(self, district, ward, col):
        '''
        Returns the houses column for the district and ward passed.

                Parameters:
                    disctrict (str): The district to get data for.
                    ward (str): The ward to get data for.
                    col (str): The type of housing data.
                
                Returns:
                    value (float): Value of the house type.
        '''
        if district == None:
            raise Exception("Error: Need to specify a district.")
        elif district not in self.district_ward_values.keys():
            raise Exception("Error: Could not find district '" + district + "' in the csv.")
        elif ward == None:
            raise Exception("Error: Need to specify a ward.")
        elif ward not in self.district_ward_values[district].keys():
            raise Exception("Error: Could not find ward '" + ward + "' in district + '" + district + "' in the csv.")
        
        value = self.district_ward_values[district][ward][col]
        if value == ":":
            return None
        return value
