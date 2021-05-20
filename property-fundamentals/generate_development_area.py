from govuk_api.ofns.api import API
ofns_api = API()

coordinates = []
wards = []

#Show the areas available
print(ofns_api.get_districts())

#Ask the user for an area
area = input("Please type an area and press enter:")

#Get the wards within an area
wards.append(ofns_api.get_wards_from_district(area))

#Get the coordinates of the wards
for j in range (0,len(wards[0])):
    coordinates.append(ofns_api.get_ward_polygon(area, wards[0][j]))
   
