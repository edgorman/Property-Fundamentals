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

flood_api = FLOOD_API()
import simplekml
kml = simplekml.Kml()

point = []
flood_area_count = [0]*len(wards[0])
pol = []
count=0

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
                    p = p.buffer(0.02)
                q = Polygon(flood_data_result[j][k][l])
                if (q.is_valid == False):
                    q = q.buffer(0.02)
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
                    p = p.buffer(0.02)
                q = Polygon(flood_data_result[j][k])
                if (q.is_valid == False):
                    q = q.buffer(0.02)
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
        c = 0
    else:
        c = (float(a)/float(b))*100
    print(c)
    
        
#Save the polygons to a KML file
kml.save(district + "_flood_data" + ".kml")
