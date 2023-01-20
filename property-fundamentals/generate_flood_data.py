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
from environment_data_api.api import API as FLOOD_API
from shapely.geometry import Polygon
import numpy as np
import json
import matplotlib.pyplot as plt

flood_api = FLOOD_API()
import simplekml
kml = simplekml.Kml()

point = []
flood_percentage = []
flood_area_count = [0]*len(wards[0])
y_pos = np.arange(len(wards[0]))
pol = []
yaxis = []
xaxis = []
count=0
colouraxis = ['#1478F0FF']*len(wards[0])

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    print(coordinates[h])
    pol[h].outerboundaryis.coords = coordinates[h]
    pol[h].style.polystyle.color = '32F07814' #= '19F07814'

flood_data_result = flood_api.get_flood_data(
    centre_lat,
    centre_lng,
    1
    #int(distance/1000)
)

m = coordinates[0]
print(m)
t = Polygon(m)
print(t)
p = Polygon([(1,1),(2,2),(4,2),(3,1)])
print(p)
q = Polygon([(1.5,2),(3,5),(5,4),(3.5,1)])
print(q)
print(p.intersects(q))  # True
print(p.intersection(q).area)  # 1.0
x = p.intersection(q)
print(x)


for j in range (0,len(flood_data_result)):
    print (len(flood_data_result[j]))
    print (flood_data_result[j])
    for k in range (0,len(flood_data_result[j])):
        if str(flood_data_result[j])[0:4] == "[[[[":
        #if len(flood_data_result[j]) != 1:
            for l in range (0,len(flood_data_result[j][k])):
                pol.insert(count,kml.newpolygon())
                pol[count].style.linestyle.width = "0"
                pol[count].outerboundaryis.coords = flood_data_result[j][k][l]
                pol[count].style.polystyle.color = 'FFF07814'
            count +=1
            #find area of flooding which is overlapping with the wards
            for h in range(0,len(coordinates)):
                p = Polygon(coordinates[h])
                if (p.is_valid == False):
                    p = p.buffer(0.001)    # edit the value in the buffer to refine the results. Look at flooding graph, and refine
                q = Polygon(flood_data_result[j][k][l])
                if (q.is_valid == False):
                    q = q.buffer(0.001)    # edit the value in the buffer to refine the results. Look at flooding graph, and refine
                print(p.is_valid)
                print(q.is_valid)
                print(p.intersects(q))
                print(p.intersection(q).area)
                flood_area_count[h] += p.intersection(q).area
                
            
        elif str(flood_data_result[j])[0:4] != "[[[[":
        #elif len(flood_data_result[j]) == 1:
            pol.insert(count,kml.newpolygon())
            pol[count].style.linestyle.width = "0"
            pol[count].outerboundaryis.coords = flood_data_result[j][k]
            pol[count].style.polystyle.color = 'FFF07814'
            count +=1
            
            #find area of flooding which is overlapping with the wards
            for h in range(0,len(coordinates)):
                p = Polygon(coordinates[h])
                if (p.is_valid == False):
                    p = p.buffer(0.001)    # edit the value in the buffer to refine the results. Look at flooding graph, and refine
                q = Polygon(flood_data_result[j][k])
                if (q.is_valid == False):
                    q = q.buffer(0.001)    # edit the value in the buffer to refine the results. Look at flooding graph, and refine
                print(p.is_valid)
                print(q.is_valid)
                print(p.intersects(q))
                print(p.intersection(q).area)
                flood_area_count[h] += p.intersection(q).area
            
        else:
            print("error")

#Calculate the approx percentage of the ward which is flooding to inform the ranking
for h in range(0,len(coordinates)):
    a = (flood_area_count[h])
    b = Polygon(coordinates[h]).area
    if (a == 0):
        flood_percentage.insert(h,0)
    else:
        flood_percentage_calculate = ((float(a)/float(b))*100)
        flood_percentage.insert(h,flood_percentage_calculate)
    print(flood_percentage)
    
        
#Save the polygons to a KML file
kml.save(district + "_flood_data" + ".kml")

#Arrange the data for the plot
yaxis_order = sorted(range(len(flood_percentage)), key=lambda k: flood_percentage[k])
print(yaxis_order)
yaxis.clear()
xaxis.clear()
#colouraxis.clear()
for j in range(0,len(wards[0])):
    a = yaxis_order[j]
    yaxis.insert(j,wards[0][a])
    xaxis.insert(j,flood_percentage[a])
    #colouraxis.insert(j,price_plot[a])
print(yaxis)
print(xaxis)

#plot the data
plt.rcParams["figure.figsize"] = (4.5,5) # if there are many wards
plt.rcParams["figure.dpi"] = 200
plt.rcParams.update({'font.size': 7})
plt.barh(y_pos, xaxis, color= colouraxis, edgecolor='black')
plt.yticks(y_pos,yaxis)
plt.xlabel("Percentage (%)")
plt.title(district +  " - % of a Ward at Flooding Risk")
plt.savefig(district + "_Flooding_risk_percentage" + ".png", bbox_inches='tight', transparent=True)
plt.clf()