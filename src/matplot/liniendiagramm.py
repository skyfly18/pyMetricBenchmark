import pandas as pd
import matplotlib.pyplot as plt
from src.fatjar import osinfos
import numpy as np
from sklearn.linear_model import LinearRegression
from array import *


def simpleline(data, jarname, namebild, messsungen, jardict,title):
    for file in jarname:
        data[file] = data[file].astype(float)
    sumdata = data.sum() / messsungen
    listxy = []
    for name in jarname:
        tupleXY = (jardict[name], sumdata[name])
        listxy.append(tupleXY)
    listxy.sort(key=lambda tup: tup[0])
    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    plt.plot(*zip(*listxy), label=title)
    plt.xlabel("Größe der jars in kb")
    plt.legend(title=osinfos.system_infos(messsungen), loc='upper left')
    plt.title(title)
    plt.savefig(namebild + ".png")
    plt.close()


def allbenchmarklinie(vref, vdec, wmc, loop, jarname, namebild, messsungen, jardict,title):
    for file in jarname:
        vref[file] = vref[file].astype(float)
        vdec[file] = vdec[file].astype(float)
        wmc[file] = wmc[file].astype(float)
        loop[file] = loop[file].astype(float)

    sumvref = vref.sum() / messsungen
    sumvdec = vdec.sum() / messsungen
    sumloop = loop.sum() / messsungen
    sumwmc = wmc.sum() / messsungen
    listvref = []
    listvdec = []
    listloop = []
    listwmc = []
    for name in jarname:
        listvdec.append((jardict[name], sumvdec[name]))
        listvref.append((jardict[name], sumvref[name]))
        listloop.append((jardict[name], sumloop[name]))
        listwmc.append((jardict[name], sumwmc[name]))
    listvref.sort(key=lambda tup: tup[0])
    listvdec.sort(key=lambda tup: tup[0])
    listloop.sort(key=lambda tup: tup[0])
    listwmc.sort(key=lambda tup: tup[0])
    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    plt.plot(*zip(*listvref), label="Metrik Vref")
    plt.plot(*zip(*listvdec), label="Metrik Vdec")
    plt.plot(*zip(*listloop), label="Metrik Loop")
    plt.plot(*zip(*listwmc), label="Metrik Wmc")
    plt.xlabel("Größe der jars in kb")
    plt.legend(title=osinfos.system_infos(messsungen), loc='upper left')
    plt.title(title)
    plt.savefig(namebild + ".png")
    plt.close()


def scatterdiagramm(data, jarname, namebild, messsungen, jardict,title):
    fig = plt.figure()
    fig.set_figwidth(20)
    fig.set_figheight(16)
    for file in jarname:
        data[file] = data[file].astype(float)
    sumdata = data.sum() / messsungen
    listx = []
    listy = []
    listxy = []
    for name in jarname:
        plt.scatter(jardict[name], sumdata[name], label=name)
        listx.append(jardict[name])
        listy.append(sumdata[name])
        listxy.append((jardict[name], sumdata[name]))

    np_listx = np.asarray(listx).reshape(-1, 1)
    np_listy = np.asarray(listy)
    np_listxy = np.asarray(listxy).reshape(1, -1)
    linear_regressor = LinearRegression().fit(np_listx, np_listy)
    y_pred =linear_regressor.predict(np_listx)
    plt.plot(listx, y_pred)
    plt.xlabel("Größe der jars in kb")
    plt.legend(title=osinfos.system_infos(messsungen), loc='upper left')
    plt.title(title)
    plt.savefig(namebild + ".png")
    plt.close()
