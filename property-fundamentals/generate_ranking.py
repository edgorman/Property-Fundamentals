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


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
desirability_with_burglary_count = []
desirability_without_burglary_count = []
affordability_count = []
property_ranking_all = property_ranking[0]
desirability_with_burglary_ward_order = []
desirability_without_burglary_ward_order = []
affordability_ward_order = []
price_order = []
universal_credit_order = []
housing_benefit_order = []
burglary_order = []
flood_order = []
outstanding_order = []
good_order = []
require_improvement_order = []
poor_order = []
scaled_price = []
scaled_burglary = []
scaled_schools = []
scaled_flood = []
scaled_universal_credit = []
scaled_housing_benefit = []

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
    #scale price
    scaled_price_calculate = ((int(price_mean[0][h]) - int(min_price)) / (int(max_price) - int(min_price)))
    scaled_price.insert(h,scaled_price_calculate)
    #scale burglary
    scaled_burglary_calculate = 1-((float(burglary_percentage[h]) - float(min_burglary)) / (float(max_burglary) - float(min_burglary)))
    scaled_burglary.insert(h,scaled_burglary_calculate)
    #scale schools
    scaled_schools_calculate = ((int(school_count_overall[h]) - int(min_schools)) / (int(max_schools) - int(min_schools)))
    scaled_schools.insert(h,scaled_schools_calculate)    
    #scale flooding
    scaled_flood_calculate = 1-((float(flood_percentage[h]) - float(min_flood)) / (float(max_flood) - float(min_flood)))
    scaled_flood.insert(h,scaled_flood_calculate)    
    #scale universal_credit
    scaled_universal_credit_calculate = 1-((float(universal_credit_percentage[h]) - float(min_universal_credit)) / (float(max_universal_credit) - float(min_universal_credit)))
    scaled_universal_credit.insert(h,scaled_universal_credit_calculate)     
    #scale housing_benefit
    scaled_housing_benefit_calculate = 1-((float(housing_benefit_percentage[h]) - float(min_housing_benefit)) / (float(max_housing_benefit) - float(min_housing_benefit)))
    scaled_housing_benefit.insert(h,scaled_housing_benefit_calculate)     
    
print(scaled_price)
print(scaled_burglary)
print(scaled_schools)
print(scaled_flood)
print(scaled_universal_credit)
print(scaled_housing_benefit)

# Weight the scaled affordability results and normalise
for h in range(0,len(coordinates)):
    affordability_temp = float(scaled_price[h])
    affordability_count.insert(h,affordability_temp)
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
    "Mean Sold Price \n (All Property Types) (£)": price_order
}

#Arrange the affordability data
affordability_df = pd.DataFrame(affordability_data, index = affordability_ward_order)
affordability_df['Mean Sold Price \n (All Property Types) (£)'] = affordability_df['Mean Sold Price \n (All Property Types) (£)'].apply(lambda x : "{:,d}".format(x))
Labels=affordability_df.columns
affordability_table = ax.table(cellText=affordability_df.values, colLabels=Labels, loc='center', cellLoc='center')
affordability_table.auto_set_font_size(False)
affordability_table.set_fontsize(10)
affordability_table.auto_set_column_width(col=list(range(len(affordability_df.columns))))

for r in range(0, len(Labels)):
    cell = affordability_table[0, r]
    cell.set_height(0.1)

#plot the price data
plt.rcParams["figure.dpi"] = 200
#plt.rcParams.update({'font.size': 12})
plt.rcParams["figure.figsize"] = (4.5,5)
plt.title(district +  " Price Ranking")
plt.savefig(district + "_ward_affordability" + ".png", bbox_inches='tight', transparent=True)

    
# Weight the scaled desirability results and normalise
for h in range(0,len(coordinates)):
    desirability_with_burglary_temp = ((float(scaled_burglary[h])*0.2) + (int(scaled_schools[h])*0.2) + (float(scaled_flood[h])*0.2) + (float(scaled_universal_credit[h])*0.2) + (float(scaled_housing_benefit[h])*0.2))
    desirability_with_burglary_count.insert(h,desirability_with_burglary_temp)
    desirability_without_burglary_temp = ((int(scaled_schools[h])*0.25) + (float(scaled_flood[h])*0.25) + (float(scaled_universal_credit[h])*0.25) + (float(scaled_housing_benefit[h])*0.25))
    desirability_without_burglary_count.insert(h,desirability_without_burglary_temp)
print(desirability_with_burglary_count)
print(desirability_without_burglary_count)
desirability_with_burglary_order = sorted(range(len(desirability_with_burglary_count)), key=lambda k: desirability_with_burglary_count[k], reverse=True)
desirability_without_burglary_order = sorted(range(len(desirability_without_burglary_count)), key=lambda k: desirability_without_burglary_count[k], reverse=True)
print(desirability_with_burglary_order)
print(desirability_without_burglary_order)


#Check if Burglary data is avaialble
burglary_data = input("Is there a full set of burglary data available (Y/N)?")

