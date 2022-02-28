import matplotlib.pyplot as plt
from pyMetricBenchmark.fatjar import osinfos


def balkenVref(vref, vrefInfo, vrefStAndL, vrefAllArgs, jarname, namebild, messsungen, title):
    for file in jarname:
        vref[file] = vref[file].astype(float)
        vrefInfo[file] = vrefInfo[file].astype(float)
        vrefStAndL[file] = vrefStAndL[file].astype(float)
        vrefAllArgs[file] = vrefAllArgs[file].astype(float)
    sumvref = vref.sum() / messsungen
    sumvrefInfo = vrefInfo.sum() / messsungen
    sumvrefAll = vrefAllArgs.sum() / messsungen
    sumvrefStAndL = vrefStAndL.sum() / messsungen
    fig = plt.figure()
    fig.set_figwidth(10)
    fig.set_figheight(10)
    width = 1
    x = ["Vref", "Vref Info Argument", "Vref Store and Load Argument", "Vref beide Argumente"]
    y = [sumvref.sum() / sumvref.size, sumvrefInfo.sum()/ sumvrefInfo.size, sumvrefStAndL.sum()/ sumvrefStAndL.size, sumvrefAll.sum()/sumvrefAll.size]
    plt.bar(x,y)
    plt.ylabel("Zeit messung")
    plt.legend(title=osinfos.system_infos(messsungen), loc='upper left')
    plt.title(title)
    plt.savefig(namebild + ".png")
    plt.close()
