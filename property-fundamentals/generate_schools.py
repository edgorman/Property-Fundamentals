from govuk_ws.ofsted.schoolratings import SchoolRatings
from doogal.api import API
import simplekml
#from generate_development_area import wards
from generate_development_area import area
school_ratings = SchoolRatings()
doogal_api = API()
kml = simplekml.Kml()

#school_ratings.get_districts()
#school_ratings.get_schools_from_district(area)
#school_ratings.get_schools_with_coordinates_from_district(doogal_api, 'Gloucester')

point = []
ofsted_colour = ['ff387109', 'ff00d6ff', 'ff25a8f9', 'ff1427a5']
ofsted_rating = ['Outstanding', 'Good', 'Requires improvement', 'Poor']

school_data = school_ratings.get_schools_with_coordinates_from_district(doogal_api, area)

for name, postcode, rating, ward, school_coordinates in school_data:
    point = kml.newpoint()
    point.name = name
    point.description = ofsted_rating[int(rating)-1]
    point.coords = [school_coordinates]
    point.style.iconstyle.color = ofsted_colour[int(rating)-1]
    point.style.iconstyle.icon.href = 'https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png'
    point.style.labelstyle.color = '00000000'  
kml.save("Gloucester" + "_school_rating" + ".kml")

   
