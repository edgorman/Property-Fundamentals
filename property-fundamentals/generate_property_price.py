import simplekml
import matplotlib.pyplot as plt
import numpy as np
from development_district import wards
from development_district import coordinates
from development_district import district
from missing_data import price_mean
from property_price import house_types

#Define variables / lists
kml = simplekml.Kml()
colour = ['19F07814', '1EF07814', '23F07814', '28F07814', '2DF07814', '32F07814', '37F07814', '3CF07814', '41F07814', '46F07814', '4BF07814', '50F07814', '55F07814' ,'5AF07814', '5FF07814', '64F07814', '69F07814', '6EF07814', '73F07814', '78F07814', '7DF07814', '82F07814', '87F07814', '8CF07814', '91F07814', '96F07814', '9BF07814', 'A0F07814', 'A5F07814', 'AAF07814']
colour_plot = ['#1478F019', '#1478F01E', '#1478F023', '#1478F028', '#1478F02D', '#1478F032', '#1478F037', '#1478F03C', '#1478F041', '#1478F046', '#1478F04B', '#1478F050', '#1478F055' ,'#1478F05A', '#1478F05F', '#1478F064', '#1478F069', '#1478F06E', '#1478F073', '#1478F078', '#1478F07D', '#1478F082', '#1478F087', '#1478F08C', '#1478F091', '#1478F096', '#1478F09B', '#1478F0A0', '#1478F0A5', '#1478F0AA']

font = {'family' : 'Arial',
    'weight' : 'normal',
    'size'   : 12}
plt.rc('font', **font)

pol = []
colour_scale = []
price_scale = []
price_plot = []
y_pos = np.arange(len(wards[0]))
yaxis = []
xaxis = []
colouraxis = []

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
        xaxis.insert(j,price_mean[n][a])
        colouraxis.insert(j,price_plot[a])
    
    #plot the data
    plt.rcParams["figure.figsize"] = (4.5,5)
    plt.rcParams["figure.dpi"] = 200
    plt.barh(y_pos, xaxis, color= colouraxis, edgecolor='black')
    plt.yticks(y_pos,yaxis)
    plt.xlabel("(£)")
    plt.title(district + ": Mean Sold Price (" + house_types[0][n] + ")") #weight='bold'
    plt.tight_layout()
    plt.savefig(district + "_mean_" + house_types[0][n] + ".png", bbox_inches='tight', transparent=True)
    #plt.savefig(district + "_mean_" + house_types[0][n] + ".png", transparent=True)
    plt.clf()
