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
    # pol[h].outerboundaryis.coords = coordinates[h]
    # pol[h].style.polystyle.color = '19F07814'

flood_data_result = flood_api.get_flood_data(
    centre_lat,
    centre_lng,
    distance
)

for j in range (0,len(flood_data_result)):
    pol.insert(h,kml.newpolygon())
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[j]
    pol[h].style.polystyle.color = '19F07814'

#Save the polygons to a KML file
kml.save(district + "_flood_data" + ".kml")
