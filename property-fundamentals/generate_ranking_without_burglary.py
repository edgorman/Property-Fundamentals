from development_district import district
from development_district import wards
from development_district import coordinates
from generate_households_universal_credit_percentage import universal_credit_percentage
from generate_housing_benefit_claimants_percentage import housing_benefit_percentage
from generate_crime_burglary_percentage_heat_map import burglary_percentage
from generate_flood_data import flood_percentage
from generate_early_education import school_count_overall
from generate_property_price import price_mean
from generate_early_education import school_count_outstanding
from generate_early_education import school_count_good
from generate_early_education import school_count_requires_improvement
from generate_early_education import school_count_poor
from generate_flood_data import yaxis_order as flood_ranking
from generate_property_price import yaxis_order as property_ranking
from generate_households_universal_credit_percentage import yaxis_order as universal_credit_ranking
from generate_crime_burglary_percentage_heat_map import yaxis_order as burglary_ranking
from generate_housing_benefit_claimants_percentage import yaxis_order as housing_benefit_ranking
from generate_early_education import yaxis_order as school_ranking
import simplekml
import zipfile

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Define variables / lists
kml = simplekml.Kml()
colour = ['2D2E344E', '322E344E', '372E344E', '3C2E344E', '412E344E', '462E344E', '4B2E344E', '502E344E', '552E344E' ,'5A2E344E', '5F2E344E', '642E344E', '692E344E', '6E2E344E', '732E344E', '782E344E', '7D2E344E', '822E344E', '872E344E', '8C2E344E', '912E344E', '962E344E', '9B2E344E', 'A02E344E', 'A52E344E', 'AA2E344E', 'AF2E344E', 'B42E344E', 'B92E344E', 'BE2E344E']
colour_plot = ['#4E342E2D', '#4E342E32', '#4E342E37', '#4E342E3C', '#4E342E41', '#4E342E46', '#4E342E4B', '#4E342E50', '#4E342E55', '#4E342E5A', '#4E342E5F', '#4E342E64', '#4E342E69', '#4E342E6E', '#4E342E73', '#4E342E78', '#4E342E7D', '#4E342E82', '#4E342E87', '#4E342E8C', '#4E342E91', '#4E342E96', '#4E342E9B', '#4E342EA0', '#4E342EA5', '#4E342EAA', '#4E342EAF', '#4E342EB4', '#4E342EB9', '#4E342EBE']
pol = []
colour_scale = []
price_plot = []
desirability_count_percentage_scale = []

fig, ax = plt.subplots()
desirability_count = np.array([0]*len(wards[0]), dtype = float)
desirability_count_normalise = np.array([0]*len(wards[0]), dtype = float)
affordability_count = np.array([0]*len(wards[0]), dtype = float)
property_ranking_all = property_ranking[0]
desirability_ward_order = []
affordability_ward_order = []
price_order = []
desirability_count_table = []
universal_credit_order = []
housing_benefit_order = []
burglary_order = []
flood_order = []
outstanding_order = []
good_order = []
require_improvement_order = []
poor_order = []
scaled_price = np.array([0]*len(wards[0]), dtype = float)
scaled_burglary = np.array([0]*len(wards[0]), dtype = float)
scaled_schools = np.array([0]*len(wards[0]), dtype = float)
scaled_flood = np.array([0]*len(wards[0]), dtype = float)
scaled_universal_credit = np.array([0]*len(wards[0]), dtype = float)
scaled_housing_benefit = np.array([0]*len(wards[0]), dtype = float)

y_pos = np.arange(len(wards[0]))
barh_yaxis = []

scaled_burglary_hbar = np.array([0]*len(wards[0]), dtype = float)
scaled_schools_hbar = np.array([0]*len(wards[0]), dtype = float)
scaled_flood_hbar = np.array([0]*len(wards[0]), dtype = float)
scaled_universal_credit_hbar = np.array([0]*len(wards[0]), dtype = float)
scaled_housing_benefit_hbar = np.array([0]*len(wards[0]), dtype = float)

weighted_burglary_hbar = np.array([0]*len(wards[0]), dtype = float)
weighted_schools_hbar = np.array([0]*len(wards[0]), dtype = float)
weighted_flood_hbar = np.array([0]*len(wards[0]), dtype = float)
weighted_universal_credit_hbar = np.array([0]*len(wards[0]), dtype = float)
weighted_housing_benefit_hbar = np.array([0]*len(wards[0]), dtype = float)

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

