from govuk_api.ofns.api import API as OFNS_API
from google_api.api import API as GOOGLE_API
from generate_development_district import district
from generate_development_district import coordinates
from generate_development_district import centre_lat
from generate_development_district import centre_lng
from generate_development_district import distance

ofns_api = OFNS_API()
google_api = API(key_path="../property-fundamentals/google_api/key.txt")
import json
import simplekml
import zipfile
kml = simplekml.Kml()

point = []
icon_style = ['images/icon-6.png']

supermarket_result = google_api.nearby_search(
    centre_lat,
    centre_lng,
    distance,
    location_type='supermarket'
)

for place in supermarket_result:
    point = kml.newpoint()
    point.name = place['name']
    point.description = place['type']
    point.coords = [(place['lng'],place['lat'])]
    point.style.iconstyle.icon.href = icon_style[0] 
kml.save(district + "_supermarket" + ".kml")
        
zf = zipfile.ZipFile(district + "_supermarket" + ".kmz", "w")
zf.write("images/icon-6.png")
zf.write(district + "_supermarket" + ".kml")
zf.close()