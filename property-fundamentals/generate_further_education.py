from govuk_api.ofns.api import API as OFNS_API
from google_api.api import API as GOOGLE_API
from doogal_api.api import API as DOOGAL_API
#from govuk_ws.geoportal.postcode_to_ward import PostcodeMapping
from postcodes_api.postcode_api import API as POSTCODE_API
from development_district import district
from development_district import wards
from development_district import coordinates
from development_district import centre_lat
from development_district import centre_lng
from development_district import distance
from development_district import max_lat
from development_district import min_lat
from development_district import max_lng
from development_district import min_lng
import matplotlib.pyplot as plt
import numpy as np
import json
import datetime

doogal_api = DOOGAL_API()
ofns_api = OFNS_API()
google_api = GOOGLE_API(key_path="../property-fundamentals/google_api/key.txt")
#postcode_mapping = PostcodeMapping()
postcodes_api = POSTCODE_API()
import simplekml
import zipfile
kml = simplekml.Kml()

y_pos = np.arange(len(wards[0]))
point = []
icon_style = ['images/icon-10.png']
further_education_count = np.array([0]*len(wards[0]))
yaxis = []
xaxis = []
pol = []

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]
    pol[h].style.polystyle.color = '32F07814' #= '19F07814'

today_month = datetime.date.today().strftime("%b")
today_year = datetime.date.today().strftime("%Y")

further_education_result = google_api.nearby_search(
    centre_lat,
    centre_lng,
    distance,
    location_type='university'
)

for j in range (0,len(further_education_result)):
    if (further_education_result[j][2]['lat'] <= max_lat) and (further_education_result[j][2]['lat'] >= min_lat) and (further_education_result[j][2]['lng'] <= max_lng) and (further_education_result[j][2]['lng'] >= min_lng):
        #Create the plot
        further_education_ward = postcodes_api.get_ward(str(further_education_result[j][2]['lng']),str(further_education_result[j][2]['lat']))
        further_education_postcode = postcodes_api.get_postcode(str(further_education_result[j][2]['lng']),str(further_education_result[j][2]['lat']))
        
        #Check ward is present in list
        ward_found = False
        for i in range (0,len(wards[0])):
            if further_education_ward == wards[0][i]:
                ward_found = True
        if ward_found == True:
            print("ward found")
        elif ward_found == False:
            print("ward not found.\n wards available are:\n")
            print(wards[0])
            print("Postcode is: ")
            print(further_education_postcode)
            print("further education ward is currently: ")
            print(further_education_ward)
            further_education_ward = input("Please type a ward from the list and press enter:\n\n (If you don't choose a ward from the list it will not be included in the chart)")
        
        
        if further_education_ward is not None:
            for i in range (0,len(wards[0])):
                if further_education_ward == wards[0][i]:
                    further_education_count[i] +=1
            #create the KML
            point = kml.newpoint()
            point.name = further_education_result[j][0]
            point.description = further_education_result[j][0]
            point.coords = [(further_education_result[j][2]['lng'],further_education_result[j][2]['lat'])]
            point.style.iconstyle.icon.href = icon_style[0]

#Save and zip the KML/KMZ  
kml.save(district + "_further_education" + ".kml")
zf = zipfile.ZipFile(district + "_further_education" + ".kmz", "w")
zf.write("images/icon-10.png")
zf.write(district + "_further_education" + ".kml")
zf.close()

#Arrange the data for the plot
yaxis_order = sorted(range(len(further_education_count)), key=lambda k: further_education_count[k])
print(yaxis_order)
yaxis.clear()
#i=len(wards[0])
for j in range(0,len(wards[0])):
    a = yaxis_order[j]
    #yaxis.insert(j, (str(i) + ". " + wards[0][a]))
    yaxis.insert(j, wards[0][a])
    xaxis.insert(j,further_education_count[a])
    #i-=1

#plot the further education data
#plt.rcParams["figure.figsize"] = (5,5.5) # if there are many wards
plt.rcParams["figure.figsize"] = (4.5,5)
plt.rcParams["figure.dpi"] = 200
plt.rcParams.update({'font.size': 7})
plt.barh(y_pos, xaxis, color = (0.1015625,0.13671875,0.4921875), edgecolor='black') #color = (R,G,B)
plt.yticks(y_pos,yaxis)
plt.xlabel("Number of Further Education Institutions")
plt.title(district + " (" + today_month + "-" + today_year + ") \n Further Education Institutions")
plt.savefig(district + "_further_education" + ".png", bbox_inches='tight', transparent=True)
plt.clf()
