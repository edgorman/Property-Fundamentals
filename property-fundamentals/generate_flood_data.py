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

#Generate / Draw polygons
# for h in range(0,len(coordinates)):
    # pol.insert(h,kml.newpolygon())
    # pol[h].name = wards[0][h]
    # pol[h].style.linestyle.width = "0"
    # print(coordinates[h])
    # pol[h].outerboundaryis.coords = coordinates[h]
    # pol[h].style.polystyle.color = '19F07814'

flood_data_result = flood_api.get_flood_data(
    centre_lat,
    centre_lng,
    0.1
    #int(distance/1000)
)

print(len(flood_data_result))
print(centre_lat)
print(centre_lng)
#print(int(distance/1000))
print(flood_data_result[0][0][0])

count=0
#print(flood_data_result[0][0][0])

# for j in range (0,len(flood_data_result)):
    # for k in range (0,len(flood_data_result[j])):
        # for l in range (0,len(flood_data_result[j][k])):
            # pol.insert(count,kml.newpolygon())
            # pol[count].style.linestyle.width = "0"
            # pol[count].outerboundaryis.coords = str(flood_data_result[j][k][l])
            # pol[count].style.polystyle.color = '19F07814'
        # count +=1
        
pol.insert(0,kml.newpolygon())
pol[0].style.linestyle.width = "0"
pol[0].outerboundaryis.coords = str(flood_data_result[0][0][0])
pol[0].style.polystyle.color = '19F07814'

#Save the polygons to a KML file
kml.save(district + "_flood_data" + ".kml")
