from govuk_api.ofns.api import API as OFNS_API
from doogal_api.api import API as DOOGAL_API
from google_api.api import API as GOOGLE_API
from development_district import district
from development_district import coordinates
from development_district import max_lat
from development_district import min_lat
from development_district import max_lng
from development_district import min_lng
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

parameters = {
    'minLat': min_lat,
    'minLng': min_lng,
    'maxLat': max_lat,
    'maxLng': max_lng,
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

kml.save(district + "_transport_small" + ".kml")
        
zf = zipfile.ZipFile(district + "_transport_small" + ".kmz", "w")
zf.write("images/icon-5.png")
zf.write("images/icon-6.png")
zf.write("images/icon-7.png")
zf.write("images/icon-8.png")
zf.write("images/icon-9.png")
zf.write("images/icon-11.png")
zf.write(district + "_transport_small" + ".kml")
zf.close()