from police_api.api import API as POLICE_API
from doogal_api.api import API as DOOGAL_API
from postcodes_api.postcode_api import API as POSTCODE_API
from development_district import district
from development_district import wards
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
point = []
icon_style = ['images/icon-14.png']
burglary_count = np.array([0]*len(wards[0]))
burglary_percentage = []
yaxis = []
xaxis = []

month1 = (today.month - 5) % 12
year1 = today.year + ((today.month - 5) // 12)
month2 = (today.month - 4) % 12
year2 = today.year + ((today.month - 4) // 12)
month3 = (today.month - 3) % 12
year3 = today.year + ((today.month - 3) // 12)

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
                    #create the KML data
                    point = kml.newpoint()
                    point.name = crime['category']
                    point.description = crime['month']
                    point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
                    point.style.iconstyle.icon.href = icon_style[0]
            
for crime in results2:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        #Create the plot data
        burglary_ward = postcodes_api.get_postcode(str(crime['location']['longitude']),str(crime['location']['latitude']))
        if burglary_ward is not None:
            for i in range (0,len(wards[0])):
                if burglary_ward == wards[0][i]:
                    burglary_count[i] +=1
                    #create the KML data
                    point = kml.newpoint()
                    point.name = crime['category']
                    point.description = crime['month']
                    point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
                    point.style.iconstyle.icon.href = icon_style[0]

for crime in results3:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        #Create the plot data
        burglary_ward = postcodes_api.get_postcode(str(crime['location']['longitude']),str(crime['location']['latitude']))
        if burglary_ward is not None:
            for i in range (0,len(wards[0])):
                if burglary_ward == wards[0][i]:
                    burglary_count[i] +=1
                    #create the KML data
                    point = kml.newpoint()
                    point.name = crime['category']
                    point.description = crime['month']
                    point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
                    point.style.iconstyle.icon.href = icon_style[0]

#Save and zip the KML/KMZ
kml.save(district + "_crime_burglary_percentage" + ".kml")
zf = zipfile.ZipFile(district + "_crime_burglary_percentage" + ".kmz", "w")
zf.write("images/icon-14.png")
zf.write(district + "_crime_burglary_percentage" + ".kml")
zf.close()

#Calculate the burglaies per 1000 households per ward
for i in range (0,len(wards[0])):
    burglary_percentage.append((int(burglary_count[i])*100) / int(households[i]))
    
    
#Arrange the data for the plot
yaxis_order = sorted(range(len(burglary_percentage)), key=lambda k: burglary_percentage[k])
print(yaxis_order)
yaxis.clear()
xaxis.clear()
for j in range(0,len(wards[0])):
    a = yaxis_order[j]
    yaxis.insert(j,wards[0][a])
    xaxis.insert(j,burglary_percentage[a])

#plot the crime data
plt.rcParams["figure.figsize"] = (4.5,5)
plt.rcParams["figure.dpi"] = 200
plt.barh(y_pos, xaxis, color = (0.7578125,0.09375,0.35546875), edgecolor='black') #color = (R,G,B)
plt.yticks(y_pos,yaxis)
plt.xlabel("Percentage (%)")
plt.title(district + " (" + date_range + ") " + ": % of Properties Burgled")
plt.savefig(district + "_burglary_percentage" + ".png", bbox_inches='tight', transparent=True)
plt.clf()