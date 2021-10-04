import os
import json
from json.decoder import JSONDecodeError
import urllib
import time
#import certifi
#import ssl

class API:
    '''
    The class for managing Google API endpoints. 
    
    The following Google APIs are used:

    https://developers.google.com/maps/documentation/places/web-service/overview.

    https://developers.google.com/maps/documentation/geocoding/overview.
    '''

    def __init__(self, key=None, key_path=None):
        self.url = 'https://maps.googleapis.com/maps/api'
        self.output = 'json'
        self.valid_types = ['accounting', 'airport', 'amusement_park', 'aquarium', 'art_gallery', 'atm', 'bakery', 'bank', 
        'bar', 'beauty_salon', 'bicycle_store', 'book_store', 'bowling_alley', 'bus_station', 'cafe', 'campground', 'car_dealer', 
        'car_rental', 'car_repair', 'car_wash', 'casino', 'cemetery', 'church', 'city_hall', 'clothing_store', 'convenience_store', 
        'courthouse', 'dentist', 'department_store', 'doctor', 'drugstore', 'electrician', 'electronics_store', 'embassy', 
        'fire_station', 'florist', 'funeral_home', 'furniture_store', 'gas_station', 'gym', 'hair_care', 'hardware_store', 
        'hindu_temple', 'home_goods_store', 'hospital', 'insurance_agency', 'jewelry_store', 'laundry', 'lawyer', 'library', 
        'light_rail_station', 'liquor_store', 'local_government_office', 'locksmith', 'lodging', 'meal_delivery', 'meal_takeaway', 
        'mosque', 'movie_rental', 'movie_theater', 'moving_company', 'museum', 'night_club', 'painter', 'park', 'parking', 
        'pet_store', 'pharmacy', 'physiotherapist', 'plumber', 'police', 'post_office', 'primary_school', 'real_estate_agency', 
        'restaurant', 'roofing_contractor', 'rv_park', 'school', 'secondary_school', 'shoe_store', 'shopping_mall', 'spa', 
        'stadium', 'storage', 'store', 'subway_station', 'supermarket', 'synagogue', 'taxi_stand', 'tourist_attraction', 
        'train_station', 'transit_station', 'travel_agency', 'university', 'veterinary_care', 'zoo']

        if key != None:
            self.key = key
        elif key_path != None:
            with open(key_path, 'r') as key_file:
                self.key = key_file.readline()
        else:
            raise Exception("Error: Need to specify a key or path to file containing key.")
        
        self.cache_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'interim', 'google_requests')
        self.cache_file = os.path.join(self.cache_path, 'data.json')
        if not os.path.exists(self.cache_file):
            open(self.cache_file, "x")
        with open(self.cache_file) as json_file:
            try: 
                self.cache_dict = json.load(json_file)
            except JSONDecodeError:
                self.cache_dict = {}


    def get_place_types(self):
        '''
        Returns the list of valid types used in the places search api.

        https://developers.google.com/maps/documentation/places/web-service/supported_types

                Parameters:
                    None
                
                Returns:
                    types (list): List of place types.
        '''
        return self.valid_types


    def check_cache(self, request):
        '''
        Checks whether the request has been made previously, and returns the cached version.

                Parameters:
                    request (str): The request being made.
                
                Returns:
                    response (dict): Dict of api response (or None).
        '''
        if request in self.cache_dict:
            return self.cache_dict[request]
        else:
            return None
    

    def store_cache(self, request, response):
        '''
        Stores the response from the API in the cache.

                Parameters:
                    request (str): The request being made.
                    response (dict): The response being stored in cache.
                
                Returns:
                    None
        '''
        self.cache_dict[request] = response
        with open(self.cache_file, 'w') as json_file:
            json.dump(self.cache_dict, json_file)


    def request(self, endpoint, parameters={}):
        '''
        Performs the request to the endpoint at self.url.

                Parameters:
                    endpoint (str): The endpoint to request from the api.
                    parameters (dict): The parameters to pass to the endpoint.
                
                Returns:
                    result (json): JSON formatted response.
        '''
        parameters["key"] = self.key
        params = urllib.parse.urlencode(parameters)
        request = f"{self.url}/{endpoint}/{self.output}?{params}"

        if self.check_cache(request):
            return self.check_cache(request)

        time.sleep(2)
        result = json.load(urllib.request.urlopen(request))#, context=ssl.create_default_context(cafile=certifi.where())))

        if result["status"] in ["OK"]:
            self.store_cache(request, result)
        elif result["status"] in ["ZERO_RESULTS", "INVALID_REQUEST"]:
            self.store_cache(request, [])
        
        return self.check_cache(request)


    def find_place_from_text(self, input_, input_type='textquery', fields='', location_bias='', location_area='') -> dict:
        '''
        Returns the API request for the 'find place from text' endpoint.

        https://developers.google.com/maps/documentation/places/web-service/search#FindPlaceRequests

                Parameters:
                    input_ (str): The location to search (required).
                    input_type (str): The type of input, can be either text or phone number.
                    fields (str): List of fields to return separated by commas.
                    location_bias (str): Prefer results in a specific area.
                    location_area (str): Additional location information.
                
                Returns:
                    result (json): JSON formatted response.
        '''
        parameters = {
            "input": input_,
            "inputtype": input_type,
        }

        if fields != "": parameters["fields"] = fields
        if location_bias != "": 
            parameters["locationbias"] = location_bias
            if location_bias != "ipbias":
                parameters["location_area"] = location_area
        
        return self.request('place/findplacefromtext', parameters)


    def nearby_search(self, lat, lon, radius, location_type=None) -> dict:
        '''
        Returns the API request for the 'nearby search' endpoint.

        https://developers.google.com/maps/documentation/places/web-service/search#PlaceSearchRequests

                Parameters:
                    lat (float): The latitude of the circle centre point.
                    lon (float): The longitude of the circle centre point.
                    radius (float): The radius of the circle to search from (in metres).
                    type_ (str): Restricts the google api to a type of location.
                
                Returns:
                    result (json): JSON formatted response.

        '''
        if location_type != None and location_type not in self.valid_types:
            raise Exception("Error: The type '" + location_type + "' is not valid for the 'nearby search' endpoint.")
        
        parameters = {
            "location": f"{lat},{lon}",
            "radius": radius
        }

        if location_type != None:
            parameters['type'] = location_type
        
        places = []
        while True:
            response = self.request('place/nearbysearch', parameters)

            if response == []:
                break
            
            for place in response['results']:
                try:
                    a = place['name']
                except:
                        a = None
                try:
                    b = place['business_status']
                except:
                        b = None
                try:
                    c = place['geometry']['location']
                except:
                        c = None
                        continue
                try:
                    d = place['rating']
                except:
                        d = None

                places.append((
                        a,
                        b,
                        c,
                        d
                    ))

            if 'next_page_token' in response:
                parameters['pagetoken'] = response['next_page_token']
            else:
                break

        return places
