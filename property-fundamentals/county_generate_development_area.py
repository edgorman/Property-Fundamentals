from govuk_api.ofns.api import API
ofns_api = API()

districts = []
wards = []
max_ward_length = 0

#Show the counties available
print(ofns_api.get_counties())

#Ask the user for a county
county = input("Please type a county and press enter:")

#Get the districts within a county
districts.append(ofns_api.get_districts_from_county(county))

#Get the wards within a district
for j in range (0,len(districts[0])):
    wards.append(ofns_api.get_wards_from_district(districts[0][j]))

for m in range (0, len(wards)):
    if (len(wards[m]) > max_ward_length):
        max_ward_length = len(wards[m])
print(max_ward_length)
        
coordinates = [[] for i in range (len(wards))]

for n in range (0, len(wards)):
    coordinates[n] = [[] for i in range (max_ward_length)]
    
#Get the coordinates of the wards
print(len(wards))
print(coordinates)
print(coordinates[0])
print(coordinates[0][0])
for j in range (0,len(wards)):
    for m in range (0, max_ward_length):
        for k in range (0,len(wards[j])):
            coordinates[j][m].insert(k, ofns_api.get_ward_polygon(districts[0][j], wards[j][k]))
# print(coordinates)