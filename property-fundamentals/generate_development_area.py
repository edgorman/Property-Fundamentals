from doogal.api import API
doogal_api = API()

coordinates = []
wards = []

#Show the districts available
print(doogal_api.get_districts())

#Ask the user for a district
area = input("Please type an area and press enter:")

#Get the wards within a district
wards.append(doogal_api.get_wards_from_district(area))

#Get the coordinates of the wards
for j in range (0,len(wards[0])):
    coordinates.append(doogal_api.get_ward_polygon(area, wards[0][j]))
   
