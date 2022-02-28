import matplotlib.pyplot as plt
from src.fatjar import osinfos
import numpy as np
from sklearn.linear_model import LinearRegression


def simpleline(data, jarname, namebild, messsungen, jardict, title):
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
    plt.ylabel("Zeit messung")
    plt.legend(title=osinfos.system_infos(messsungen), loc='upper left')
    plt.title(title)

    plt.savefig(namebild + ".png")
    plt.close()


def allbenchmarklinie(vref, vdec, wmc, loop, jarname, namebild, messsungen, jardict, title):
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
    plt.ylabel("Zeit messung")
    plt.legend(title=osinfos.system_infos(messsungen), loc='upper left')
    plt.title(title)

    plt.savefig(namebild + ".png")
    plt.close()


def scatterdiagramm(data, jarname, namebild, messsungen, jardict, title):
    fig = plt.figure()
    fig.set_figwidth(20)
    fig.set_figheight(16)
    for file in jarname:
        data[file] = data[file].astype(float)
    sumdata = data.sum() / messsungen
    listx = []
    listy = []
    for name in jarname:
        plt.scatter(jardict[name], sumdata[name], label=name)
        listx.append(jardict[name])
        listy.append(sumdata[name])

    np_listx = np.asarray(listx).reshape(-1, 1)
    np_listy = np.asarray(listy)
    linear_regressor = LinearRegression().fit(np_listx, np_listy)
    y_pred = linear_regressor.predict(np_listx)
    plt.plot(listx, y_pred)
    plt.xlabel("Größe der jars in kb")
    plt.ylabel("Zeit messung")
    plt.legend(title=osinfos.system_infos(messsungen), loc='upper left')
    plt.title(title)

    plt.savefig(namebild + ".png")
    plt.close()


def allvreflinie(vref, vrefInfo, vrefStAndL, vrefAllArgs, jarname, namebild, messsungen, jardict, title):
    for file in jarname:
        vref[file] = vref[file].astype(float)
        vrefInfo[file] = vrefInfo[file].astype(float)
        vrefStAndL[file] = vrefStAndL[file].astype(float)
        vrefAllArgs[file] = vrefAllArgs[file].astype(float)

    sumvref = vref.sum() / messsungen
    sumvrefInfo = vrefInfo.sum() / messsungen
    sumvrefAll = vrefAllArgs.sum() / messsungen
    sumvrefStAndL = vrefStAndL.sum() / messsungen
    listvref = []
    listvrefInfo = []
    listvrefAll = []
    listvrefSt = []
    for name in jarname:
        listvrefInfo.append((jardict[name], sumvrefInfo[name]))
        listvref.append((jardict[name], sumvref[name]))
        listvrefAll.append((jardict[name], sumvrefAll[name]))
        listvrefSt.append((jardict[name], sumvrefStAndL[name]))
    listvref.sort(key=lambda tup: tup[0])
    listvrefInfo.sort(key=lambda tup: tup[0])
    listvrefAll.sort(key=lambda tup: tup[0])
    listvrefSt.sort(key=lambda tup: tup[0])
    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    plt.plot(*zip(*listvref), label="Vref")
    plt.plot(*zip(*listvrefInfo), label="Vref Argument Info")
    plt.plot(*zip(*listvrefAll), label="Vref Alle Argumente")
    plt.plot(*zip(*listvrefSt), label="Vref Store And Load Argument")
    plt.xlabel("Größe der jars in kb")
    plt.ylabel("Zeit messung")
    plt.legend(title=osinfos.system_infos(messsungen), loc='upper left')
    plt.title(title)

    plt.savefig(namebild + ".png")
    plt.close()

    def multifilelinie(guava, spring, jarnameguava, jarnamespring, namebild, messsungen, jardictguava, jardictspring, title):
        for file in jarname:
            guava[file] = guava[file].astype(float)
            spring[file] = spring[file].astype(float)

        summulti1 = guava.sum() / messsungen
        summulti2 = spring.sum() / messsungen
        multi1list = []
        listmulti2 = []
        for name in jarnameguava:
            multi1list.append((jardictguava[name], summulti1[name]))
        for name in jarnamespring:
            listmulti2.append((jardictspring[name], summulti2[name]))
        multi1list.sort(key=lambda tup: tup[0])
        listmulti2.sort(key=lambda tup: tup[0])
        fig = plt.figure()
        fig.set_figwidth(10)
        fig.set_figheight(10)
        plt.plot(*zip(*multi1list), label="Guava")
        plt.plot(*zip(*listmulti2), label="Spring")
        plt.xlabel("Größe der jars in kb")
        plt.ylabel("Zeit messung")
        plt.legend(title=osinfos.system_infos(messsungen), loc='upper left')
        plt.title(title)
        plt.savefig(namebild + ".png")
        plt.close()
