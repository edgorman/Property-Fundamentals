from govuk_api.ofns.api import API as OFNS_API
from doogal_api.api import API as DOOGAL_API
from govuk_ws.ofns.population import Population
from math import sin, cos, sqrt, atan2, radians
ofns_api = OFNS_API()
doogal_api = DOOGAL_API()
population_api = Population()
import geopy.distance
import matplotlib.pyplot as plt
import numpy as np

coordinates = []
wards = []
ward_codes = []
lat_list = []
lng_list = []
households = []
population = []

#Show the districts available
print(ofns_api.get_districts())

#Ask the user for a district
district = input("Please type an district and press enter:")

#Get the wards within a district
wards.append(ofns_api.get_wards_from_district(district))

#Get the ward codes within a district
for j in range (0,len(wards[0])):
    ward_codes.append(ofns_api.get_ward_codes_from_district(district, wards[0][j]))
    
print(ward_codes)
    
#Get the households within a district
#households = np.empty(len(wards[0]), dtype = int)
for j in range (0,len(wards[0])):
    households.append(ofns_api.get_households_from_district(district, wards[0][j]))
    
print(households)

#Get the population within a ward
#population = np.empty(len(wards[0]), dtype = int)
for j in range (0,len(wards[0])):
    population.append(population_api.get_population(ward_codes[j]))

print(population)

#Get the coordinates of the wards
for j in range (0,len(wards[0])):
    try:
        coordinates.append(ofns_api.get_ward_polygon(district, wards[0][j]))
    except ValueError as e:
        if str(e) == "Error: Need to specify a district.":
            print("Error: Need to specify a district.")
        elif str(e) == "Error: Could not find district '" + district + "' in the csv.":
            print("Error: Could not find district '" + district + "' in the csv.")
        elif str(e) == "Error: Need to specify a ward.":
            print("Error: Need to specify a ward.")
        elif str(e) == "Error: Could not find ward '" + wards[0][j] + "' from district '" + district + "'.":
            print("Error: Could not find ward '" + wards[0][j] + "' from district '" + district + "'.")
        elif str(e) == "Error: The OFNS server has no coordinate data for ward '" + wards[0][j] + "' from district '" + district + "'.":
            print("Using Doogal API")
            coordinates.append(doogal_api.get_ward_polygon(district, wards[0][j]))


#Seperate the Latitude and Longitude coordinates
for j in range (0,len(wards[0])):
    for k in range (0,len(coordinates[j])):
        lng , lat = map(float, str(coordinates[j][k]).strip('[]').split(','))
        lat_list.append(lat)
        lng_list.append(lng)

#Doogal API Coordinates
transport_max_lat = max(lat_list) + 0.1
transport_min_lat = min(lat_list) - 0.1
transport_max_lng = max(lng_list) + 0.05
transport_min_lng = min(lng_list) - 0.05

max_lat = max(lat_list)
min_lat = min(lat_list)
max_lng = max(lng_list)
min_lng = min(lng_list)

#Google API Coordintes
centre_lat = (max_lat + min_lat)/2
centre_lng = (max_lng + min_lng)/2

coords1 = (max_lat, max_lng)
coords2 = (min_lat, min_lng)
coords3 = (max_lat, min_lng)
coords4 = (min_lat, max_lng)

distance1 = geopy.distance.distance(coords1,coords2).m
distance2 = geopy.distance.distance(coords1,coords3).m
distance3 = geopy.distance.distance(coords1,coords4).m
distance4 = geopy.distance.distance(coords2,coords3).m
distance5 = geopy.distance.distance(coords2,coords4).m
distance6 = geopy.distance.distance(coords3,coords4).m

distance = max(distance1,distance2,distance3,distance4,distance5,distance6)

