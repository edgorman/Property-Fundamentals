import os
import re
import io
import zipfile
import requests

class MeanPrice:
    '''
    The class for managing the Mean Price dataset from OFNS. 
    
    The following OFNS dataset is used:

    https://www.ons.gov.uk/peoplepopulationandcommunity/housing/datasets/meanpricepaidbywardhpssadataset38
    '''

    def __init__(self):
        self.dataset_dest = os.path.abspath(os.path.join(__file__, '../../../..', 'data/external/mean_price_per_ward/'))
        self.dataset_path = 'peoplepopulationandcommunity/housing/datasets/meanpricepaidbywardhpssadataset38/'
        self.zippage_url = 'https://www.ons.gov.uk/file?uri=/' + self.dataset_path
        self.webpage_url = 'https://www.ons.gov.uk/' + self.dataset_path

        # Get most recent mean price dataset
        webpage = requests.get(self.webpage_url)
        dataset = re.search('(\w*)\/(\w*)\.zip', webpage.text).group(1)

        # If this dataset hasn't been seen before
        if dataset not in os.listdir(self.dataset_dest):
            # Extract zip to new folder
            response = requests.get(self.zippage_url + "/" + dataset + "/hpssadataset38meanpricepaidbyward.zip")
            zip_file = zipfile.ZipFile(io.BytesIO(response.content))
            zip_file.extractall(os.path.join(self.dataset_dest, dataset))

            # TODO: Convert xls to csv file


if __name__ == "__main__":
    m = MeanPrice()
