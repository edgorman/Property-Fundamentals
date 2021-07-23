import simplekml
import matplotlib.pyplot as plt
import numpy as np
from development_district import wards
from development_district import coordinates
from development_district import district
from development_district import ward_codes
from statxplore_api.api import API as STATXPLORE_API
import json

#Define variables / lists
kml = simplekml.Kml()
colour = ['191400FF', '1E1400FF', '231400FF', '281400FF', '2D1400FF', '321400FF', '371400FF', '3C1400FF', '411400FF', '461400FF', '4B1400FF', '501400FF', '551400FF' ,'5A1400FF', '5F1400FF', '641400FF', '691400FF', '6E1400FF', '731400FF', '781400FF', '7D1400FF', '821400FF', '871400FF', '8C1400FF', '911400FF', '961400FF', '9B1400FF', 'A01400FF', 'A51400FF', 'AA1400FF']
colour_plot = ['#FF001419', '#FF00141E', '#FF001423', '#FF001428', '#FF00142D', '#FF001432', '#FF001437', '#FF00143C', '#FF001441', '#FF001446', '#FF00144B', '#FF001450', '#FF001455', '#FF00145A', '#FF00145F', '#FF001464', '#FF001469', '#FF00146E', '#FF001473', '#FF001478', '#FF00147D', '#FF001482', '#FF001487', '#FF00148C', '#FF001491', '#FF001496', '#FF00149B', '#FF0014A0', '#FF0014A5', '#FF0014AA']

print(ward_codes)

universal_credit = []
pol = []
colour_scale = []
price_plot = []
y_pos = np.arange(len(wards[0]))
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
            price_plot.insert(j,colour_plot[k])
            break
    #Add price and colour to the polygons
    pol[j].description = statxplore_api.get_universal_credit_date('table', ward_codes[h]) + ": " + str(int(universal_credit[j])) + " Households on universal credit"
    pol[j].style.polystyle.color = universal_credit_scale[j]
    
#Save the polygons to a KML file
kml.save(district + "_universal_credit" + ".kml")

#plot the data
plt.barh(y_pos, universal_credit, color= price_plot, edgecolor='black')
plt.yticks(y_pos,wards[0])
plt.gca().invert_yaxis()
plt.xlabel("Number of Households")
plt.title(district + " Households on Universal Credit")
#plt.rcParams["figure.figsize"] = (20,3)
#plt.savefig(district + "_Households_on_universal_credit" + ".png")
plt.savefig(district + "_Households_on_universal_credit" + ".png", bbox_inches='tight')
plt.clf()
