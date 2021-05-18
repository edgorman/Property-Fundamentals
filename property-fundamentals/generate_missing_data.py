from generate_development_area import coordinates
from generate_property_price import price_mean
from generate_property_price import house_types

#Define variables / lists
wards_neighbour = []
wards_neighbour_count = []
average_price = []
    
#Estimate missing mean price data by taking the average of the neighbouring wards
for n in range (0,len(house_types[0])):
    wards_neighbour.clear() 
    wards_neighbour_count.clear()
    average_price.clear()
    for b in range (0,len(coordinates)):
        wards_neighbour.append([])
        c=0
        for a in range (0,len(coordinates)):
            wards_neighbour[b].insert(a,0)
            for j in range (0,len(coordinates[a])):
                for k in range (0,len(coordinates[b])):
                    if a == b:
                        break
                    elif coordinates[a][j] == coordinates[b][k]:
                        wards_neighbour[b].insert(a,price_mean[n][b])
                        if wards_neighbour[b][a] != 0:
                            c+=1
                        break
                else:
                    continue
                break
        wards_neighbour_count.insert(b,c)
        if wards_neighbour_count[b] !=0:
            average_price.insert(b,int(float((sum(wards_neighbour[b]))/wards_neighbour_count[b])))
        else:
            average_price.insert(b,int(float((sum(price_mean[n]))/len(coordinates))))
            
    for j in range(0,len(coordinates)):
        if (price_mean[n][j] == 0):
            price_mean[n][j] = average_price[j]





