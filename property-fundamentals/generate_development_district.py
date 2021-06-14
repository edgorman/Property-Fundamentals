from govuk_api.ofns.api import API as OFNS_API
from doogal_api.api import API as DOOGAL_API
from math import sin, cos, sqrt, atan2, radians
ofns_api = OFNS_API()
doogal_api = DOOGAL_API()

coordinates = []
wards = []
lat_list = []
lng_list = []

#Show the districts available
print(ofns_api.get_districts())

#Ask the user for a district
district = input("Please type an district and press enter:")

#Get the wards within a district
wards.append(ofns_api.get_wards_from_district(district))

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
max_lat = max(lat_list)
min_lat = min(lat_list)
max_lng = max(lng_list)
min_lng = min(lng_list)

#Google API Coordintes
centre_lat = (max_lat + min_lat)/2
centre_lng = (max_lng + min_lng)/2

R = 6373000

max_lat_rad = radians(max_lat)
min_lat_rad = radians(min_lat)
max_lng_rad = radians(max_lng)
min_lng_rad = radians(min_lng)

dlon = min_lng_rad - max_lng_rad
dlat = min_lat_rad - max_lat_rad

a = sin(dlat / 2)**2 + cos(min_lat_rad) * cos(max_lat_rad) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print(distance)
print(centre_lat)
print(centre_lng)
