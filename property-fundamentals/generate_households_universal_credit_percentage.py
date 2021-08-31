import simplekml
import matplotlib.pyplot as plt
import numpy as np
from development_district import wards
from development_district import coordinates
from development_district import district
from development_district import ward_codes
from development_district import households
from statxplore_api.api import API as STATXPLORE_API
import json

#Define variables / lists
kml = simplekml.Kml()
colour = ['190078F0', '1E0078F0', '230078F0', '280078F0', '2D0078F0', '320078F0', '370078F0', '3C0078F0', '410078F0', '460078F0', '4B0078F0', '500078F0', '550078F0' ,'5A0078F0', '5F0078F0', '640078F0', '690078F0', '6E0078F0', '730078F0', '780078F0', '7D0078F0', '820078F0', '870078F0', '8C0078F0', '910078F0', '960078F0', '9B0078F0', 'A00078F0', 'A50078F0', 'AA0078F0']
colour_plot = ['#F0780019', '#F078001E', '#F0780023', '#F0780028', '#F078002D', '#F0780032', '#F0780037', '#F078003C', '#F0780041', '#F0780046', '#F078004B', '#F0780050', '#F0780055', '#F078005A', '#F078005F', '#F0780064', '#F0780069', '#F078006E', '#F0780073', '#F0780078', '#F078007D', '#F0780082', '#F0780087', '#F078008C', '#F0780091', '#F0780096', '#F078009B', '#F07800A0', '#F07800A5', '#F07800AA']

print(ward_codes)

universal_credit = []
universal_credit_percentage = []
pol = []
colour_scale = []
price_plot = []
y_pos = np.arange(len(wards[0]))
universal_credit_percentage_scale = []
statxplore_api = STATXPLORE_API(key_path="../property-fundamentals/statxplore_api/key.txt")
yaxis = []
xaxis = []
colouraxis = []
month = statxplore_api.get_universal_credit_date('table', ward_codes[0])[:3]
year = statxplore_api.get_universal_credit_date('table', ward_codes[0])[-4:]

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]
    
    universal_credit.append(statxplore_api.get_universal_credit('table', ward_codes[h]))
    universal_credit_percentage.append((float(universal_credit[h])*100) / float(households[h]))
    
print(universal_credit_percentage)

#Generate universal credit scaling information
max_universal_credit_percentage = max(universal_credit_percentage)
min_universal_credit_percentage = min(universal_credit_percentage)
delta = max_universal_credit_percentage - min_universal_credit_percentage
step = delta / (len(colour)-1)

print(max_universal_credit_percentage)
print(min_universal_credit_percentage)
print(delta)
print(step)

#Normalise the colours in the universal credit range
for i in range(0,len(colour)):
    colour_scale.insert(i,(min_universal_credit_percentage + (i*step)))
    
    
print(colour_scale)

#Assign a colour to the normalised universal credit
for j in range(0,len(coordinates)):
    universal_credit_percentage_scale.append([])
    for k in range(0,len(colour_scale)):
        if (colour_scale[k] >= (universal_credit_percentage[j])):
            universal_credit_percentage_scale.insert(j,colour[k])
            price_plot.insert(j,colour_plot[k])
            break
        elif (k == len(colour_scale)-1):
            universal_credit_percentage_scale.insert(j,colour[k])
            price_plot.insert(j,colour_plot[k])
            
    #Add universal credit and colour to the polygons
    pol[j].description = statxplore_api.get_universal_credit_date('table', ward_codes[h]) + ": " + str(universal_credit_percentage[j])[0:4] + "% of Households on Universal Credit"
    pol[j].style.polystyle.color = universal_credit_percentage_scale[j]
    
#Save the polygons to a KML file
kml.save(district + "_universal_credit_percentage" + ".kml")

#Arrange the data for the plot
yaxis_order = sorted(range(len(universal_credit_percentage)), key=lambda k: universal_credit_percentage[k])
print(yaxis_order)
yaxis.clear()
xaxis.clear()
colouraxis.clear()
for j in range(0,len(wards[0])):
    a = yaxis_order[j]
    yaxis.insert(j,wards[0][a])
    xaxis.insert(j,universal_credit_percentage[a])
    colouraxis.insert(j,price_plot[a])

#plot the data
#plt.rcParams["figure.figsize"] = (4.5,5.5) # if there are many wards
plt.rcParams["figure.figsize"] = (4.5,5)
plt.rcParams["figure.dpi"] = 200
plt.barh(y_pos, xaxis, color= colouraxis, edgecolor='black')
plt.yticks(y_pos,yaxis)
plt.xlabel("Percentage (%)")
plt.title(district + " (" + month + "-" + year + ") \n % of Households on Universal Credit")
plt.savefig(district + "_Households_on_universal_credit_percentage" + ".png", bbox_inches='tight', transparent=True)
plt.clf()

