import simplekml
from development_district import wards
from development_district import coordinates
from development_district import district
from development_district import ward_codes
from statxplore_api.api import API as STATXPLORE_API
import json

#Define variables / lists
kml = simplekml.Kml()
colour = ['191400FF', '1E1400FF', '231400FF', '281400FF', '2D1400FF', '321400FF', '371400FF', '3C1400FF', '411400FF', '461400FF', '4B1400FF', '501400FF', '551400FF' ,'5A1400FF', '5F1400FF', '641400FF', '691400FF', '6E1400FF', '731400FF', '781400FF', '7D1400FF', '821400FF', '871400FF', '8C1400FF', '911400FF', '961400FF', '9B1400FF', 'A01400FF', 'A51400FF', 'AA1400FF']
#colour = ['1914E7FF', '1E14E7FF', '2314E7FF', '2814E7FF', '2D14E7FF', '3214E7FF', '3714E7FF', '3C14E7FF', '4114E7FF', '4614E7FF', '4B14E7FF', '5014E7FF', '5514E7FF' ,'5A14E7FF', '5F14E7FF', '6414E7FF', '6914E7FF', '6E14E7FF', '7314E7FF', '7814E7FF', '7D14E7FF', '8214E7FF', '8714E7FF', '8C14E7FF', '9114E7FF', '9614E7FF', '9B14E7FF', 'A014E7FF', 'A514E7FF', 'AA14E7FF']

print(ward_codes)

universal_credit = []
pol = []
colour_scale = []
universal_credit_scale = []
statxplore_api = STATXPLORE_API(key_path="../property-fundamentals/statxplore_api/key.txt")

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]
    
    universal_credit.append(statxplore_api.get_universal_credit('table', ward_codes[h]))
    
print(universal_credit)

#Generate price scaling information
max_universal_credit = max(universal_credit)
min_universal_credit = min(universal_credit)
delta = max_universal_credit - min_universal_credit
step = delta / (len(colour)-1)

#Normalise the colours in the price range
for i in range(0,len(colour)):
    colour_scale.insert(i,int(min_universal_credit + (i*step)))

#Assign a colour to the normalised house prices
for j in range(0,len(coordinates)):
    universal_credit_scale.append([])
    for k in range(0,len(colour_scale)):
        if (colour_scale[k] >= universal_credit[j]):
            universal_credit_scale.insert(j,colour[k])
            break
    #Add price and colour to the polygons
    #pol[j].description = json_object["fields"][0]["items"][0]["labels"][0] + ": " + str(int(universal_credit[j])) + " " + json_object["measures"][0]["label"]
    pol[j].style.polystyle.color = universal_credit_scale[j]
    
#Save the polygons to a KML file
kml.save(district + "_universal credit" + ".kml")


