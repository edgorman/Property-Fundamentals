from govuk_api.ofns.api import API as OFNS_API
from doogal_api.api import API as DOOGAL_API
ofns_api = OFNS_API()
doogal_api = DOOGAL_API()

coordinates = []
wards = []

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
