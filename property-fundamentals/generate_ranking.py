from development_district import district
from development_district import wards
from development_district import coordinates
from generate_households_universal_credit_percentage import universal_credit_percentage
from generate_housing_benefit_claimants_percentage import housing_benefit_percentage
from generate_crime_burglary_percentage_heat_map import burglary_percentage
from generate_flood_data import flood_percentage
from generate_property_price import price_mean

# use these for the weighting calculation
# from generate_early_education import school_ranking

# use these in the chart
# from generate_flood_data import flood_percentage
# from generate_property_price import property_price
# from generate_households_universal_credit_percentage import universal_credit_percentage
# from generate_crime_burglary_percentage_heat_map import burglary_percentage
# from generate_housing_benefit_claimants_percentage import housing_benefit_percentage
# from generate_early_education import school_score

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

data = {
  "Mean Sold Price \n (All Property Types) (£)": price_mean[0],
  "(%) of Households \n on Universal Credit": universal_credit_percentage,
  "(%) of Households \n on Housing Benefit": housing_benefit_percentage,
  "(%) of Properties \n Burgled": burglary_percentage,
  "(%) of Wards at \n Flooding Risk": flood_percentage,
  "Schools and Nurseries \n Ofsted Rating": [420, 380, 390,420, 380, 390,420, 380, 390,420, 380, 390,420, 380, 390,420, 380, 390]
}

df = pd.DataFrame(data, index = wards[0])
#df.style.format(na_rep='Mean Sold Price \n (All Property Types) (£)', formatter=int, thousands=',')
#df = df.round(decimals = 1)
df = df.round({'(%) of Households \n on Universal Credit': 1})
df = df.round({'(%) of Households \n on Housing Benefit': 1})
df = df.round({'(%) of Properties \n Burgled': 2})
df = df.round({'(%) of Wards at \n Flooding Risk': 1})
#df.style.set_properties(**{'text-align': 'left'})
Labels=df.columns
the_table = ax.table(cellText=df.values, colLabels=Labels, rowLabels=df.index, loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
the_table.auto_set_column_width(col=list(range(len(df.columns))))

for r in range(0, len(Labels)):
    cell = the_table[0, r]
    cell.set_height(0.1)

#fig.tight_layout()


plt.rcParams["figure.dpi"] = 200
#plt.rcParams.update({'font.size': 7})
plt.rcParams["figure.figsize"] = (4.5,5)
plt.title(district +  " Ward Ranking")
plt.savefig(district + "_ward_rankings" + ".png", bbox_inches='tight', transparent=True)


#burglary_data = input("Is there a full set of burglary data available (Y/N)?")


# if burglary_data =='Y':
    # for h in range(0,len(coordinates)):
        # ranking_count.insert(h,(flood_ranking[h] * 0.1) + (property_ranking[h] * 0.5) + (universal_credit_ranking[h] * 0.1) + (burglary_ranking[h] * 0.1) + (housing_benefit_ranking[h] * 0.1)+ (school_ranking[h] * 0.1))
    
    #Use tabulate to plot the data
    #https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd
    
# elif burglary_data =='N':
    # for h in range(0,len(coordinates)):
        # ranking_count.insert(h,(flood_ranking[h] * 0.125) + (property_ranking[h] * 0.5) + (universal_credit_ranking[h] * 0.125) + (housing_benefit_ranking[h] * 0.125)+ (school_ranking[h] * 0.125))
    
    #Use tabulate to plot the data
    #https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd
    
# else
    # print("input error")



