import os
import re
import io
import sys
import csv
import zipfile
import requests

import xlrd

class PostcodeMapping:
    '''
    The class for managing the Postcode to Ward dataset from Goeportal. 
    
    The following Geoportal dataset is used:

    https://geoportal.statistics.gov.uk/datasets/postcode-to-parish-to-ward-to-local-authority-district-december-2011-lookup-in-england-and-wales/about
    '''

    def __init__(self):

        '''
        pcd7: 7-character version of the postcode (e.g. 'BT1 1AA', 'BT486PL')
        pcd8: 8-character version of the postcode (e.g. 'BT1  1AA', 'BT48 6PL')
        pcds: one space between the district and sector-unit part of the postcode (e.g. 'BT1 1AA', 'BT48 6PL') - possibly the most common formatting of postcodes.
        par11cd: Parish Code
        par11nm: Parish Name
        par11nmw: Parish Name (Welsh)
        wd11cd: Ward Code
        wd11nm: Ward Name
        wd11nmw: Ward Name (Welsh)
        lad11cd: Local Authority Code
        lad11nm: Local Authority Name
        lad11nmw: Local Authority Name (Welsh)
        '''
        
        self.postcode_to_ward_map = {}

        # Load data.csv file
        with open(os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', 'data', 'external', 'Postcode_to_Parish_to_Ward_to_Local_Authority_District', 'pcd11_par11_wd11_lad11_ew_lu.csv'))) as csv_file:
            csv_results = list(csv.reader(csv_file, delimiter=','))[1:]

            # For each row in the csv file
            for pcd7,pcd8,pcds,par11cd,par11nm,par11nmw,wd11cd,wd11nm,wd11nmw,lad11cd,lad11nm,lad11nmw in csv_results:
                if pcds not in self.postcode_to_ward_map.keys():
                    self.postcode_to_ward_map[pcds] = {}

                self.postcode_to_ward_map[pcds] = wd11nm


    def get_postcodes(self):
        '''
        Returns the postcodes that are present in pcd11_par11_wd11_lad11_ew_lu.csv.

                Parameters:
                    None
                
                Returns:
                    postcodes (list): List of postcodes in alphabetical order.
        '''
        return sorted(list(self.postcode_to_ward_map.keys()))


    def get_ward_from_postcode(self, pcds):
        '''
        Returns the ward for the postcode passed.

                Parameters:
                    pcds (str): The postcode of interest
                
                Returns:
                    value (str): The ward where the postcode is located
        '''
        if pcds == None:
            raise Exception("Error: Need to specify a postcode.")
        elif pcds not in self.postcode_to_ward_map.keys():
            raise Exception("Error: Could not find postcode '" + pcds + "' in the csv.")
        
        value = self.postcode_to_ward_map[pcds]
        if value == ":":
            return None
        return value
