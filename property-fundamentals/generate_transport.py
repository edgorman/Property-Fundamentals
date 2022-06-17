from govuk_api.ofns.api import API as OFNS_API
from doogal_api.api import API as DOOGAL_API
from google_api.api import API as GOOGLE_API
from development_district import district
from development_district import coordinates
from development_district import wards
from development_district import transport_max_lat
from development_district import transport_min_lat
from development_district import transport_max_lng
from development_district import transport_min_lng
from development_district import centre_lat
from development_district import centre_lng
from development_district import distance
ofns_api = OFNS_API()
doogal_api = DOOGAL_API()
ofns_api = OFNS_API()
google_api = GOOGLE_API(key_path="../property-fundamentals/google_api/key.txt")
import json
import simplekml
import zipfile
kml = simplekml.Kml()

point = []
icon_style = ['images/icon-5.png','images/icon-6.png','images/icon-7.png','images/icon-8.png','images/icon-9.png','images/icon-11.png']

colour = ['19F07814', '1EF07814', '23F07814', '28F07814', '2DF07814', '32F07814', '37F07814', '3CF07814', '41F07814', '46F07814', '4BF07814', '50F07814', '55F07814' ,'5AF07814', '5FF07814', '64F07814', '69F07814', '6EF07814', '73F07814', '78F07814', '7DF07814', '82F07814', '87F07814', '8CF07814', '91F07814', '96F07814', '9BF07814', 'A0F07814', 'A5F07814', 'AAF07814']
pol = []

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]
    pol[h].style.polystyle.color = '32F07814' #= '19F07814'

parameters = {
    'minLat': transport_min_lat,
    'minLng': transport_min_lng,
    'maxLat': transport_max_lat,
    'maxLng': transport_max_lng,
}
result = doogal_api.request('GetPlacesNear.ashx', parameters).read().decode('utf-8')
places = json.loads(result)

subway_station_result = google_api.nearby_search(
    centre_lat,
    centre_lng,
    distance,
    location_type='subway_station'
)

for place in places:
    if place['type'] == 'Railway Station':
        point = kml.newpoint()
        point.name = place['name']
        point.description = place['type']
        point.coords = [(place['lng'],place['lat'])]
        point.style.iconstyle.icon.href = icon_style[0]
    if place['type'] == 'Bus/Coach Station':
        point = kml.newpoint()
        point.name = place['name']
        point.description = place['type']
        point.coords = [(place['lng'],place['lat'])]
        point.style.iconstyle.icon.href = icon_style[1]
    if place['type'] == 'Airport':
        point = kml.newpoint()
        point.name = place['name']
        point.description = place['type']
        point.coords = [(place['lng'],place['lat'])]
        point.style.iconstyle.icon.href = icon_style[2]
    if place['type'] == 'Tramway':
        point = kml.newpoint()
        point.name = place['name']
        point.description = place['type']
        point.coords = [(place['lng'],place['lat'])]
        point.style.iconstyle.icon.href = icon_style[3]
    if place['type'] == 'Ferry Terminal':
        point = kml.newpoint()
        point.name = place['name']
        point.description = place['type']
        point.coords = [(place['lng'],place['lat'])]
        point.style.iconstyle.icon.href = icon_style[4]
        
for j in range (0,len(subway_station_result)):
    point = kml.newpoint()
    point.name = subway_station_result[j][0]
    point.description = subway_station_result[j][0]
    point.coords = [(subway_station_result[j][2]['lng'],subway_station_result[j][2]['lat'])]
    point.style.iconstyle.icon.href = icon_style[5] 

kml.save(district + "_transport" + ".kml")
        
zf = zipfile.ZipFile(district + "_transport" + ".kmz", "w")
zf.write("images/icon-5.png")
zf.write("images/icon-6.png")
zf.write("images/icon-7.png")
zf.write("images/icon-8.png")
zf.write("images/icon-9.png")
zf.write("images/icon-11.png")
zf.write(district + "_transport" + ".kml")
zf.close()