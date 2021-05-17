from govuk_ws.ofns.medianprice import MedianPrice
from generate_development_area import wards
from generate_development_area import area
median_price = MedianPrice()

#Define lists
house_types = []
price_median = []
price_median_raw = []

#Get house types
house_types.append(median_price.get_house_types())

#Get median price for house types
for h in range (0,len(house_types[0])):
    price_median_raw.append([])
    price_median.append([])
    for i in range (0,len(wards[0])):
        price_median_raw[h].insert(i,median_price.get_ward_data(area, wards[0][i], house_types[0][h]))
        if (price_median_raw[h][i] == None):
            price_median[h].insert(i,0)
        else:
            price_median[h].insert(i,(int(float(price_median_raw[h][i]))))





   
