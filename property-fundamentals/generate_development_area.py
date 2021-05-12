from govuk_api.ofns.api import API
ofns_api = API()
#ofns_api.get_districts()

coordinates = []
wards = []

wards.append(ofns_api.get_ward('Gloucester'))

for j in range (0,len(wards[0])):
    coordinates.append(ofns_api.get_ward_polygon('Gloucester', wards[0][j]))
    
# with open('test.txt','w')as f:
    # for element in coordinates:
        # f.write("%s\n" % element)
