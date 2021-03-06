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
icon_style = ['images/icon-11.png']

subway_station_result = google_api.nearby_search(
    centre_lat,
    centre_lng,
    distance,
    location_type='subway_station'
)

for j in range (0,len(subway_station_result)):
    point = kml.newpoint()
    point.name = subway_station_result[j][0]
    point.description = subway_station_result[j][0]
    point.coords = [(subway_station_result[j][2]['lng'],subway_station_result[j][2]['lat'])]
    point.style.iconstyle.icon.href = icon_style[0] 
kml.save(district + "_subway_station" + ".kml")
        
zf = zipfile.ZipFile(district + "_subway_station" + ".kmz", "w")
zf.write("images/icon-11.png")
zf.write(district + "_subway_station" + ".kml")
zf.close()