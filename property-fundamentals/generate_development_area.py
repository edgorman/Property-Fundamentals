from govuk_api.ofns.api import API
ofns_api = API()
#ofns_api.get_districts()

coords_raw = []
coords = []
wards_raw = []
wards = []

wards_raw.append(ofns_api.get_ward('Gloucester'))
wards = wards_raw [0]

#j=0
#coords_raw.append(ofns_api.get_ward_polygon('Gloucester', wards[j]))
#print(coords_raw)
#print(ofns_api.get_ward_polygon('Gloucester', wards[j]))

ofns_api.get_ward_polygon('Gloucester', 'Hucclecote')
#coords_raw.append(ofns_api.get_ward_polygon('Gloucester', 'Hucclecote'))
#print(coords_raw)

#for j in range (0,len(wards)):
#    coords_raw.append(ofns_api.get_ward_polygon('Gloucester', wards[j]))
    #coords = coords_raw[j]
#print(coords_raw(0))