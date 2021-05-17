from govuk_ws.ofns.medianprice import MedianPrice
from generate_development_area import wards
from generate_development_area import area
median_price = MedianPrice()

house_types = []

price_median = []
# median_price_all = []
# median_price_detached = []
# median_price_semi_detached = []
# median_price_terraced = []
# median_price_flats = []

price_median_raw = []
# median_price_all_raw = []
# median_price_detached_raw = []
# median_price_semi_detached_raw = []
# median_price_terraced_raw = []
# median_price_flats_raw = []

house_types.append(median_price.get_house_types())
print(house_types)
print(house_types[0][0])
print(house_types[0][1])
print(house_types[0][2])
print(house_types[0][3])
print(house_types[0][4])

# Median price all
for h in range (0,4):
    price_median_raw.append([])
    price_median.append([])
    for i in range (0,len(wards[0])):
        price_median_raw[h].insert(i,median_price.get_ward_data(area, wards[0][i], house_types[0][h]))
        if (price_median_raw[h][i] == None):
            price_median[h].insert(i,0)
        else:
            price_median[h].insert(i,(int(float(price_median_raw[h][i]))))
print(price_median)
print(price_median_raw)

# # Median price detached
# for i in range (0,len(wards[0])):
    # median_price_detached_raw.append(median_price.get_ward_data(area, wards[0][i], house_types[0][1]))
    # if (median_price_detached_raw[i] == None):
        # median_price_detached.append(0)
    # else:
        # median_price_detached.append(int(float(median_price_detached_raw[i])))
# print(median_price_detached)
# print(median_price_detached_raw)

# # Median price semi-detached
# for i in range (0,len(wards[0])):
    # median_price_semi_detached_raw.append(median_price.get_ward_data(area, wards[0][i], house_types[0][2]))
    # if (median_price_semi_detached_raw[i] == None):
        # median_price_semi_detached.append(0)
    # else:
        # median_price_semi_detached.append(int(float(median_price_semi_detached_raw[i])))
# print(median_price_semi_detached)
# print(median_price_semi_detached_raw)

# # Median price terraced
# for i in range (0,len(wards[0])):
    # median_price_terraced_raw.append(median_price.get_ward_data(area, wards[0][i], house_types[0][3]))
    # if (median_price_terraced_raw[i] == None):
        # median_price_terraced.append(0)
    # else:
        # median_price_terraced.append(int(float(median_price_terraced_raw[i])))
# print(median_price_terraced)
# print(median_price_terraced_raw)

# # Median price flats
# for i in range (0,len(wards[0])):
    # median_price_flats_raw.append(median_price.get_ward_data(area, wards[0][i], house_types[0][4]))
    # if (median_price_flats_raw[i] == None):
        # median_price_flats.append(0)
    # else:
        # median_price_flats.append(int(float(median_price_flats_raw[i])))
# print(median_price_flats)
# print(median_price_flats_raw)

#median_price_all.append(int(float(median_price.get_ward_data(area, wards[0][i], "all"))))




   
