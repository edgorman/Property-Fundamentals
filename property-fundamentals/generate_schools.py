from govuk_ws.ofsted.schoolratings import SchoolRatings
from doogal.api import API
#from generate_development_area import wards
#from generate_development_area import area
school_ratings = SchoolRatings()
doogal_api = API()

#school_ratings.get_districts()
school_ratings.get_schools_from_district('Gloucester')
#school_ratings.get_schools_with_coordinates_from_district(doogal_api, 'Gloucester')

#school_data = []
point = []
ofsted_colour = ['4C14E7FF', '4C1497FF', '4C143EFF', '4C1400FF']
ofsted_rating = ['Outstanding', 'Good', 'Requires improvement' 'Poor']

school_data = school_ratings.get_schools_with_coordinates_from_district(doogal_api, 'Gloucester')
#(name,postcode,rating,ward,coordinates) = school_data
print(school_data)

# for name, postcode, rating, ward, coordinates in school_data:
    # point = kml.newpoint()
    # point.name = name
    # point.description = ofsted_rating[rating-1]
    # point.coords = coordinates
    # point.style.color = ofsted_colour[rating-1]
# kml.save("Gloucester" + "_school_rating_" + ".kml")

   