max_price = max(price_mean[0])
min_price = min(price_mean[0])
max_burglary = max(burglary_percentage)
min_burglary = min(burglary_percentage)
max_schools = max(school_count_overall)
min_schools = min(school_count_overall)
max_flood = max(flood_percentage)
min_flood = min(flood_percentage)
max_universal_credit = max(universal_credit_percentage)
min_universal_credit = min(universal_credit_percentage)
max_housing_benefit = max(housing_benefit_percentage)
min_housing_benefit = min(housing_benefit_percentage)

print(max_price)
print(min_price)
print(max_burglary)
print(min_burglary)
print(max_schools)
print(min_schools)
print(max_flood)
print(min_flood)
print(max_universal_credit)
print(min_universal_credit)
print(max_housing_benefit)
print(min_housing_benefit)

#normalise results
for h in range(0,len(coordinates)):
    scaled_price[h] = ((int(price_mean[0][h]) - int(min_price)) / (int(max_price) - int(min_price)))
    scaled_burglary[h] = 1-((float(burglary_percentage[h]) - float(min_burglary)) / (float(max_burglary) - float(min_burglary)))
    scaled_schools[h] = ((int(school_count_overall[h]) - int(min_schools)) / (int(max_schools) - int(min_schools)))
    scaled_flood[h] = 1-((float(flood_percentage[h]) - float(min_flood)) / (float(max_flood) - float(min_flood)))
    scaled_universal_credit[h] = 1-((float(universal_credit_percentage[h]) - float(min_universal_credit)) / (float(max_universal_credit) - float(min_universal_credit)))
    scaled_housing_benefit[h] = 1-((float(housing_benefit_percentage[h]) - float(min_housing_benefit)) / (float(max_housing_benefit) - float(min_housing_benefit)))

print(scaled_price)
print(scaled_burglary)
print(scaled_schools)
print(scaled_flood)
print(scaled_universal_credit)
print(scaled_housing_benefit)

# Weight the scaled affordability results and normalise
for h in range(0,len(coordinates)):
    affordability_count[h] = float(scaled_price[h])
print(affordability_count)
affordability_order = sorted(range(len(affordability_count)), key=lambda k: affordability_count[k])
print(affordability_order)

# Change the order of the affordability table data based on the ranking
for j in range(0,len(wards[0])):
    b = affordability_order[j]
    affordability_ward_order.insert(j,wards[0][b])
    price_order.insert(j,price_mean[0][b])

    
#Create the affordability data
affordability_data = {
    "Ward": affordability_ward_order,
    "Mean Sold\nPrice (All Property\nTypes) (£)": price_order
}

#Arrange the affordability data
affordability_df = pd.DataFrame(affordability_data, index = affordability_ward_order)
affordability_df['Mean Sold\nPrice (All Property\nTypes) (£)'] = affordability_df['Mean Sold\nPrice (All Property\nTypes) (£)'].apply(lambda x : "{:,d}".format(x))
Labels=affordability_df.columns
affordability_table = ax.table(cellText=affordability_df.values, colLabels=Labels, loc='center', cellLoc='center')
affordability_table.auto_set_font_size(False)
affordability_table.set_fontsize(7)
affordability_table.auto_set_column_width(col=list(range(len(affordability_df.columns))))

for r in range(0, len(Labels)):
    cell = affordability_table[0, r]
    cell.set_height(0.15)

#plot the price data
#plt.rcParams["figure.dpi"] = 200
#plt.rcParams.update({'font.size': 12})
plt.rcParams["figure.figsize"] = (4.5,5)
plt.title(district +  " Price Ranking", fontsize=10)
plt.savefig(district + "_ward_affordability" + ".png", bbox_inches='tight', transparent=True)

    
# Weight the scaled desirability results and normalise
for h in range(0,len(coordinates)):
    desirability_count[h] = (float(scaled_schools[h]*0.325) + float(scaled_flood[h]*0.125) + float(scaled_universal_credit[h]*0.275) + float(scaled_housing_benefit[h]*0.275))
print(desirability_count)
desirability_order = sorted(range(len(desirability_count)), key=lambda k: desirability_count[k], reverse=True)
print(desirability_order)


# normalise the desirability results
min_desirability_count = min(desirability_count)
max_desirability_count = max(desirability_count)
print(desirability_count)
print(min_desirability_count)
print(max_desirability_count)
for h in range(0,len(coordinates)):
    desirability_count_normalise[h] = ((float(desirability_count[h]) - float(min_desirability_count)) / (float(max_desirability_count) - float(min_desirability_count)))
print(desirability_count_normalise)


scaled_schools_hbar = scaled_schools[desirability_order]
scaled_flood_hbar = scaled_flood[desirability_order]
scaled_universal_credit_hbar = scaled_universal_credit[desirability_order]
scaled_housing_benefit_hbar = scaled_housing_benefit[desirability_order]

