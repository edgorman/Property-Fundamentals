from police_api.api import API as POLICE_API
from doogal_api.api import API as DOOGAL_API
from postcodes_api.postcode_api import API as POSTCODE_API
from development_district import district
from development_district import wards
from development_district import coordinates
from development_district import households
from development_district import max_lat
from development_district import min_lat
from development_district import max_lng
from development_district import min_lng
from development_district import centre_lat
from development_district import centre_lng
from development_district import distance
import datetime
import matplotlib.pyplot as plt
import numpy as np
import json

y_pos = np.arange(len(wards[0]))
police_api = POLICE_API()
doogal_api = DOOGAL_API()
postcodes_api = POSTCODE_API()
import simplekml
import zipfile
kml = simplekml.Kml()
today = datetime.date.today()
pol = []
colour_scale = []
price_plot = []
icon_style = ['images/icon-14.png']
burglary_count = np.array([0]*len(wards[0]))
burglary_percentage = []
yaxis = []
xaxis = []
colouraxis = []
colour = ['191400FF', '1E1400FF', '231400FF', '281400FF', '2D1400FF', '321400FF', '371400FF', '3C1400FF', '411400FF', '461400FF', '4B1400FF', '501400FF', '551400FF' ,'5A1400FF', '5F1400FF', '641400FF', '691400FF', '6E1400FF', '731400FF', '781400FF', '7D1400FF', '821400FF', '871400FF', '8C1400FF', '911400FF', '961400FF', '9B1400FF', 'A01400FF', 'A51400FF', 'AA1400FF']
colour_plot = ['#FF001419', '#FF00141E', '#FF001423', '#FF001428', '#FF00142D', '#FF001432', '#FF001437', '#FF00143C', '#FF001441', '#FF001446', '#FF00144B', '#FF001450', '#FF001455', '#FF00145A', '#FF00145F', '#FF001464', '#FF001469', '#FF00146E', '#FF001473', '#FF001478', '#FF00147D', '#FF001482', '#FF001487', '#FF00148C', '#FF001491', '#FF001496', '#FF00149B', '#FF0014A0', '#FF0014A5', '#FF0014AA']
burglary_percentage_scale = []

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]

month1 = (today.month - 5) % 12
year1 = today.year + ((today.month - 5) // 12)
month2 = (today.month - 4) % 12
year2 = today.year + ((today.month - 4) // 12)
month3 = (today.month - 3) % 12
year3 = today.year + ((today.month - 3) // 12)

if month1 == 0:
    month1 = 12
    year1 -=1
elif month2 == 0:
    month2 = 12
    year2 -=1
elif month3 == 0:
    month3 = 12
    year3 -=1    

print(month1)
print(month2)
print(month3)
print(year1)
print(year2)
print(year3)
print(today.month)

date_range = datetime.date(year1,month1,1).strftime("%b") + "-" + str(year1) + " to " + datetime.date(year1,month3,1).strftime("%b") + "-" + str(year3)

print((str(year1) + "-" + (f"{month1:02}")))
print((str(year2) + "-" + (f"{month2:02}")))
print((str(year3) + "-" + (f"{month3:02}")))

results1 = police_api.get_burglary_street_level_crimes(centre_lat, centre_lng, distance, (str(year1) + "-" + (f"{month1:02}")))
results2 = police_api.get_burglary_street_level_crimes(centre_lat, centre_lng, distance, (str(year2) + "-" + (f"{month2:02}")))
results3 = police_api.get_burglary_street_level_crimes(centre_lat, centre_lng, distance, (str(year3) + "-" + (f"{month3:02}")))

for crime in results1:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        #Create the plot data
        burglary_ward = postcodes_api.get_postcode(str(crime['location']['longitude']),str(crime['location']['latitude']))
        if burglary_ward is not None:
            for i in range (0,len(wards[0])):
                if burglary_ward == wards[0][i]:
                    burglary_count[i] +=1
            
for crime in results2:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        #Create the plot data
        burglary_ward = postcodes_api.get_postcode(str(crime['location']['longitude']),str(crime['location']['latitude']))
        if burglary_ward is not None:
            for i in range (0,len(wards[0])):
                if burglary_ward == wards[0][i]:
                    burglary_count[i] +=1

for crime in results3:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        #Create the plot data
        burglary_ward = postcodes_api.get_postcode(str(crime['location']['longitude']),str(crime['location']['latitude']))
        if burglary_ward is not None:
            for i in range (0,len(wards[0])):
                if burglary_ward == wards[0][i]:
                    burglary_count[i] +=1

#Calculate the burglaies percentage per ward
for i in range (0,len(wards[0])):
    burglary_percentage.append((int(burglary_count[i])*100) / int(households[i]))
    
#Generate burglary scaling information
max_burglary_percentage = max(burglary_percentage)
min_burglary_percentage = min(burglary_percentage)
delta = max_burglary_percentage - min_burglary_percentage
step = delta / (len(colour)-1)

print(max_burglary_percentage)
print(min_burglary_percentage)
print(delta)
print(step)

#Normalise the colours in the burglary percentage range
for i in range(0,len(colour)):
    colour_scale.insert(i,float(min_burglary_percentage + (i*step)))
    
#Assign a colour to the normalised burglary percentage
for j in range(0,len(coordinates)):
    burglary_percentage_scale.append([])
    for k in range(0,len(colour_scale)):
        if (colour_scale[k] >= burglary_percentage[j]):
            burglary_percentage_scale.insert(j,colour[k])
            price_plot.insert(j,colour_plot[k])
            break
        elif (k == len(colour_scale)-1):
            burglary_percentage_scale.insert(j,colour[k])
            price_plot.insert(j,colour_plot[k])
            
    #Add universal credit and colour to the polygons
    pol[j].description = date_range + ": " + str(burglary_percentage[j])[0:4] + "% of Households burgled per Ward"
    pol[j].style.polystyle.color = burglary_percentage_scale[j]
    
#Save the polygons to a KML file
kml.save(district + "_crime_burglary_percentage" + ".kml")
    
#Arrange the data for the plot
yaxis_order = sorted(range(len(burglary_percentage)), key=lambda k: burglary_percentage[k])
print(yaxis_order)
yaxis.clear()
xaxis.clear()
for j in range(0,len(wards[0])):
    a = yaxis_order[j]
    yaxis.insert(j,wards[0][a])
    xaxis.insert(j,burglary_percentage[a])
    colouraxis.insert(j,price_plot[a])

#plot the crime data
#plt.rcParams["figure.figsize"] = (4.5,5.5) # if there are many wards
plt.rcParams["figure.figsize"] = (4.5,5)
plt.rcParams["figure.dpi"] = 200
plt.rcParams.update({'font.size': 7})
plt.barh(y_pos, xaxis, color = colouraxis, edgecolor='black') #color = (R,G,B)
plt.yticks(y_pos,yaxis)
plt.xlabel("Percentage (%)")
plt.title(district + " (" + date_range + ")" + " \n % of Properties Burgled")
plt.savefig(district + "_burglary_percentage" + ".png", bbox_inches='tight', transparent=True)
plt.clf()