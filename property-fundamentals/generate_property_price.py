from govuk_ws.ofns.meanprice import MeanPrice
#from govuk_ws.ofns.meanprice import MedianPrice
from generate_development_district import wards
from generate_development_district import district
mean_price = MeanPrice()
#median_price = MedianPrice()

#Define lists
house_types = []
price_mean = []
price_mean_raw = []
#price_median = []
#price_median_raw = []

#Get house types
house_types.append(mean_price.get_house_types())

#Get mean price for house types
for h in range (0,len(house_types[0])):
    price_mean_raw.append([])
    price_mean.append([])
    for i in range (0,len(wards[0])):
        price_mean_raw[h].insert(i,mean_price.get_ward_data(district, wards[0][i], house_types[0][h]))
        if (price_mean_raw[h][i] == None):
            price_mean[h].insert(i,0)
        else:
            price_mean[h].insert(i,(int(float(price_mean_raw[h][i]))))

#Get median price for house types
# for h in range (0,len(house_types[0])):
    # price_median_raw.append([])
    # price_median.append([])
    # for i in range (0,len(wards[0])):
        # price_median_raw[h].insert(i,median_price.get_ward_data(district, wards[0][i], house_types[0][h]))
        # if (price_median_raw[h][i] == None):
            # price_median[h].insert(i,0)
        # else:
            # price_median[h].insert(i,(int(float(price_median_raw[h][i]))))



   
