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
new_school_ward = []
new_school_ward_2 = []
icon_style = ['images/icon-1.png', 'images/icon-2.png', 'images/icon-3.png', 'images/icon-4.png']
ofsted_rating = ['Outstanding', 'Good', 'Requires improvement', 'Poor']
school_count_outstanding = np.array([0]*len(wards[0]))
school_count_good = np.array([0]*len(wards[0]))
school_count_requires_improvement = np.array([0]*len(wards[0]))
school_count_poor = np.array([0]*len(wards[0]))
school_count_overall = np.array([0]*len(wards[0]))
yaxis = []
xaxis = []
pol = []
xaxis_outstanding = np.array([0]*len(wards[0]))
xaxis_good = np.array([0]*len(wards[0]))
xaxis_requires_improvement = np.array([0]*len(wards[0]))
xaxis_poor = np.array([0]*len(wards[0]))

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]
    pol[h].style.polystyle.color = '32F07814' #= '19F07814'
    
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
        
        #Check ward is present in list
        ward_found = False
        for j in range (0,len(wards[0])):
            if school_ward[0][6] == wards[0][j]:
                ward_found = True
            elif school_ward[0][6].find("&") != -1 and school_ward[0][6].find(".") != -1:
                new_school_ward = school_ward[0][6].replace("&", "and")
                new_school_ward_2 = new_school_ward.replace(".", "")
                print(new_school_ward_2)
                if new_school_ward_2 == wards[0][j]:
                    school_ward[0][6] = new_school_ward_2
                    ward_found = True
            elif school_ward[0][6].find("&") != -1:
                new_school_ward = school_ward[0][6].replace("&", "and")
                print(new_school_ward)
                if new_school_ward == wards[0][j]:
                    school_ward[0][6] = new_school_ward
                    ward_found = True
            elif school_ward[0][6].find(".") != -1:
                new_school_ward = school_ward[0][6].replace(".", "")
                print(new_school_ward)
                if new_school_ward == wards[0][j]:
                    school_ward[0][6] = new_school_ward
                    ward_found = True

        if ward_found == True:
            print("ward found")
        elif ward_found == False:
            print("ward not found.\n wards available are:\n")
            print(wards[0])
            print("postcode is: ")
            print(postcode)
            print("school ward is currently: ")
            print(school_ward[0][6])
            school_ward[0][6] = input("Please type a ward from the list and press enter:\n\n (If you don't choose a ward from the list it will not be included in the chart)")
        
        #Calculate the school ward rating count
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
for j in range(0,len(wards[0])):
    school_count_overall[j] = (((school_count_outstanding[j])*2) + ((school_count_good[j])*1) + ((school_count_requires_improvement[j])*-1) + ((school_count_poor[j])*-2))

yaxis_order = sorted(range(len(school_count_overall)), key=lambda k: school_count_overall[k])
yaxis_order.reverse()
yaxis.clear()

for j in range(0,len(wards[0])):
    a = yaxis_order[j]
    yaxis.insert(j,wards[0][a])
    
xaxis_outstanding = school_count_outstanding[yaxis_order]
xaxis_good = school_count_good[yaxis_order]
xaxis_requires_improvement = school_count_requires_improvement[yaxis_order]
xaxis_poor = school_count_poor[yaxis_order]

#plot the data
plt.rcParams["figure.figsize"] = (4.5,5) # if there are many wards
plt.rcParams["figure.dpi"] = 200
plt.rcParams.update({'font.size': 7})
p1 = plt.barh(y_pos, xaxis_poor, color = (0.7578125,0.09375,0.35546875), edgecolor='black', left=xaxis_requires_improvement+xaxis_good+xaxis_outstanding) #color = (R,G,B)
p2 = plt.barh(y_pos, xaxis_requires_improvement, color = (0.98046875,0.75,0.17578125), edgecolor='black', left=xaxis_good+xaxis_outstanding) #color = (R,G,B)
p3 = plt.barh(y_pos, xaxis_good, color = (0.484375,0.69921875,0.2578125), edgecolor='black', left=xaxis_outstanding) #color = (R,G,B)
p4 = plt.barh(y_pos, xaxis_outstanding, color = (0.03515625,0.44140625,0.21875), edgecolor='black') #color = (R,G,B)
plt.yticks(y_pos,yaxis)
plt.xlabel("Number of Schools")
plt.gca().invert_yaxis()
plt.title(district + " (" + ofsted_month + "-" + ofsted_year + ") \n Schools and Nurseries Ofsted Rating")
plt.legend([p4,p3,p2,p1],["Outstanding", "Good", "Requires Improvement", "Poor"], loc="lower center", bbox_to_anchor=(0.3,-0.2), framealpha=0, ncol = 4)
plt.savefig(district + "_ofsted_rating" + ".png", bbox_inches='tight', transparent=True)
plt.clf()


