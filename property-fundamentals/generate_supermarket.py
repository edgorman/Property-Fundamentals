from govuk_api.ofns.api import API as OFNS_API
from google_api.api import API as GOOGLE_API
from development_district import district
from development_district import coordinates
from development_district import centre_lat
from development_district import centre_lng
from development_district import distance

ofns_api = OFNS_API()
google_api = GOOGLE_API(key_path="../property-fundamentals/google_api/key.txt")
import simplekml
import zipfile
kml = simplekml.Kml()

point = []
icon_style = ['images/icon-10.png']

supermarket_result = google_api.nearby_search(
    centre_lat,
    centre_lng,
    distance,
    location_type='supermarket'
)

for j in range (0,len(supermarket_result)):
    point = kml.newpoint()
    point.name = supermarket_result[j][0]
    point.description = supermarket_result[j][0]
    point.coords = [(supermarket_result[j][2]['lng'],supermarket_result[j][2]['lat'])]
    point.style.iconstyle.icon.href = icon_style[0] 
kml.save(district + "_supermarket" + ".kml")
        
zf = zipfile.ZipFile(district + "_supermarket" + ".kmz", "w")
zf.write("images/icon-10.png")
zf.write(district + "_supermarket" + ".kml")
zf.close()