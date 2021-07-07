from govuk_api.ofns.api import API as OFNS_API
from google_api.api import API as GOOGLE_API
from govuk_ws.ofsted.schoolratings import SchoolRatings
from doogal_api.api import API as DOOGAL_API
from development_district import district
#from development_district import coordinates
from development_district import centre_lat
from development_district import centre_lng
from development_district import distance
from development_district import max_lat
from development_district import min_lat
from development_district import max_lng
from development_district import min_lng
school_ratings = SchoolRatings()
doogal_api = DOOGAL_API()

ofns_api = OFNS_API()
google_api = GOOGLE_API(key_path="../property-fundamentals/google_api/key.txt")
import simplekml
import zipfile
kml = simplekml.Kml()

point = []
icon_style = ['images/icon-1.png', 'images/icon-2.png', 'images/icon-3.png', 'images/icon-4.png','images/icon-10.png']
ofsted_rating = ['Outstanding', 'Good', 'Requires improvement', 'Poor']

school_data = school_ratings.get_schools_with_coordinates_from_district(doogal_api, district)

further_education_result = google_api.nearby_search(
    centre_lat,
    centre_lng,
    distance,
    location_type='university'
)

for j in range (0,len(further_education_result)):
    point = kml.newpoint()
    point.name = further_education_result[j][0]
    point.description = further_education_result[j][0]
    point.coords = [(further_education_result[j][2]['lng'],further_education_result[j][2]['lat'])]
    point.style.iconstyle.icon.href = icon_style[4]
    
for name, postcode, rating, ward, school_coordinates in school_data:
    lng , lat = map(float, str(school_coordinates).strip('[]').split(','))
    if (lat <= max_lat) and (lat >= min_lat) and (lng <= max_lng) and (lng >= min_lng):
        point = kml.newpoint()
        point.name = name
        point.description = ofsted_rating[int(rating)-1]
        point.coords = [school_coordinates]
        point.style.iconstyle.icon.href = icon_style[int(rating)-1] 
    
kml.save(district + "_education" + ".kml")
        
zf = zipfile.ZipFile(district + "_education" + ".kmz", "w")
zf.write("images/icon-1.png")
zf.write("images/icon-2.png")
zf.write("images/icon-3.png")
zf.write("images/icon-4.png")
zf.write("images/icon-10.png")
zf.write(district + "_education" + ".kml")
zf.close()