from govuk_api.ofns.api import API as OFNS_API
from doogal_api.api import API as DOOGAL_API
from generate_development_district import district
from generate_development_district import coordinates
from generate_development_district import max_lat
from generate_development_district import min_lat
from generate_development_district import max_lng
from generate_development_district import min_lng
ofns_api = OFNS_API()
doogal_api = DOOGAL_API()
import json
import simplekml
import zipfile
kml = simplekml.Kml()

point = []
icon_style = ['images/icon-5.png']
parameters = {
    'minLat': min_lat,
    'minLng': min_lng,
    'maxLat': max_lat,
    'maxLng': max_lng,
}
result = doogal_api.request('GetPlacesNear.ashx', parameters).read().decode('utf-8')
places = json.loads(result)

for place in places:
    if place['type'] == 'Railway Station':
        point = kml.newpoint()
        point.name = place['name']
        point.description = place['type']
        point.coords = [(place['lng'],place['lat'])]
        point.style.iconstyle.icon.href = icon_style[0] 
kml.save(district + "_train_station" + ".kml")
        
zf = zipfile.ZipFile(district + "_train_station" + ".kmz", "w")
zf.write("images/icon-5.png")
zf.write(district + "_train_station" + ".kml")
zf.close()