import simplekml
from development_district import wards
from development_district import coordinates
from development_district import district

#Define variables / lists
kml = simplekml.Kml()
pol = []

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]
    pol[h].style.polystyle.color = '64FFFFFF'#'0FF07814'
    
kml.save(district + "_Google_Earth" + ".kml") 



