from govuk_ws.ofsted.schoolratings import SchoolRatings
from doogal.api import API
import simplekml
#from generate_development_area import wards
#from generate_development_area import area
school_ratings = SchoolRatings()
doogal_api = API()
kml = simplekml.Kml()

#school_ratings.get_districts()
#school_ratings.get_schools_from_district(area)
#school_ratings.get_schools_with_coordinates_from_district(doogal_api, 'Gloucester')

#school_data = []
point = []
ofsted_colour = ['4CFF0000', '4C00FF00', '4C0000FF', '4CFF0000']
ofsted_rating = ['Outstanding', 'Good', 'Requires improvement', 'Poor']

#school_data = school_ratings.get_schools_with_coordinates_from_district(doogal_api, area)
school_data = school_ratings.get_schools_with_coordinates_from_district(doogal_api, 'Gloucester')
#print(school_data)

for name, postcode, rating, ward, school_coordinates in school_data:
    point = kml.newpoint()
    point.name = name
    point.description = ofsted_rating[int(rating)-1]
    point.coords = [school_coordinates]
    point.style.iconstyle.color = ofsted_colour[int(rating)-1]
    #point.style.color = ofsted_colour[int(rating)-1]
    print(ofsted_colour[int(rating)-1])
kml.save("Gloucester" + "_school_rating" + ".kml")

   
