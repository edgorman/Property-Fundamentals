from govuk_api.ofns.api import API as OFNS_API
from google_api.api import API as GOOGLE_API
from govuk_ws.ofsted.schoolratings import SchoolRatings
from doogal_api.api import API as DOOGAL_API
from govuk_ws.geoportal.postcode_to_ward import PostcodeMapping
from development_district import district
from development_district import wards
from development_district import centre_lat
from development_district import centre_lng
from development_district import distance
from development_district import max_lat
from development_district import min_lat
from development_district import max_lng
from development_district import min_lng
import matplotlib.pyplot as plt
import numpy as np

school_ratings = SchoolRatings()
doogal_api = DOOGAL_API()
ofns_api = OFNS_API()
google_api = GOOGLE_API(key_path="../property-fundamentals/google_api/key.txt")
postcode_mapping = PostcodeMapping()
import simplekml
import zipfile
kml = simplekml.Kml()
y_pos = np.arange(len(wards[0]))

point = []
icon_style = ['images/icon-1.png', 'images/icon-2.png', 'images/icon-3.png', 'images/icon-4.png','images/icon-10.png']
ofsted_rating = ['Outstanding', 'Good', 'Requires improvement', 'Poor']
#school_count = [[0] * len(wards[0])] * 4
#school_count_outstanding = np.array([1,2,1,0,1,2,1,3,0,1,2,3,1,0,2,1])
#school_count_good = np.array([0,1,3,2,1,3,2,1,0,2,3,1,2,3,1,0])
#school_count_requires_improvement = np.array([1,2,3,2,1,2,1,1,0,0,0,1,1,1,1,0])
#school_count_poor = np.array([0,2,1,2,1,2,1,0,1,2,1,2,1,2,1,2])
school_count_outstanding = np.array([0]*len(wards[0]))
school_count_good = np.array([0]*len(wards[0]))
school_count_requires_improvement = np.array([0]*len(wards[0]))
school_count_poor = np.array([0]*len(wards[0]))

school_data = school_ratings.get_schools_with_coordinates_from_district(doogal_api, district)

further_education_result = google_api.nearby_search(
    centre_lat,
    centre_lng,
    distance,
    location_type='university'
)

for j in range (0,len(further_education_result)):
    if (further_education_result[j][2]['lat'] <= max_lat) and (further_education_result[j][2]['lat'] >= min_lat) and (further_education_result[j][2]['lng'] <= max_lng) and (further_education_result[j][2]['lng'] >= min_lng):
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
        school_ward = postcode_mapping.get_ward_from_postcode(postcode)
        print(school_ward)
    
kml.save(district + "_education" + ".kml")
        
zf = zipfile.ZipFile(district + "_education" + ".kmz", "w")
zf.write("images/icon-1.png")
zf.write("images/icon-2.png")
zf.write("images/icon-3.png")
zf.write("images/icon-4.png")
zf.write("images/icon-10.png")
zf.write(district + "_education" + ".kml")
zf.close()

#plot the data
p1 = plt.barh(y_pos, school_count_poor, color = 'red', edgecolor='black', left=school_count_requires_improvement+school_count_good+school_count_outstanding)
p2 = plt.barh(y_pos, school_count_requires_improvement, color = 'yellow', edgecolor='black', left=school_count_good+school_count_outstanding)
p3 = plt.barh(y_pos, school_count_good, color = 'springgreen', edgecolor='black', left=school_count_outstanding)
p4 = plt.barh(y_pos, school_count_outstanding, color = 'green', edgecolor='black')
plt.yticks(y_pos,wards[0])
plt.gca().invert_yaxis()
plt.xlabel("Number of Schools")
plt.title(district + " Primary and Secondary School Ofsted Rating")
plt.legend([p4,p3,p2,p1],["Outstanding", "Good", "Requires Improvement", "Poor"], loc="lower center", bbox_to_anchor=(0.5,-0.4))
plt.savefig(district + "_ofsted_rating" + ".png", bbox_inches='tight')#, transparent=True)
plt.clf()
