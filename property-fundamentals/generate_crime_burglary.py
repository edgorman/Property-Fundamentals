from police_api.api import API as POLICE_API
from development_district import district
from development_district import max_lat
from development_district import min_lat
from development_district import max_lng
from development_district import min_lng
from development_district import centre_lat
from development_district import centre_lng
from development_district import distance

police_api = POLICE_API()
import simplekml
import zipfile
kml = simplekml.Kml()

point = []
icon_style = ['images/icon-14.png']

results = police_api.get_street_level_crimes(centre_lat, centre_lng, distance)

for crime in results:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        if crime['category'] == 'burglary':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[0]
        
kml.save(district + "_crime_burglary" + ".kml")
        
zf = zipfile.ZipFile(district + "_crime_burglary" + ".kmz", "w")
zf.write("images/icon-14.png")
zf.write(district + "_crime_burglary" + ".kml")
zf.close()