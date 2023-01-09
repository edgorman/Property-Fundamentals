import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

plt.rcParams["figure.figsize"] = (9,9)


y = np.array([10, 10, 25, 25, 30])
mylabels = ["Burglary", "Flooding", "Universal Credit", "Housing benefit", "Schools"]
mylabels_factor = ["Risk", "Risk", "Push", "Push", "Pull"]
myexplode = [0.2, 0.2, 0, 0.1, 0]
mycolors = ["#FF0014", "#1478F0", "#F07800", "#B478FF", "#006400"]
textprops = {"fontsize":16}

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, colors = mycolors, textprops =textprops, autopct = "%0.2f%%",startangle = 0)
plt.legend( labels = mylabels_factor,
            title='Desirability Factor',
            title_fontsize=16,
            loc="lower center",
            bbox_to_anchor=(0.4,-0.1),
            framealpha=0,
            ncol = 5,
            fontsize=16)

#plot the data
#plt.rcParams["figure.dpi"] = 200
#plt.rcParams["figure.figsize"] = (10,10)
plt.title("Desirability Weighting with Burglary data", loc="center", fontsize=18)
plt.savefig("desirability_weighting_with_burglary" + ".png", bbox_inches='tight', transparent=True)
plt.close()
    

y2 = np.array([12.5, 27.5, 27.5, 32.5])
mylabels2 = ["Flooding", "Universal Credit", "Housing benefit", "Schools"]
mylabels_factor2 = ["Risk", "Push", "Push", "Pull"]
myexplode2 = [0.2, 0, 0.1, 0]
mycolors2 = ["#1478F0", "#F07800", "#B478FF", "#006400"]
textprops2 = {"fontsize":16}

plt.pie(y2, labels = mylabels2, explode = myexplode2, shadow = True, colors = mycolors2, textprops =textprops2, autopct = "%0.2f%%", startangle = 0)
plt.legend( labels = mylabels_factor2,
            title='Desirability Factor',
            title_fontsize=16,
            loc="lower center",
            bbox_to_anchor=(0.4,-0.1),
            framealpha=0,
            ncol = 5,
            fontsize=16)

#plot the data
#plt.rcParams["figure.dpi"] = 200
#plt.rcParams["figure.figsize"] = (10,10)
plt.title("Desirability Weighting without Burglary data", loc="center", fontsize=18)
plt.savefig("desirability_weighting_without_burglary" + ".png", bbox_inches='tight', transparent=True)
plt.close()






y = np.array([10, 10, 25, 25, 30])
mylabels = ["Burglary", "Flooding", "Universal Credit", "Housing benefit", "Schools"]
mylabels_factor = ["Risk", "Risk", "Push", "Push", "Pull"]
myexplode = [0.2, 0.2, 0, 0.1, 0]
mycolors = ["#FF0014", "#1478F0", "#F07800", "#B478FF", "#006400"]
textprops = {"fontsize":16}

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, colors = mycolors, textprops =textprops, autopct = "%0.2f%%",startangle = 0)
plt.legend( labels = mylabels_factor,
            title='Desirability Factor',
            title_fontsize=16,
            loc="lower center",
            bbox_to_anchor=(0.4,-0.1),
            framealpha=0,
            ncol = 5,
            fontsize=16)

#plot the data
#plt.rcParams["figure.dpi"] = 200
#plt.rcParams["figure.figsize"] = (10,10)
plt.title("Desirability Weighting with Burglary data", loc="center", fontsize=18)
plt.savefig("desirability_weighting_with_burglary" + ".png", bbox_inches='tight', transparent=True)
plt.close()




#plot the scatter
plt.rcParams["figure.figsize"] = (3.5,3)
x = np.array([0.2,0.4,0.8])
y = np.array([350000,240000,180000])
colors = np.array(["red","green","blue"])
#text_labels = np.array(["Ward A","Ward B","Ward C"])

for xp, yp, c in zip(x, y, colors):
   plt.scatter(xp, yp, s=800, c=c)

#plt.rcParams["figure.figsize"] = (3.5,3)
plt.title("Average Property Price vs. Location Desirability", fontsize=20, y=1.12)
plt.ylabel("Average Price (£)", fontsize=16)
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.gca().set_ylim(bottom=100000, top=400000)
plt.gca().set_xlim(left=0, right=1)
plt.locator_params(axis='x', nbins=2)
plt.locator_params(axis='y', nbins=3)

plt.xlabel( "Location Desirability\n(0=Not desirable)\n(1=Desirable)" , fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.legend( labels = ["A","B","C"],
            title='Location',
            title_fontsize=16,
            loc="upper right",
            bbox_to_anchor=(1.5,1),
            framealpha=0,
            ncol = 1,
            labelspacing = 1.2,
            fontsize=16)


plt.savefig("_scatter_generic" + ".png", bbox_inches='tight', transparent=True)
plt.close()





#plot the scatter
plt.rcParams["figure.figsize"] = (7,7)
x2 = np.array([0.2,0.4,0.8])
y2 = np.array([350000,240000,180000])
colors2 = np.array(["red","green","blue"])
#text_labels = np.array(["Ward A","Ward B","Ward C"])

for xp2, yp2, c2 in zip(x2, y2, colors2):
   plt.scatter(xp2, yp2, s=800, c=c2)

#plt.rcParams["figure.figsize"] = (3.5,3)
plt.title("Average Property Price vs. Location Desirability", fontsize=28, y=1.12)
plt.ylabel("Average Price (£)", fontsize=24)
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.gca().set_ylim(bottom=100000, top=400000)
plt.gca().set_xlim(left=0, right=1)
plt.locator_params(axis='x', nbins=2)
plt.locator_params(axis='y', nbins=3)

plt.xlabel( "Location Desirability\n(0=Not desirable)\n(1=Desirable)" , fontsize=24)
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)

plt.legend( labels = ["A","B","C"],
            title='Location',
            title_fontsize=24,
            loc="upper right",
            bbox_to_anchor=(1.5,1),
            framealpha=0,
            ncol = 1,
            labelspacing = 1.2,
            fontsize=24)


plt.savefig("_scatter_generic_2" + ".png", bbox_inches='tight', transparent=True)
plt.close()