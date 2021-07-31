from police_api.api import API as POLICE_API
from doogal_api.api import API as DOOGAL_API
from postcodes_api.postcode_api import API as POSTCODE_API
from development_district import district
from development_district import wards
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
crime_count = np.array([0]*len(wards[0]))

month1 = (today.month - 5) % 12
year1 = today.year + ((today.month - 5) // 12)
month2 = (today.month - 4) % 12
year2 = today.year + ((today.month - 4) // 12)
month3 = (today.month - 3) % 12
year3 = today.year + ((today.month - 3) // 12)

print((str(year1) + "-" + (f"{month1:02}")))
print((str(year2) + "-" + (f"{month2:02}")))
print((str(year3) + "-" + (f"{month3:02}")))

results1 = police_api.get_street_level_crimes(centre_lat, centre_lng, distance, (str(year1) + "-" + (f"{month1:02}")))
results2 = police_api.get_street_level_crimes(centre_lat, centre_lng, distance, (str(year2) + "-" + (f"{month2:02}")))
results3 = police_api.get_street_level_crimes(centre_lat, centre_lng, distance, (str(year3) + "-" + (f"{month3:02}")))

for crime in results1:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        if crime['category'] == 'burglary':
            #Create the plot data
            crime_ward = postcodes_api.get_postcode(str(crime['location']['longitude']),str(crime['location']['latitude']))
            if crime_ward is not None:
                for i in range (0,len(wards[0])):
                    if crime_ward == wards[0][i]:
                        crime_count[i] +=1
                        #create the KML data
                        point = kml.newpoint()
                        point.name = crime['category']
                        point.description = crime['month']
                        point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
                        point.style.iconstyle.icon.href = icon_style[0]
            
for crime in results2:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        if crime['category'] == 'burglary':
            #Create the plot data
            crime_ward = postcodes_api.get_postcode(str(crime['location']['longitude']),str(crime['location']['latitude']))
            if crime_ward is not None:
                for i in range (0,len(wards[0])):
                    if crime_ward == wards[0][i]:
                        crime_count[i] +=1
                        #create the KML data
                        point = kml.newpoint()
                        point.name = crime['category']
                        point.description = crime['month']
                        point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
                        point.style.iconstyle.icon.href = icon_style[0]

for crime in results3:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        if crime['category'] == 'burglary':
            #Create the plot data
            crime_ward = postcodes_api.get_postcode(str(crime['location']['longitude']),str(crime['location']['latitude']))
            if crime_ward is not None:
                for i in range (0,len(wards[0])):
                    if crime_ward == wards[0][i]:
                        crime_count[i] +=1
                        #create the KML data
                        point = kml.newpoint()
                        point.name = crime['category']
                        point.description = crime['month']
                        point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
                        point.style.iconstyle.icon.href = icon_style[0]

#Save and zip the KML/KMZ
kml.save(district + "_crime_burglary" + ".kml")
zf = zipfile.ZipFile(district + "_crime_burglary" + ".kmz", "w")
zf.write("images/icon-14.png")
zf.write(district + "_crime_burglary" + ".kml")
zf.close()

#plot the crime data
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.barh(y_pos, crime_count, color = 'red', edgecolor='black')
plt.yticks(y_pos,wards[0])
plt.gca().invert_yaxis()
plt.xlabel("Number of Burglaries")
plt.title(district + " Burglaries in the last 3 Months",weight='bold')
plt.savefig(district + "_burglaries" + ".png", bbox_inches='tight', transparent=True)
plt.clf()