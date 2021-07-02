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
icon_style = ['images/icon-12.png','images/icon-13.png','images/icon-14.png','images/icon-15.png','images/icon-16.png','images/icon-17.png','images/icon-18.png','images/icon-19.png','images/icon-20.png','images/icon-21.png','images/icon-22.png','images/icon-23.png']

results = police_api.get_street_level_crimes(centre_lat, centre_lng, distance)

for crime in results:
    if (float(crime['location']['latitude']) <= max_lat) and (float(crime['location']['latitude']) >= min_lat) and (float(crime['location']['longitude']) <= max_lng) and (float(crime['location']['longitude']) >= min_lng):
        if crime['category'] == 'anti-social-behaviour':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[0]
        if crime['category'] == 'bicycle-theft':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[1]
        if crime['category'] == 'burglary':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[2]
        if crime['category'] == 'criminal-damage-arson':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[3]
        if crime['category'] == 'drugs':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[4]
        if crime['category'] == 'other-theft':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[5]
        if crime['category'] == 'possession-of-weapons':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[6]
        if crime['category'] == 'public-order':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[7]
        if crime['category'] == 'robbery':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[5]
        if crime['category'] == 'shoplifting':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[8]
        if crime['category'] == 'theft-from-the-person':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[5]
        if crime['category'] == 'vehicle-crime':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[9]
        if crime['category'] == 'violent-crime':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[10]
        if crime['category'] == 'other-crime':
            point = kml.newpoint()
            point.name = crime['category']
            point.description = crime['month']
            point.coords = [(crime['location']['longitude'],crime['location']['latitude'])]
            point.style.iconstyle.icon.href = icon_style[11]
        
kml.save(district + "_crime" + ".kml")
        
zf = zipfile.ZipFile(district + "_crime" + ".kmz", "w")
zf.write("images/icon-12.png")
zf.write("images/icon-13.png")
zf.write("images/icon-14.png")
zf.write("images/icon-15.png")
zf.write("images/icon-16.png")
zf.write("images/icon-17.png")
zf.write("images/icon-18.png")
zf.write("images/icon-19.png")
zf.write("images/icon-20.png")
zf.write("images/icon-21.png")
zf.write("images/icon-22.png")
zf.write("images/icon-23.png")
zf.write(district + "_crime" + ".kml")
zf.close()