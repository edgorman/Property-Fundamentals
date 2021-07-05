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

month1 = (today.month - 14) % 12
year1 = today.year + ((today.month - 14) // 12)
month2 = (today.month - 13) % 12
year2 = today.year + ((today.month - 13) // 12)
month3 = (today.month - 12) % 12
year3 = today.year + ((today.month - 12) // 12)
month4 = (today.month - 11) % 12
year4 = today.year + ((today.month - 11) // 12)
month5 = (today.month - 10) % 12
year5 = today.year + ((today.month - 10) // 12)
month6 = (today.month - 9) % 12
year6 = today.year + ((today.month - 9) // 12)
month7 = (today.month - 8) % 12
year7 = today.year + ((today.month - 8) // 12)
month8 = (today.month - 7) % 12
year8 = today.year + ((today.month - 7) // 12)
month9 = (today.month - 6) % 12
year9 = today.year + ((today.month - 6) // 12)
month10 = (today.month - 5) % 12
year10 = today.year + ((today.month - 5) // 12)
month11 = (today.month - 4) % 12
year11 = today.year + ((today.month - 4) // 12)
month12 = (today.month - 3) % 12
year12 = today.year + ((today.month - 3) // 12)

print(month1)
print(year1)

results = police_api.get_street_level_crimes(centre_lat, centre_lng, distance, (str(year1) + "-" + (f"{month1:02}")))  

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