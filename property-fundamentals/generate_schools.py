from govuk_ws.ofsted.schoolratings import SchoolRatings
from doogal_api.api import API as DOOGAL_API
#from generate_development_area import wards
from generate_development_district import district
import simplekml
import zipfile
school_ratings = SchoolRatings()
doogal_api = DOOGAL_API()
kml = simplekml.Kml()

#school_ratings.get_districts()
#school_ratings.get_schools_from_district(district)
#school_ratings.get_schools_with_coordinates_from_district(doogal_api, 'Gloucester')

point = []
icon_style = ['images/icon-1.png', 'images/icon-2.png', 'images/icon-3.png', 'images/icon-4.png']
ofsted_rating = ['Outstanding', 'Good', 'Requires improvement', 'Poor']

school_data = school_ratings.get_schools_with_coordinates_from_district(doogal_api, district)

for name, postcode, rating, ward, school_coordinates in school_data:
    point = kml.newpoint()
    point.name = name
    point.description = ofsted_rating[int(rating)-1]
    point.coords = [school_coordinates]
    point.style.iconstyle.icon.href = icon_style[int(rating)-1] 
kml.save(district + "_school_rating" + ".kml")

zf = zipfile.ZipFile(district + "_school_rating" + ".kmz", "w")
zf.write("images/icon-1.png")
zf.write("images/icon-2.png")
zf.write("images/icon-3.png")
zf.write("images/icon-4.png")
zf.write(district + "_school_rating" + ".kml")
zf.close()