#arrange the data
for j in range(0,len(wards[0])):
    a = desirability_order[j]
    desirability_count_table.insert(j,desirability_count_normalise[a])
    desirability_ward_order.insert(j,wards[0][a])
    universal_credit_order.insert(j,universal_credit_percentage[a])
    housing_benefit_order.insert(j,housing_benefit_percentage[a])
    flood_order.insert(j,flood_percentage[a])
    barh_yaxis.insert(j,wards[0][a])
    weighted_schools_hbar[j] = float(scaled_schools_hbar[j]*0.325)
    weighted_flood_hbar[j] = float(scaled_flood_hbar[j]*0.125)
    weighted_universal_credit_hbar[j] = float(scaled_universal_credit_hbar[j]*0.275)
    weighted_housing_benefit_hbar[j] = float(scaled_housing_benefit_hbar[j]*0.275)

outstanding_order = school_count_outstanding[desirability_order]
good_order = school_count_good[desirability_order]
require_improvement_order = school_count_requires_improvement[desirability_order]
poor_order = school_count_poor[desirability_order]

#Create the data
desirability_data = {
  "Ward": desirability_ward_order,
  # "weighted \n school": weighted_schools_hbar,
  # "weighted \n flood": weighted_flood_hbar,
  # "weighted \n uc": weighted_universal_credit_hbar,
  # "weighted \n hb": weighted_housing_benefit_hbar,
  # "Desirability \nScore": desirability_count_table,
  "(%) of\nHouseholds\non Universal\nCredit": universal_credit_order,
  "(%) of\nHouseholds\non Housing\nBenefit": housing_benefit_order,
  "(%) of\nWard\narea at\nFlooding\nRisk": flood_order,
  "No.\nOutstanding\nSchools": outstanding_order,
  "No.\nGood\nSchools": good_order,
  "No.\nRequires\nImprovement\nSchools": require_improvement_order,
  "No.\nPoor\nSchools": poor_order
}


#Arrange the data
desirability_df = pd.DataFrame(desirability_data, index = desirability_ward_order)
# desirability_df = desirability_df.round({'Desirability \nScore': 4})
desirability_df = desirability_df.round({'(%) of\nHouseholds\non Universal\nCredit': 1})
desirability_df = desirability_df.round({'(%) of\nHouseholds\non Housing\nBenefit': 1})
desirability_df = desirability_df.round({'(%) of\nWard\narea at\nFlooding\nRisk': 1})
# desirability_df = desirability_df.round({'weighted \n school': 3})
# desirability_df = desirability_df.round({'weighted \n flood': 3})
# desirability_df = desirability_df.round({'weighted \n uc': 3})
# desirability_df = desirability_df.round({'weighted \n hb': 3})
Labels=desirability_df.columns
desirability_table = ax.table(cellText=desirability_df.values, colLabels=Labels, loc='center', cellLoc='center')
desirability_table.auto_set_font_size(False)
desirability_table.set_fontsize(7)
desirability_table.auto_set_column_width(col=list(range(len(desirability_df.columns))))

for r in range(0, len(Labels)):
    cell = desirability_table[0, r]
    cell.set_height(0.15)

#plot the data
#plt.rcParams["figure.dpi"] = 200
plt.rcParams["figure.figsize"] = (4.5,5)
plt.title(district +  ": Desirability Ranking", loc="center", fontsize=10)
plt.savefig(district + "_ward_desirability" + ".png", bbox_inches='tight', transparent=True)
plt.close()



#plot the horizontal bar for desirability
plt.rcParams["figure.figsize"] = (4.5,5) # if there are many wards
plt.rcParams["figure.dpi"] = 200
#plt.rcParams.update({'font.size': 7})
p2 = plt.barh(y_pos, weighted_schools_hbar, color = (0,0.39215686,0), left=weighted_flood_hbar+weighted_universal_credit_hbar+weighted_housing_benefit_hbar) #color = (R,G,B)
p3 = plt.barh(y_pos, weighted_flood_hbar, color = (0.07843137,0.47058823,0.94117647), left=weighted_universal_credit_hbar+weighted_housing_benefit_hbar) #color = (R,G,B)
p4 = plt.barh(y_pos, weighted_universal_credit_hbar, color = (0.94117647,0.47058823,0), left=weighted_housing_benefit_hbar) #color = (R,G,B)
p5 = plt.barh(y_pos, weighted_housing_benefit_hbar, color = (0.70588235,0.47058823,1)) #color = (R,G,B)
  
