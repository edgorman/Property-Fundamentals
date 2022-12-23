from development_district import district
from development_district import wards
from development_district import coordinates
from generate_households_universal_credit_percentage import universal_credit_percentage
from generate_housing_benefit_claimants_percentage import housing_benefit_percentage
from generate_crime_burglary_percentage_heat_map import burglary_percentage
from generate_flood_data import flood_percentage
from generate_property_price import price_mean

from generate_early_education import school_count_outstanding
from generate_early_education import school_count_good
from generate_early_education import school_count_requires_improvement
from generate_early_education import school_count_poor

# use these for the weighting calculation
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

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

# for h in range(0,len(coordinates)):
    # print(h)
    # print(wards[0][h], "flooding = ", (int(flood_ranking.index(h)) + 1), " ", flood_percentage[h])
    # print(wards[0][h], "price = ", (int(property_ranking_all.index(h)) + 1), " ", price_mean[0][h])
    # print(wards[0][h], "UC = ", (int(universal_credit_ranking.index(h)) + 1), " ", universal_credit_percentage[h])
    # print(wards[0][h], "burglary = ", (int(burglary_ranking.index(h)) + 1), " ", burglary_percentage[h])
    # print(wards[0][h], "HB = ", (int(housing_benefit_ranking.index(h)) + 1), " ", housing_benefit_percentage[h])
    # print(wards[0][h], "school = ", (int(outstanding_count.index(h)) + 1))
    # print(wards[0][h], "school = ", (int(good_count.index(h)) + 1))
    # print(wards[0][h], "school = ", (int(require_improvement_count.index(h)) + 1))
    # print(wards[0][h], "school = ", (int(poor_count.index(h)) + 1))
    # print(wards[0][h], "school = ", (int(school_ranking.index(h)) + 1))

# print("flooding = ", flood_ranking)
# print("price = ", property_ranking_all)
# print("UC = ", universal_credit_ranking)
# print("burglary = ", burglary_ranking)
# print("HB = ", housing_benefit_ranking)
# print("school = ", school_ranking)

# Rank the wards
for h in range(0,len(coordinates)):
    #ranking_count_temp = ((int(flood_ranking.index(h)) + 1) * 0.1) + ((int(universal_credit_ranking.index(h)) + 1) * 0.1) + ((int(burglary_ranking.index(h)) + 1) * 0.1) + ((int(housing_benefit_ranking.index(h)) + 1) * 0.1)+ ((int(school_ranking.index(h)) + 1) * 0.1) + ((int(property_ranking_all.index(h)) + 1) * 0.5)
    ranking_count_temp = ((int(flood_ranking.index(h)) + 1) * 0.1) + ((int(universal_credit_ranking.index(h)) + 1) * 0.1) + ((int(housing_benefit_ranking.index(h)) + 1) * 0.1)+ ((int(school_ranking.index(h)) + 1) * 0.1) + ((int(property_ranking_all.index(h)) + 1) * 0.1)
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
  "No. Oustanding \n Schools": outstanding_order,
  "No. Good Schools": good_order,
  "No. Requires \n Improvement Schools": require_improvement_order,
  "No. Poor Schools": poor_order
}


df = pd.DataFrame(data, index = ward_order)
#df.style.format(na_rep='Mean Sold Price \n (All Property Types) (£)', formatter=int, thousands=',')
#df = df.round(decimals = 1)
df = df.round({'(%) of Households \n on Universal Credit': 1})
df = df.round({'(%) of Households \n on Housing Benefit': 1})
df = df.round({'(%) of Properties \n Burgled': 2})
df = df.round({'(%) of Wards at \n Flooding Risk': 1})
#df.style.set_properties(**{'text-align': 'left'})
Labels=df.columns
the_table = ax.table(cellText=df.values, colLabels=Labels, loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
the_table.auto_set_column_width(col=list(range(len(df.columns))))

for r in range(0, len(Labels)):
    cell = the_table[0, r]
    cell.set_height(0.1)

#fig.tight_layout()


plt.rcParams["figure.dpi"] = 200
plt.rcParams.update({'font.size': 12})
plt.rcParams["figure.figsize"] = (4.5,5)
plt.title(district +  " Ward Ranking")
plt.savefig(district + "_ward_rankings" + ".png", bbox_inches='tight', transparent=True)



#burglary_data = input("Is there a full set of burglary data available (Y/N)?")


# if burglary_data =='Y':
    # for h in range(0,len(coordinates)):
        # ranking_count.insert(h,(flood_ranking[h] * 0.1) + (property_ranking[0][h] * 0.5) + (universal_credit_ranking[h] * 0.1) + (burglary_ranking[h] * 0.1) + (housing_benefit_ranking[h] * 0.1)+ (school_ranking[h] * 0.1))
    
    #Use tabulate to plot the data
    #https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd
    
# elif burglary_data =='N':
    # for h in range(0,len(coordinates)):
        # ranking_count.insert(h,(flood_ranking[h] * 0.125) + (property_ranking[0][h] * 0.5) + (universal_credit_ranking[h] * 0.125) + (housing_benefit_ranking[h] * 0.125)+ (school_ranking[h] * 0.125))
    
    #Use tabulate to plot the data
    #https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd
    
# else
    # print("input error")



