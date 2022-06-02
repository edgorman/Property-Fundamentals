from govuk_api.ofns.api import API as OFNS_API
from govuk_ws.ofsted.schoolratings import SchoolRatings
from doogal_api.api import API as DOOGAL_API
#from govuk_ws.geoportal.postcode_to_ward import PostcodeMapping
from postcodes_api.postcode_api import API as POSTCODE_API
from development_district import district
from development_district import wards
from development_district import coordinates
from development_district import centre_lat
from development_district import centre_lng
from development_district import distance
from development_district import max_lat
from development_district import min_lat
from development_district import max_lng
from development_district import min_lng
import matplotlib.pyplot as plt
import numpy as np
import json

school_ratings = SchoolRatings()
doogal_api = DOOGAL_API()
ofns_api = OFNS_API()
#postcode_mapping = PostcodeMapping()
postcodes_api = POSTCODE_API()
import simplekml
import zipfile
kml = simplekml.Kml()

y_pos = np.arange(len(wards[0]))
point = []
school_ward = []
icon_style = ['images/icon-1.png', 'images/icon-2.png', 'images/icon-3.png', 'images/icon-4.png']
ofsted_rating = ['Outstanding', 'Good', 'Requires improvement', 'Poor']
school_count_outstanding = np.array([0]*len(wards[0]))
school_count_good = np.array([0]*len(wards[0]))
school_count_requires_improvement = np.array([0]*len(wards[0]))
school_count_poor = np.array([0]*len(wards[0]))
yaxis = []
xaxis = []
pol = []
yaxis_school = []

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]
    pol[h].style.polystyle.color = '19F07814'
    
#xaxis_outstanding = np.array([0]*len(wards[0]))
#xaxis_good = np.array([0]*len(wards[0]))
#xaxis_requires_improvement = np.array([0]*len(wards[0]))
#xaxis_poor = np.array([0]*len(wards[0]))

school_data = school_ratings.get_schools_with_coordinates_from_district(doogal_api, district)


for name, postcode, rating, ward, school_coordinates, date in school_data:
    lng , lat = map(float, str(school_coordinates).strip('[]').split(','))
    if (lat <= max_lat) and (lat >= min_lat) and (lng <= max_lng) and (lng >= min_lng):
        ofsted_month = date[3:-3]
        ofsted_year = "20" + date[7:]
        #create the KML
        point = kml.newpoint()
        point.name = name
        point.description = ofsted_rating[int(rating)-1]
        point.coords = [school_coordinates]
        point.style.iconstyle.icon.href = icon_style[int(rating)-1] 
        #Create the plot
        school_ward.insert(0,doogal_api.get_postcode_info(postcode))
        if int(rating) == 1:
            for j in range (0,len(wards[0])):
                if school_ward[0][6] == wards[0][j]:
                    school_count_outstanding[j] +=1
        elif int(rating) == 2:
             for j in range (0,len(wards[0])):
                if school_ward[0][6] == wards[0][j]:
                    school_count_good[j] +=1                
        elif int(rating) == 3:
            for j in range (0,len(wards[0])):
                if school_ward[0][6] == wards[0][j]:
                    school_count_requires_improvement[j] +=1                    
        elif int(rating) == 4:
            for j in range (0,len(wards[0])):
                if school_ward[0][6] == wards[0][j]:
                    school_count_poor[j] +=1
                    
print(date)

#Save and zip the KML/KMZ  
kml.save(district + "_early_education" + ".kml")
zf = zipfile.ZipFile(district + "_early_education" + ".kmz", "w")
zf.write("images/icon-1.png")
zf.write("images/icon-2.png")
zf.write("images/icon-3.png")
zf.write("images/icon-4.png")
zf.write(district + "_early_education" + ".kml")
zf.close()


#Arrange the data for the plot
# yaxis_order = sorted(range(len(school_count_good)), key=lambda k: school_count_good[k])
# print(yaxis_order)
# yaxis.clear()
# for j in range(0,len(wards[0])):
    # a = yaxis_order[j]
    # yaxis.insert(j,wards[0][a])
# xaxis_outstanding = school_count_outstanding[yaxis_order]
# xaxis_good = school_count_good[yaxis_order]
# xaxis_requires_improvement = school_count_requires_improvement[yaxis_order]
# xaxis_poor = school_count_poor[yaxis_order]

print(ofsted_month)
print(ofsted_year)

#plot the school data
#for j in range(0,len(wards[0])):
    #yaxis_school.insert(j, (str(j+1) + ". " + wards[0][j]))

#plt.rcParams["figure.figsize"] = (4.5,5.5) # if there are many wards
plt.rcParams["figure.figsize"] = (4.5,5)
plt.rcParams["figure.dpi"] = 200
plt.rcParams.update({'font.size': 7})
p1 = plt.barh(y_pos, school_count_poor, color = (0.7578125,0.09375,0.35546875), edgecolor='black', left=school_count_requires_improvement+school_count_good+school_count_outstanding) #color = (R,G,B)
p2 = plt.barh(y_pos, school_count_requires_improvement, color = (0.98046875,0.75,0.17578125), edgecolor='black', left=school_count_good+school_count_outstanding) #color = (R,G,B)
p3 = plt.barh(y_pos, school_count_good, color = (0.484375,0.69921875,0.2578125), edgecolor='black', left=school_count_outstanding) #color = (R,G,B)
p4 = plt.barh(y_pos, school_count_outstanding, color = (0.03515625,0.44140625,0.21875), edgecolor='black') #color = (R,G,B)
plt.yticks(y_pos,wards[0])
plt.xlabel("Number of Schools")
plt.gca().invert_yaxis()
plt.title(district + " (" + ofsted_month + "-" + ofsted_year + ") \n Schools and Nurseries Ofsted Rating")
plt.legend([p4,p3,p2,p1],["Outstanding", "Good", "Requires Improvement", "Poor"], loc="lower center", bbox_to_anchor=(0.2,-0.2), framealpha=0, ncol = 4)
plt.savefig(district + "_ofsted_rating" + ".png", bbox_inches='tight', transparent=True)
plt.clf()