plt.yticks(y_pos,barh_yaxis)
plt.xlabel( "0= Undesirable         Relative Desirability           Desirable = 1" , fontsize=7)
plt.gca().invert_yaxis()
plt.title(district + ": Desirability Ranking")
plt.legend([p5,p4,p3,p2],["Low Housing \nBenefit", "Low Universal \nCredit", "Low Flooding \nRisk", "Good \nSchools"], loc="lower center", bbox_to_anchor=(0.4,-0.2), framealpha=0, ncol = 4)

plt.savefig(district + "_desirability_bar_char" + ".png", bbox_inches='tight', transparent=True)
plt.clf()



#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]

#Generate scaling information
max_desirability_count_normalise = max(desirability_count_normalise)
min_desirability_count_normalise = min(desirability_count_normalise)
delta = max_desirability_count_normalise - min_desirability_count_normalise
step = delta / (len(colour)-1)

print(desirability_count_normalise)
print(desirability_count_normalise)
print(delta)
print(step)

#Normalise the colours in the universal credit range
for i in range(0,len(colour)):
    colour_scale.insert(i,(min_desirability_count_normalise + (i*step)))

#Assign a colour to the normalised universal credit
for j in range(0,len(coordinates)):
    desirability_count_percentage_scale.append([])
    for k in range(0,len(colour_scale)):
        if (colour_scale[k] >= (desirability_count_normalise[j])):
            desirability_count_percentage_scale.insert(j,colour[k])
            price_plot.insert(j,colour_plot[k])
            break
        elif (k == len(colour_scale)-1):
            desirability_count_percentage_scale.insert(j,colour[k])
            price_plot.insert(j,colour_plot[k])
            
    #Add universal credit and colour to the polygons
    #pol[j].description = statxplore_api.get_universal_credit_date('table', ward_codes[h]) + ": " + str(universal_credit_percentage[j])[0:4] + "% of Households on Universal Credit"
    pol[j].style.polystyle.color = desirability_count_percentage_scale[j]

#Save the polygons to a KML file
kml.save(district + "_desirability" + ".kml")

zf = zipfile.ZipFile(district + "_desirability" + ".kmz", "w")
zf.write(district + "_desirability" + ".kml")
zf.close()




















    
#plot the scatter
text_labels = wards[0]
unique_markers = ["d", "v", "s", "*", "^", "d", "v", "s", "*", "^"]
unique_colours = ['r','b','g','k','c','m','y']
col = []
markers = []
r=0
q=0

for s in range(0, len(wards[0])):
    col.insert(s,unique_colours[r])
    markers.insert(s,unique_markers[q])
    r+=1
    if r==7:
        r=0
        q+=1

print(col)
print(markers)
#scatter = plt.scatter(desirability_count_normalise,price_mean[0], s=20, c=colormap[color_categories], marker='o')


for xp, yp, m, c in zip(desirability_count_normalise, price_mean[0], markers, col):
   plt.scatter(xp, yp, marker=m, s=20, c=c)

# for h, wards[0] in enumerate(wards[0]):
    # plt.annotate(wards[0], (desirability_count_normalise[h],price_mean[0][h]), fontsize = 6, color = 'black', xytext=(desirability_count_normalise[h]+0.03,price_mean[0][h]+0.03))
plt.rcParams["figure.figsize"] = (5.5,5)
plt.title(district + ": Property Price vs. Location Desirability", fontsize=10)
plt.ylabel("Mean Sold Price for All Property Types (£)", fontsize=7)
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.xlabel( "0= Undesirable         Location Desirability           Desirable = 1" , fontsize=7) #str("{:.2f}".format(min(desirability_count_normalise)))
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

# handles, labels = plt.gca().get_legend_handles_labels()
# by_label = dict(zip(labels, handles))
# plt.legend(by_label.values(), by_label.keys())

plt.legend( labels = text_labels,
            title='Wards',
            title_fontsize=7,
            loc="upper right",
            bbox_to_anchor=(0.6,1),
            framealpha=0,
            ncol = 1,
            fontsize=6)


plt.savefig(district + "_scatter" + ".png", bbox_inches='tight', transparent=True)
plt.close()

    
#Generate / Draw polygons
for h in range(0,len(coordinates)):
    pol.insert(h,kml.newpolygon())
    pol[h].name = wards[0][h]
    pol[h].style.linestyle.width = "0"
    pol[h].outerboundaryis.coords = coordinates[h]
    pol[h].style.polystyle.color = '32F07814' #= '19F07814'
    
#Save and zip the KML/KMZ  
kml.save(district + "_scatter" + ".kml")

zf = zipfile.ZipFile(district + "_scatter" + ".kmz", "w")
zf.write(district + "_scatter" + ".kml")
zf.close()





