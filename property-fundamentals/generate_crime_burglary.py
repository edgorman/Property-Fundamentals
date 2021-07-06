from police_api.api import API as POLICE_API
from development_district import district
from development_district import max_lat
from development_district import min_lat
from development_district import max_lng
from development_district import min_lng
from development_district import centre_lat
from development_district import centre_lng
from development_district import distance
import datetime

police_api = POLICE_API()
import simplekml
import zipfile
kml = simplekml.Kml()
today = datetime.date.today()
point = []
icon_style = ['images/icon-14.png']

month1 = (today.month - 5) % 12
year1 = today.year + ((today.month - 5) // 12)
month2 = (today.month - 4) % 12
year2 = today.year + ((today.month - 4) // 12)
month3 = (today.month - 3) % 12
year3 = today.year + ((today.month - 3) // 12)

print((str(year1) + "-" + (f"{month1:02}")))
print((str(year2) + "-" + (f"{month2:02}")))
print((str(year3) + "-" + (f"{month3:02}")))

results1 = police_api.get_street_level_crimes(centre_lat, centre_lng, distance, (str(year1) + "-" + (f"{month1:02}")))
results2 = police_api.get_street_level_crimes(centre_lat, centre_lng, distance, (str(year2) + "-" + (f"{month2:02}")))
results3 = police_api.get_street_level_crimes(centre_lat, centre_lng, distance, (str(year3) + "-" + (f"{month3:02}")))

for crime in results1:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        if crime['category'] == 'burglary':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[0]
            
for crime in results2:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        if crime['category'] == 'burglary':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[0]

for crime in results3:
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