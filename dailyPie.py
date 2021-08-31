from numpy import add
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

from pandas.core.dtypes.missing import isnull

label_color = {"BK":"blue",
                "CH":"cyan",
                "EAT":"green",
                "WK":"yellow",
                "LN":"gold",
                "GYM":"pink",
                "RD":"purple",
                "ON":"brown",
                "BH":"mediumblue"}

def draw(daliyData, daily_date, daily_week):
    
    dailyDict = defaultdict(lambda:0)

    totalTime = 0
    for x in daliyData:
        if not (pd.isnull(x) or x == "GU" or x == "SP") :
            dailyDict[x] += 1
            totalTime += 1

    # Data to plot
    labels = []
    sizes = []
    colors = []

    for x, y in dailyDict.items():
        if not x in label_color:
            raise ValueError(f"{x} doesnot exists in label set")
        else:
            labels.append(x)
            sizes.append(y)
            colors.append(label_color[x])

    # Plot
    def absolute_value(val):
        #print(val*0.5*totalTime/100.)
        a  = np.round(val/200.*totalTime, 2)
        return a
    plt.pie(sizes, labels=labels, autopct=absolute_value, colors=colors)

    plt.axis('equal')
    title = "{}-{}-TotalTime-{}".format(daily_date, daily_week, totalTime/2)
    new_title = title.replace(r'/',"-")
    plt.title(new_title)
    plt.savefig("dailyImg/{}.png".format(new_title))