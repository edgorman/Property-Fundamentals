import simplekml
from generate_development_area import wards
from generate_development_area import coordinates
from generate_development_area import area
from generate_property_price import price_median
from generate_property_price import house_types

#Define variables / lists
kml = simplekml.Kml()
colour = ['4C14E7FF','4C14DEFF','4C14D5FF','4C14CCFF','4C14C3FF','4C14BAFF','4C14B1FF','4C14A8FF','4C14A0FF','4C1497FF','4C148EFF','4C1485FF','4C147CFF','4C1473FF','4C146AFF','4C1461FF','4C1458FF','4C1450FF','4C1447FF','4C143EFF','4C1435FF','4C142CFF','4C1423FF','4C141AFF','4C1411FF','4C1408FF','4C1400FF']
pol = []
colour_scale = []
price_scale = []

#Generate / Draw KML polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]

#Generate price scaling information
max_price = max(price_median[0])
min_price = min(price_median[0])
print(max_price)
print(min_price)
delta = max_price - min_price
step = delta / (len(colour)-1)    

#Normalise the colours in the price range
for i in range(0,len(colour)):
    colour_scale.insert(i,int(min_price + (i*step)))
print(colour_scale)
print(len(colour_scale))
print(len(wards[0]))
print(len(coordinates))

#Assign a colour to the normalised house prices
for j in range(0,len(coordinates)):
    #price_scale.append([])
    for k in range(0,len(colour_scale)):
        if (colour_scale[k] >= price_median[0][j]):
            price_scale.insert(j,colour[k])
            break
print(price_scale)

#Add price and colour to the polygons
for m in range(0,len(coordinates)):
    pol[m].description = "£" + str(price_median[0][m])
    pol[m].style.polystyle.color = price_scale[m]


#Save the polygons to a KML file
kml.save(area + "_median_" + house_types[0][0] + ".kml")



