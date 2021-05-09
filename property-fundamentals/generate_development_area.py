from govuk_api.ofns.api import API
ofns_api = API()
#ofns_api.get_districts()

coordinates_raw = []
coordinates = []
wards_raw = []
wards = []

wards_raw.append(ofns_api.get_ward('Gloucester'))
wards = wards_raw [0]

#for j in range (0,len(wards)):
#    coordinates_raw.append(ofns_api.get_ward_polygon('Gloucester', wards[j]))
#    coordinates = coordinates_raw[j]