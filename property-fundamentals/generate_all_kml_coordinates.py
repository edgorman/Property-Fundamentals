from govuk_api.ofns.api import API as OFNS_API
from doogal_api.api import API as DOOGAL_API
ofns_api = OFNS_API()
doogal_api = DOOGAL_API()
import geopy.distance
import numpy as np

coordinates = []
wards = []

district = ofns_api.get_districts()
print(district)

#Ask the user for a district
Number_string = input("Please type an district number:")
Number = int(Number_string)

wards.append(ofns_api.get_wards_from_district(district[Number]))

for j in range (0,len(wards[0])):
    try:
        coordinates.append(ofns_api.get_ward_polygon(district[Number], wards[0][j]))
    except ValueError as e:
        if str(e) == "Error: Need to specify a district.":
            print("Error: Need to specify a district.")
        elif str(e) == "Error: Could not find district '" + district[Number] + "' in the csv.":
            print("Error: Could not find district '" + district[Number] + "' in the csv.")
        elif str(e) == "Error: Need to specify a ward.":
            print("Error: Need to specify a ward.")
        elif str(e) == "Error: Could not find ward '" + wards[0][j] + "' from district '" + district[Number] + "'.":
            print("Error: Could not find ward '" + wards[0][j] + "' from district '" + district[Number] + "'.")
        elif str(e) == "Error: The OFNS server has no coordinate data for ward '" + wards[0][j] + "' from district '" + district[Number] + "'.":
            print("Using Doogal API")
            coordinates.append(doogal_api.get_ward_polygon(district[Number], wards[0][j]))

with open("C:/Users/Anchal Goel/Desktop/Coordinates/" + district[Number] + "_coordinates.txt", "w") as f:
    for item in coordinates:
        f.write("%s\n" % coordinates)
coordinates.clear()



