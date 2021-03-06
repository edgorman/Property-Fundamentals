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
from environment_data_api.api import API as FLOOD_API
import numpy as np
import json

flood_api = FLOOD_API()
import simplekml
kml = simplekml.Kml()

point = []
flood_data_count = np.array([0]*len(wards[0]))
pol = []
count=0

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    print(coordinates[h])
    pol[h].outerboundaryis.coords = coordinates[h]
    pol[h].style.polystyle.color = '32F07814' #= '19F07814'

flood_data_result = flood_api.get_flood_data(
    centre_lat,
    centre_lng,
    1
    #int(distance/1000)
)



for j in range (0,len(flood_data_result)):
    print (len(flood_data_result[j]))
    print (flood_data_result[j])
    for k in range (0,len(flood_data_result[j])):
        if str(flood_data_result[j])[0:4] == "[[[[":
        #if len(flood_data_result[j]) != 1:
            for l in range (0,len(flood_data_result[j][k])):
                pol.insert(count,kml.newpolygon())
                pol[count].style.linestyle.width = "0"
                pol[count].outerboundaryis.coords = flood_data_result[j][k][l]
                pol[count].style.polystyle.color = 'FFF07814'
            count +=1
        elif str(flood_data_result[j])[0:4] != "[[[[":
        #elif len(flood_data_result[j]) == 1:
            pol.insert(count,kml.newpolygon())
            pol[count].style.linestyle.width = "0"
            pol[count].outerboundaryis.coords = flood_data_result[j][k]
            pol[count].style.polystyle.color = 'FFF07814'
            count +=1
        else:
            print("error")
        
#Save the polygons to a KML file
kml.save(district + "_flood_data" + ".kml")