#Add code when there are many wards


# plt.rcParams["figure.figsize"] = (2,5) # if there are many wards
# plt.rcParams["figure.dpi"] = 200
# plt.rcParams.update({'font.size': 5})
# p1 = plt.barh(y_pos[0:34], school_count_poor[0:34], color = (0.7578125,0.09375,0.35546875), edgecolor='black', left=school_count_requires_improvement[0:34]+school_count_good[0:34]+school_count_outstanding[0:34]) #color = (R,G,B)
# p2 = plt.barh(y_pos[0:34], school_count_requires_improvement[0:34], color = (0.98046875,0.75,0.17578125), edgecolor='black', left=school_count_good[0:34]+school_count_outstanding[0:34]) #color = (R,G,B)
# p3 = plt.barh(y_pos[0:34], school_count_good[0:34], color = (0.484375,0.69921875,0.2578125), edgecolor='black', left=school_count_outstanding[0:34]) #color = (R,G,B)
# p4 = plt.barh(y_pos[0:34], school_count_outstanding[0:34], color = (0.03515625,0.44140625,0.21875), edgecolor='black') #color = (R,G,B)
# plt.yticks(y_pos[0:34],wards[0][0:34])
# plt.xlabel("Number of Schools")
# plt.gca().invert_yaxis()
# plt.title(district + " (" + ofsted_month + "-" + ofsted_year + ") \n Schools and Nurseries Ofsted Rating")
# plt.legend([p4,p3,p2,p1],["Outstanding", "Good", "Requires Improvement", "Poor"], loc="lower center", bbox_to_anchor=(0.2,-0.2), framealpha=0, ncol = 4)
# plt.savefig(district + "_ofsted_rating" + ".png", bbox_inches='tight', transparent=True)
# plt.clf()

# plt.rcParams["figure.figsize"] = (2,5) # if there are many wards
# plt.rcParams["figure.dpi"] = 200
# plt.rcParams.update({'font.size': 5})
# p1 = plt.barh(y_pos[35:69], school_count_poor[35:69], color = (0.7578125,0.09375,0.35546875), edgecolor='black', left=school_count_requires_improvement[35:69]+school_count_good[35:69]+school_count_outstanding[35:69]) #color = (R,G,B)
# p2 = plt.barh(y_pos[35:69], school_count_requires_improvement[35:69], color = (0.98046875,0.75,0.17578125), edgecolor='black', left=school_count_good[35:69]+school_count_outstanding[35:69]) #color = (R,G,B)
# p3 = plt.barh(y_pos[35:69], school_count_good[35:69], color = (0.484375,0.69921875,0.2578125), edgecolor='black', left=school_count_outstanding[35:69]) #color = (R,G,B)
# p4 = plt.barh(y_pos[35:69], school_count_outstanding[35:69], color = (0.03515625,0.44140625,0.21875), edgecolor='black') #color = (R,G,B)
# plt.yticks(y_pos[35:69],wards[0][35:69])
# plt.xlabel("Number of Schools")
# plt.gca().invert_yaxis()
# plt.title(district + " (" + ofsted_month + "-" + ofsted_year + ") \n Schools and Nurseries Ofsted Rating")
# plt.savefig(district + "_ofsted_rating" + "2.png", bbox_inches='tight', transparent=True)
# plt.clf()