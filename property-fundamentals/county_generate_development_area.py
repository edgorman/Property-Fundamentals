from govuk_api.ofns.api import API
ofns_api = API()

coordinates = []
districts = []
wards = []

#Show the counties available
print(ofns_api.get_counties())

#Ask the user for a county
county = input("Please type a county and press enter:")

#Get the districts within a county
districts.append(ofns_api.get_districts_from_county(county))

print(districts)

#Get the wards within a district
for j in range (0,len(districts[0])):
    wards.append(ofns_api.get_wards_from_district(districts[0][j]))

print(wards)
print(len(wards))
print(len(wards[0]))

#Get the coordinates of the wards
for j in range (0,len(districts[0])):
    coordinates.append([])
    for k in range (0,len(wards[j])):
        print(districts[0][j])
        print(wards[j][k])
        coordinates.append(ofns_api.get_ward_polygon(districts[0][j], wards[j][k]))
   
print(coordinates)