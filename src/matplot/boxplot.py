import matplotlib.pyplot as plt
from src.fatjar import osinfos
import pandas as pd


# Erstellt boxplot für jeden einzelnen Jar
def boxplotD(data, jarname, namebild, messsungen, title):
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
        plt.ylabel("Zeit messung")
        plt.legend(title=osinfos.system_infos(messsungen), loc="upper left")
        plt.title(title)

        plt.savefig(namebild + str(zahl) + ".png")
        plt.close()
        zahl += 1
        i += 1

# Erstellt einen Boxplot wo alle Metriken gezeigt werden
def boxplotallmetrics(vref, wmc, loop, vdec, jarname, namebild, messsungen, title):
    for file in jarname:
        vref[file] = vref[file].astype(float)
        wmc[file] = wmc[file].astype(float)
        loop[file] = loop[file].astype(float)
        vdec[file] = vdec[file].astype(float)
    sumvref = vref.sum() / messsungen
    sumwmc = wmc.sum() / messsungen
    sumvdec = vdec.sum() / messsungen
    sumloop = loop.sum() / messsungen
    fig = plt.figure()
    fig.set_figwidth(18)
    fig.set_figheight(8)
    df = pd.concat([sumvref, sumvdec, sumloop, sumwmc], axis=1)
    df.columns =['VREF', 'VDEC','LOOP', 'WMC']
    df_plot = df.boxplot()
    df_plot.plot()
    plt.ylabel("Zeit messung")
    plt.legend(title=osinfos.system_infos(messsungen), loc="upper left")
    plt.title(title)
    plt.savefig(namebild + ".png")
    plt.close()
