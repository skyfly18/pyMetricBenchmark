import pandas as pd
import matplotlib.pyplot as plt
from src.fatjar import osinfos


def boxplotD(data, jarname, namebild, messsungen,title):
    for file in jarname:
        data[file] = data[file].astype(float)
    i = 0
    zahl = 1
    while i < len(jarname):
        list = []
        for z in range(4):
            if (i < len(jarname)):
                list.append(jarname[i])
                i += 1
        fig = plt.figure()
        fig.set_figwidth(18)
        fig.set_figheight(8)
        boxplotGH = data.boxplot(column=list)
        boxplotGH.plot()
        plt.legend(title=osinfos.system_infos(messsungen), loc="upper left")
        plt.title(title)
        plt.savefig(namebild + str(zahl) + ".png")
        plt.close()
        zahl += 1
        i += 1
