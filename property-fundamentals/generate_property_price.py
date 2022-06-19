import simplekml
import matplotlib.pyplot as plt
import numpy as np
from development_district import wards
from development_district import coordinates
from development_district import district
from missing_data import price_mean
from property_price import house_types
from govuk_ws.ofns.meanprice import MeanPrice
mean_price = MeanPrice()

#Define variables / lists
kml = simplekml.Kml()
#colour = ['19F07814', '1EF07814', '23F07814', '28F07814', '2DF07814', '32F07814', '37F07814', '3CF07814', '41F07814', '46F07814', '4BF07814', '50F07814', '55F07814' ,'5AF07814', '5FF07814', '64F07814', '69F07814', '6EF07814', '73F07814', '78F07814', '7DF07814', '82F07814', '87F07814', '8CF07814', '91F07814', '96F07814', '9BF07814', 'A0F07814', 'A5F07814', 'AAF07814']
colour = ['2DF07814', '32F07814', '37F07814', '3CF07814', '41F07814', '46F07814', '4BF07814', '50F07814', '55F07814' ,'5AF07814', '5FF07814', '64F07814', '69F07814', '6EF07814', '73F07814', '78F07814', '7DF07814', '82F07814', '87F07814', '8CF07814', '91F07814', '96F07814', '9BF07814', 'A0F07814', 'A5F07814', 'AAF07814', 'AFF07814', 'B4F07814', 'B9F07814', 'BEF07814']
#colour_plot = ['#1478F019', '#1478F01E', '#1478F023', '#1478F028', '#1478F02D', '#1478F032', '#1478F037', '#1478F03C', '#1478F041', '#1478F046', '#1478F04B', '#1478F050', '#1478F055' ,'#1478F05A', '#1478F05F', '#1478F064', '#1478F069', '#1478F06E', '#1478F073', '#1478F078', '#1478F07D', '#1478F082', '#1478F087', '#1478F08C', '#1478F091', '#1478F096', '#1478F09B', '#1478F0A0', '#1478F0A5', '#1478F0AA']
colour_plot = ['#1478F02D', '#1478F032', '#1478F037', '#1478F03C', '#1478F041', '#1478F046', '#1478F04B', '#1478F050', '#1478F055' ,'#1478F05A', '#1478F05F', '#1478F064', '#1478F069', '#1478F06E', '#1478F073', '#1478F078', '#1478F07D', '#1478F082', '#1478F087', '#1478F08C', '#1478F091', '#1478F096', '#1478F09B', '#1478F0A0', '#1478F0A5', '#1478F0AA', '#1478F0AF', '#1478F0B4', '#1478F0B9', '#1478F0BE']


pol = []
colour_scale = []
price_scale = []
price_plot = []
y_pos = np.arange(len(wards[0]))
yaxis = []
xaxis = []
colouraxis = []

#Get date for plot title
year = mean_price._update_dataset()[-2:]
month = mean_price._update_dataset()[10:-4]
month_cap = month.capitalize()[0:3]

#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]

#Create the Mean price KML files    
for n in range (0,len(house_types[0])):
    
    #Generate price scaling information
    max_price = max(price_mean[n])
    min_price = min(price_mean[n])
    delta = max_price - min_price
    step = delta / (len(colour)-1)

    #Normalise the colours in the price range
    for i in range(0,len(colour)):
        colour_scale.insert(i,int(min_price + (i*step)))

    #Assign a colour to the normalised house prices
    for j in range(0,len(coordinates)):
        price_scale.append([])
        for k in range(0,len(colour_scale)):
            if (colour_scale[k] >= price_mean[n][j]):
                price_scale[n].insert(j,colour[k])
                price_plot.insert(j,colour_plot[k])
                break
        #Add price and colour to the polygons
        pol[j].description = "£" + str(price_mean[n][j])
        pol[j].style.polystyle.color = price_scale[n][j]
       
    #Save the polygons to a KML file
    kml.save(district + "_mean_" + house_types[0][n] + ".kml")
    
    #Arrange the data for the plot
    yaxis_order = sorted(range(len(price_mean[n])), key=lambda k: price_mean[n][k])
    print(yaxis_order)
    yaxis.clear()
    xaxis.clear()
    colouraxis.clear()
    for j in range(0,len(wards[0])):
        a = yaxis_order[j]
        yaxis.insert(j,wards[0][a])
        xaxis.insert(j,round(price_mean[n][a],-3))
        colouraxis.insert(j,price_plot[a])
    
    #plot the data
    #plt.rcParams["figure.figsize"] = (4.5,5.5) # if there are many wards
    plt.rcParams["figure.figsize"] = (5.5,5)
    plt.rcParams["figure.dpi"] = 200
    plt.rcParams.update({'font.size': 7})
    #plt.rc('ytick', labelsize=4)
    plt.locator_params(axis='x', nbins=4)
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
    hbars = plt.barh(y_pos, xaxis, color= colouraxis, edgecolor='black')
    plt.gca().set_xlim(left=0)#xaxis[0]-(2*xaxis[0]))
    plt.yticks(y_pos,yaxis)
    plt.xlabel("(£)")
    #plt.annotate('(Prices \n displayed \n to the \n nearest \n £1,000 are \n estimated \n due to lack \n of data)', xy=(0.7, 0.05), xycoords='axes fraction')  
    plt.bar_label(hbars, label_type="center", fmt='%d', labels=[f'{x:,.0f}' for x in hbars.datavalues])
    #plt.title(district + " (" + month_cap + "-" + year + "20): Mean Sold Price (" + house_types[0][n].capitalize() + ")")
    plt.title(district + " (" + month_cap + "-" + "20" + year + ") \n Mean Sold Price (" + house_types[0][n].capitalize() + ")")
    plt.tight_layout()
    plt.savefig(district + "_mean_" + house_types[0][n] + ".png", bbox_inches='tight', transparent=True)
    plt.clf()
