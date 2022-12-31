import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')


y = np.array([20, 20, 20, 20, 20])
mylabels = ["Burglary", "Flooding", "Universal Credit", "Housing benefit", "Schools"]
myexplode = [0, 0, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#1478F0", "red"]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, colors = mycolors)

#plot the data
plt.rcParams["figure.dpi"] = 200
plt.rcParams["figure.figsize"] = (4.5,5)
plt.title("Desirability Weighting", loc="center", fontsize=10)
plt.savefig("desirability_weighting" + ".png", bbox_inches='tight', transparent=True)
plt.close()
    





