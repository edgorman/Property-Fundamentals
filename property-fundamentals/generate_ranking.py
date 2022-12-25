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
ranking_count = []
property_ranking_all = property_ranking[0]
ward_order = []
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
scaled_flooding = []
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
max_flooding = max(flood_percentage)
min_flooding = min(flood_percentage)
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
print(max_flooding)
print(min_flooding)
print(max_universal_credit)
print(min_universal_credit)
print(max_housing_benefit)
print(min_housing_benefit)

#scale results
for h in range(0,len(coordinates)):
    #scale price
    scaled_price_calculate = ((int(price_mean[0][h]) - int(min_price)) / (int(max_price) - int(min_price)))
    scaled_price.insert(h,scaled_price_calculate)
    #scale burglary
    scaled_burglary_calculate = ((float(burglary_percentage[h]) - float(min_burglary)) / (float(max_burglary) - float(min_burglary)))
    scaled_burglary.insert(h,scaled_price_calculate)
    #scale schools
    
    
    #scale flooding
    
    
    #scale universal_credit
    
    
    #scale housing_benefit
    
    
    
#print(scaled_price)
print(scaled_burglary)
#print(scaled_schools)
#print(scaled_flooding)
#print(scaled_universal_credit)
#print(scaled_housing_benefit)    
    
#Check if Burglary data is avaialble
burglary_data = input("Is there a full set of burglary data available (Y/N)?")


if burglary_data =='Y':
    
    # Rank the wards
    for h in range(0,len(coordinates)):
        ranking_count_temp = ((int(flood_ranking.index(h)) + 1) * 0.05) + ((int(universal_credit_ranking.index(h)) + 1) * 0.15) + ((int(burglary_ranking.index(h)) + 1) * 0.05) + ((int(housing_benefit_ranking.index(h)) + 1) * 0.15)+ ((int(school_ranking.index(h)) + 1) * 0.1) + ((int(property_ranking_all.index(h)) + 1) * 0.5)
        ranking_count.insert(h,ranking_count_temp)
    print(ranking_count)
    ranking_order = sorted(range(len(ranking_count)), key=lambda k: ranking_count[k])
    print(ranking_order)

    # Change the order of the table data based on the ranking
    for j in range(0,len(wards[0])):
        a = ranking_order[j]
        ward_order.insert(j,wards[0][a])
        price_order.insert(j,price_mean[0][a])
        universal_credit_order.insert(j,universal_credit_percentage[a])
        housing_benefit_order.insert(j,housing_benefit_percentage[a])
        burglary_order.insert(j,burglary_percentage[a])
        flood_order.insert(j,flood_percentage[a])
       
    outstanding_order = school_count_outstanding[ranking_order]
    good_order = school_count_good[ranking_order]
    require_improvement_order = school_count_requires_improvement[ranking_order]
    poor_order = school_count_poor[ranking_order]
       
    #Create the data
    data = {
      "Ward": ward_order,
      "Mean Sold Price \n (All Property Types) (£)": price_order,
      "(%) of Households \n on Universal Credit": universal_credit_order,
      "(%) of Households \n on Housing Benefit": housing_benefit_order,
      "(%) of Properties \n Burgled": burglary_order,
      "(%) of Wards at \n Flooding Risk": flood_order,
      "No. Outstanding \n Schools": outstanding_order,
      "No. Good Schools": good_order,
      "No. Requires \n Improvement Schools": require_improvement_order,
      "No. Poor Schools": poor_order
    }

    #Arrange the data
    df = pd.DataFrame(data, index = ward_order)
    df['Mean Sold Price \n (All Property Types) (£)'] = df['Mean Sold Price \n (All Property Types) (£)'].apply(lambda x : "{:,d}".format(x))
    df = df.round({'(%) of Households \n on Universal Credit': 1})
    df = df.round({'(%) of Households \n on Housing Benefit': 1})
    df = df.round({'(%) of Properties \n Burgled': 2})
    df = df.round({'(%) of Wards at \n Flooding Risk': 1})
    Labels=df.columns
    the_table = ax.table(cellText=df.values, colLabels=Labels, loc='center', cellLoc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.auto_set_column_width(col=list(range(len(df.columns))))

    for r in range(0, len(Labels)):
        cell = the_table[0, r]
        cell.set_height(0.1)

    #fig.tight_layout()

    #plot the data
    plt.rcParams["figure.dpi"] = 200
    plt.rcParams.update({'font.size': 12})
    plt.rcParams["figure.figsize"] = (4.5,5)
    plt.title(district +  " Ward Ranking")
    plt.savefig(district + "_ward_rankings" + ".png", bbox_inches='tight', transparent=True)

    
elif burglary_data =='N':

    # Rank the wards
    for h in range(0,len(coordinates)):
        ranking_count_temp = ((int(flood_ranking.index(h)) + 1) * 0.05) + ((int(universal_credit_ranking.index(h)) + 1) * 0.15) + ((int(housing_benefit_ranking.index(h)) + 1) * 0.15)+ ((int(school_ranking.index(h)) + 1) * 0.15) + ((int(property_ranking_all.index(h)) + 1) * 0.5)
        ranking_count.insert(h,ranking_count_temp)
    print(ranking_count)
    ranking_order = sorted(range(len(ranking_count)), key=lambda k: ranking_count[k])
    print(ranking_order)

    # Change the order of the table data based on the ranking
    for j in range(0,len(wards[0])):
        a = ranking_order[j]
        ward_order.insert(j,wards[0][a])
        price_order.insert(j,price_mean[0][a])
        universal_credit_order.insert(j,universal_credit_percentage[a])
        housing_benefit_order.insert(j,housing_benefit_percentage[a])
        flood_order.insert(j,flood_percentage[a])
       
    outstanding_order = school_count_outstanding[ranking_order]
    good_order = school_count_good[ranking_order]
    require_improvement_order = school_count_requires_improvement[ranking_order]
    poor_order = school_count_poor[ranking_order]
       
    #Create the data
    data = {
      "Ward": ward_order,
      "Mean Sold Price \n (All Property Types) (£)": price_order,
      "(%) of Households \n on Universal Credit": universal_credit_order,
      "(%) of Households \n on Housing Benefit": housing_benefit_order,
      "(%) of Wards at \n Flooding Risk": flood_order,
      "No. Outstanding \n Schools": outstanding_order,
      "No. Good Schools": good_order,
      "No. Requires \n Improvement Schools": require_improvement_order,
      "No. Poor Schools": poor_order
    }

    #Arrange the data
    df = pd.DataFrame(data, index = ward_order)
    df['Mean Sold Price \n (All Property Types) (£)'] = df['Mean Sold Price \n (All Property Types) (£)'].apply(lambda x : "{:,d}".format(x))
    df = df.round({'(%) of Households \n on Universal Credit': 1})
    df = df.round({'(%) of Households \n on Housing Benefit': 1})
    df = df.round({'(%) of Wards at \n Flooding Risk': 1})
    Labels=df.columns
    the_table = ax.table(cellText=df.values, colLabels=Labels, loc='center', cellLoc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.auto_set_column_width(col=list(range(len(df.columns))))

    for r in range(0, len(Labels)):
        cell = the_table[0, r]
        cell.set_height(0.1)

    #fig.tight_layout()

    #plot the data
    plt.rcParams["figure.dpi"] = 200
    plt.rcParams.update({'font.size': 12})
    plt.rcParams["figure.figsize"] = (4.5,5)
    plt.title(district +  " Ward Ranking")
    plt.savefig(district + "_ward_rankings" + ".png", bbox_inches='tight', transparent=True)

    
else:
    print("input error")






