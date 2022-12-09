# from development_district import district
# from development_district import wards
# from development_district import coordinates

# use these for the weighting calculation
# from generate_flood_data import flood_ranking
# from generate_property_price import property_ranking
# from generate_households_universal_credit_percentage import universal_credit_ranking
# from generate_crime_burglary_percentage_heat_map import burglary_ranking
# from generate_housing_benefit_claimants_percentage import housing_benefit_ranking
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

df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

ax.table(cellText=df.values, colLabels=df.columns, loc='center')

fig.tight_layout()

plt.show()


#ranking_count = [0]*len(wards[0])

#table related code
# table = [['First Name', 'Last Name', 'Age'], 
         # ['John', 'Smith', 39], 
         # ['Mary', 'Jane', 25], 
         # ['Jennifer', 'Doe', 28]]
         
# print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

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



