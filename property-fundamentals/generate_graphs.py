import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')


y = np.array([20, 20, 20, 20, 20])
mylabels = ["Burglary", "Flooding", "Universal Credit", "Housing benefit", "Schools"]
myexplode = [0, 0, 0, 0, 0]
mycolors = ["#FF0014", "#1478F0", "#F07800", "#B478FF", "#006400"]
textprops = {"fontsize":7}

plt.pie(y, labels = mylabels, explode = myexplode, shadow = False, colors = mycolors, textprops =textprops, autopct = "%0.2d%%")

#plot the data
plt.rcParams["figure.dpi"] = 200
plt.rcParams["figure.figsize"] = (4.5,5)
plt.title("Desirability Weighting with Burglary data", loc="center", fontsize=10)
plt.savefig("desirability_weighting_with_burglary" + ".png", bbox_inches='tight', transparent=True)
plt.close()
    

y2 = np.array([25, 25, 25, 25])
mylabels2 = ["Flooding", "Universal Credit", "Housing benefit", "Schools"]
myexplode2 = [0, 0, 0, 0]
mycolors2 = ["#1478F0", "#F07800", "#B478FF", "#006400"]
textprops2 = {"fontsize":7}

plt.pie(y2, labels = mylabels2, explode = myexplode2, shadow = False, colors = mycolors2, textprops =textprops2, autopct = "%0.2d%%")

#plot the data
plt.rcParams["figure.dpi"] = 200
plt.rcParams["figure.figsize"] = (4.5,5)
plt.title("Desirability Weighting without Burglary data", loc="center", fontsize=10)
plt.savefig("desirability_weighting_without_burglary" + ".png", bbox_inches='tight', transparent=True)
plt.close()


print(matplotlib.colors.hex2color("#FF0014"))
print(matplotlib.colors.hex2color("#1478F0"))
print(matplotlib.colors.hex2color("#F07800"))
print(matplotlib.colors.hex2color("#B478FF"))
print(matplotlib.colors.hex2color("#006400"))