if burglary_data =='Y':
    
    #arrange the data
    for j in range(0,len(wards[0])):
        a = desirability_with_burglary_order[j]
        desirability_with_burglary_ward_order.insert(j,wards[0][a])
        universal_credit_order.insert(j,universal_credit_percentage[a])
        housing_benefit_order.insert(j,housing_benefit_percentage[a])
        burglary_order.insert(j,burglary_percentage[a])
        flood_order.insert(j,flood_percentage[a])
    
    outstanding_order = school_count_outstanding[desirability_with_burglary_order]
    good_order = school_count_good[desirability_with_burglary_order]
    require_improvement_order = school_count_requires_improvement[desirability_with_burglary_order]
    poor_order = school_count_poor[desirability_with_burglary_order]

    #Create the data
    desirability_data = {
      "Ward": desirability_with_burglary_ward_order,
      "(%) of Households \n on Universal Credit": universal_credit_order,
      "(%) of Households \n on Housing Benefit": housing_benefit_order,
      "(%) of Properties \n Burgled": burglary_order,
      "(%) of Ward area \n at Flooding Risk": flood_order,
      "No. Outstanding \n Schools": outstanding_order,
      "No. Good Schools": good_order,
      "No. Requires \n Improvement Schools": require_improvement_order,
      "No. Poor Schools": poor_order
    }
    
    desirability_count = desirability_with_burglary_count
    desirability_ward_order = desirability_with_burglary_order

elif burglary_data =='N':

    #arrange the data
    for j in range(0,len(wards[0])):
        a = desirability_without_burglary_order[j]
        desirability_without_burglary_ward_order.insert(j,wards[0][a])
        universal_credit_order.insert(j,universal_credit_percentage[a])
        housing_benefit_order.insert(j,housing_benefit_percentage[a])
        burglary_order.insert(j,burglary_percentage[a])
        flood_order.insert(j,flood_percentage[a])
        
    outstanding_order = school_count_outstanding[desirability_without_burglary_order]
    good_order = school_count_good[desirability_without_burglary_order]
    require_improvement_order = school_count_requires_improvement[desirability_without_burglary_order]
    poor_order = school_count_poor[desirability_without_burglary_order]   
    
    #Create the data
    desirability_data = {
      "Ward": desirability_without_burglary_ward_order,
      "(%) of Households \n on Universal Credit": universal_credit_order,
      "(%) of Households \n on Housing Benefit": housing_benefit_order,
      "(%) of Ward area \n at Flooding Risk": flood_order,
      "No. Outstanding \n Schools": outstanding_order,
      "No. Good Schools": good_order,
      "No. Requires \n Improvement Schools": require_improvement_order,
      "No. Poor Schools": poor_order
    }
    
    desirability_count = desirability_without_burglary_count
    desirability_ward_order = desirability_without_burglary_order
    
else:
    print("input error")    

#Arrange the data
desirability_df = pd.DataFrame(desirability_data, index = desirability_ward_order)
desirability_df = desirability_df.round({'(%) of Households \n on Universal Credit': 1})
desirability_df = desirability_df.round({'(%) of Households \n on Housing Benefit': 1})
desirability_df = desirability_df.round({'(%) of Properties \n Burgled': 2})
desirability_df = desirability_df.round({'(%) of Ward area \n at Flooding Risk': 1})
Labels=desirability_df.columns
desirability_table = ax.table(cellText=desirability_df.values, colLabels=Labels, loc='center', cellLoc='center')
desirability_table.auto_set_font_size(False)
desirability_table.set_fontsize(10)
desirability_table.auto_set_column_width(col=list(range(len(desirability_df.columns))))

for r in range(0, len(Labels)):
    cell = desirability_table[0, r]
    cell.set_height(0.1)

#plot the data
plt.rcParams["figure.dpi"] = 200
plt.rcParams["figure.figsize"] = (4.5,5)
plt.title(district +  ": Desirability Ranking", loc="center",
)
plt.savefig(district + "_ward_desirability" + ".png", bbox_inches='tight', transparent=True)
plt.close()
    
#plot the scatter
text_labels = wards[0]
unique_markers = ["d", "v", "s", "*", "^", "d", "v", "s", "*", "^"]
unique_colours = ['r','b','g','k','c','m','y']
col = []
markers = []
r=0
q=0

for s in range(0, len(wards[0])):
    print(r)
    print(q)
    col.insert(s,unique_colours[r])
    markers.insert(s,unique_markers[q])
    r+=1
    if r==7:
        r=0
        q+=1

print(col)
print(markers)
#scatter = plt.scatter(desirability_count,price_mean[0], s=20, c=colormap[color_categories], marker='o')


for xp, yp, m, c in zip(desirability_count, price_mean[0], markers, col):
   plt.scatter(xp, yp, marker=m, s=20, c=c)

# for h, wards[0] in enumerate(wards[0]):
    # plt.annotate(wards[0], (desirability_count[h],price_mean[0][h]), fontsize = 6, color = 'black', xytext=(desirability_count[h]+0.03,price_mean[0][h]+0.03))
plt.rcParams["figure.figsize"] = (5.5,5)
plt.title(district + ": Property Price vs. Relative Desirability", fontsize=10)
plt.ylabel("Mean Sold Price for All Property Types (£)", fontsize=7)
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.xlabel(str("{:.2f}".format(min(desirability_count))) + " = Undesirable         Relative Desirability           Desirable = 1" , fontsize=7)
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.legend( labels = text_labels,
            title='Wards',
            title_fontsize=7,
            loc="upper right",
            bbox_to_anchor=(1.5,1),
            framealpha=0,
            ncol = 1,
            fontsize=6)


plt.savefig(district + "_scatter" + ".png", bbox_inches='tight', transparent=True)
plt.close()

    






