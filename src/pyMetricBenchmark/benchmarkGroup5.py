import os
import pandas as pd
from pyMetricBenchmark.matplot import boxplot, liniendiagramm
from pyMetricBenchmark.matplot import balkenplot
from pyMetricBenchmark.datei import download
from pyMetricBenchmark.fatjar import subfatjar


# Funktionen um die Daten der Performace csv in eigenständige Dataframm zu ändern
# Im column steht die jar file namen
def vrefDataframm(data, csvdata, jarsname):
    ddict = {}
    for i in range(len(csvdata)):
        file = csvdata.at[i, "File"]
        if (file == "<framework init> "):
            continue
        spfile = file.rsplit('/')
        jarname = spfile.pop()
        for name in jarsname:
            if name == jarname:
                ddict[name] = csvdata.at[i, "methods.vref"]
    series = pd.Series(ddict)
    data.loc[len(data.index + 1)] = series


def loopDataframm(data, csvdata, jarsname):
    ddict = {}
    for i in range(len(csvdata)):
        file = csvdata.at[i, "File"]
        if (file == "<framework init> "):
            continue
        spfile = file.rsplit('/')
        jarname = spfile.pop()
        for name in jarsname:
            if name == jarname:
                ddict[name] = csvdata.at[i, "methods.loop"]
    series = pd.Series(ddict)
    data.loc[len(data.index + 1)] = series


def wmcDataframm(data, csvdata, jarsname):
    ddict = {}
    for i in range(len(csvdata)):
        file = csvdata.at[i, "File"]
        if (file == "<framework init> "):
            continue
        spfile = file.rsplit('/')
        jarname = spfile.pop()
        for name in jarsname:
            if name == jarname:
                ddict[name] = csvdata.at[i, "wmc"]
    series = pd.Series(ddict)
    data.loc[len(data.index + 1)] = series


def vdDataframm(data, csvdata, jarsname):
    dict = {}
    for i in range(len(csvdata)):
        file = csvdata.at[i, "File"]
        if (file == "<framework init> "):
            continue
        spfile = file.rsplit('/')
        jarname = spfile.pop()
        for name in jarsname:
            if name == jarname:
                dict[name] = csvdata.at[i, "VariablesDeclared.count"]
    series = pd.Series(dict)
    data.loc[len(data.index + 1)] = series

def inStDataframm(data, csvdata, jarsname):
    dict = {}
    for i in range(len(csvdata)):
        file = csvdata.at[i, "File"]
        if (file == "<framework init> "):
            continue
        spfile = file.rsplit('/')
        jarname = spfile.pop()
        for name in jarsname:
            if name == jarname:
                dict[name] = csvdata.at[i, "Internal Stability"]
    series = pd.Series(dict)
    data.loc[len(data.index + 1)] = series

def benchmarkGroup5(fatjar, home, messungen):

    # Verzeichniss Namen
    globeljarsname = "globaljars"
    group5 = "group5"
    multifileg = "multifileguava"
    multifilesp = "multifilespring"

    # Pfade zur jars
    globeljars = os.path.join(home, globeljarsname)
    group5jars = os.path.join(home, group5)
    multifileguava = os.path.join(home, multifileg)
    multifilespring = os.path.join(home, multifilesp)

    # Wechsel ins Verzeichniss wo die CSVs abgespeichert werden
    # Alle Ergebnisse werden hier abgespeichert
    csvfile = "ergebniss"
    os.chdir(os.path.join(home, csvfile))

   # Einrichtung der benötigten Variablen
    allglobaljarsname = []
    for filename in os.listdir(globeljars):
        allglobaljarsname.append(filename)
    globaljargroesse = download.datei_groesse(globeljars)
    vrefglobal = pd.DataFrame(columns=allglobaljarsname)
    vdglobal = pd.DataFrame(columns=allglobaljarsname)
    wmcglobal = pd.DataFrame(columns=allglobaljarsname)
    loopglobal = pd.DataFrame(columns=allglobaljarsname)
    # Analysis der gemeinsames Benchmark
    print("---------Beginne Auswertung des gemeinsamen Benchmark-------------")
    for i in range(messungen):
        subfatjar.runAllSingle(fatjar, globeljars)
        df = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefglobal, df, allglobaljarsname)
        wmcDataframm(wmcglobal, df, allglobaljarsname)
        loopDataframm(loopglobal, df, allglobaljarsname)
        vdDataframm(vdglobal, df, allglobaljarsname)
    boxplot.boxplotD(vrefglobal, allglobaljarsname, "vrefglobalboxplot", messungen, "Vref Boxplot Gemeinsamer Benchmark")
    boxplot.boxplotD(wmcglobal, allglobaljarsname, "wmcglobalboxplot", messungen, "Wmc Boxplot Gemeinsamer Benchmark")
    boxplot.boxplotD(loopglobal, allglobaljarsname, "loopglobalboxplot", messungen, "Loop Boxplot Gemeinsamer Benchmark")
    boxplot.boxplotD(vdglobal, allglobaljarsname, "vdecglobalboxplot", messungen, "Vdec BoxplotGemeinsamer Benchmark")
    liniendiagramm.simpleline(vrefglobal, allglobaljarsname, "vrefgloballinien", messungen, globaljargroesse, "Vref Gemeinsamer Benchmark")
    liniendiagramm.scatterdiagramm(vrefglobal, allglobaljarsname, "vrefglobalregression", messungen, globaljargroesse,
                                   "Vref Gemeinsamer Benchmark")
    liniendiagramm.simpleline(vdglobal, allglobaljarsname, "vdecgloballinien", messungen, globaljargroesse, "Vdec Gemeinsamer Benchmark")
    liniendiagramm.scatterdiagramm(vdglobal, allglobaljarsname, "vdecglobalregression", messungen, globaljargroesse,
                                   "Vdec Gemeinsamer Benchmark")
    liniendiagramm.simpleline(wmcglobal, allglobaljarsname, "wmcgloballinien", messungen, globaljargroesse, "Wmc Gemeinsamer Benchmark")
    liniendiagramm.scatterdiagramm(wmcglobal, allglobaljarsname, "wmcglobalregression", messungen, globaljargroesse,
                                   "Wmc Gemeinsamer Benchmark")
    liniendiagramm.simpleline(loopglobal, allglobaljarsname, "loopgloballinien", messungen, globaljargroesse, "Loop Gemeinsamer Benchmark")
    liniendiagramm.scatterdiagramm(loopglobal, allglobaljarsname, "loopglobalregression", messungen, globaljargroesse,
                                   "Loop Gemeinsamer Benchmark")
    liniendiagramm.allbenchmarklinie(vrefglobal, vdglobal, wmcglobal, loopglobal, allglobaljarsname, "Global-Benchmark",
                                     messungen, globaljargroesse, "Diagramm aller Metriken der Gruppe 5")

    boxplot.boxplotallmetrics(vrefglobal, wmcglobal, loopglobal, vdglobal, allglobaljarsname, "boxplotallmetrics", messungen, "Boxplot aller Metrics Gemeinsamer Benchmark")

    # Speziale Analyse von vref mit Argumente auf Global benchmark
    print("------------Beginne auswertung mit speziellen argumente auf dem gemeinsamen Benchmark---------------------")
    vrefglobalStandL = pd.DataFrame(columns=allglobaljarsname)
    vrefglobalVa = pd.DataFrame(columns=allglobaljarsname)
    vrefglobalAllArg = pd.DataFrame(columns=allglobaljarsname)

    for i in range(messungen):
        subfatjar.runSingleStoreAndLoad(fatjar, globeljars)
        df = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefglobalStandL, df, allglobaljarsname)
        subfatjar.runSingleInfo(fatjar, globeljars)
        df2 = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefglobalVa, df2, allglobaljarsname)
        subfatjar.runAllArgument(fatjar, globeljars)
        df3 = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefglobalAllArg, df3, allglobaljarsname)
    liniendiagramm.scatterdiagramm(vrefglobalAllArg, allglobaljarsname, "vrefargsglobalregression", messungen,
                                   globaljargroesse,
                                   "Vref all Argumente")
    liniendiagramm.scatterdiagramm(vrefglobalVa, allglobaljarsname, "vrefinfoglobalregression", messungen,
                                   globaljargroesse,
                                   "Vref Argument Info")
    liniendiagramm.scatterdiagramm(vrefglobalStandL, allglobaljarsname, "vrefstandlglobalregression", messungen,
                                   globaljargroesse,
                                   "Vref Argument StoreAndLoad")
    liniendiagramm.allvreflinie(vrefglobal, vrefglobalVa, vrefglobalStandL, vrefglobalAllArg, allglobaljarsname,
                                "vrefglobalvergleich", messungen, globaljargroesse,
                                "Vref mit und ohne Argumente Vergleich auf dem gemeinsamen Benchmark")
    balkenplot.balkenVref(vrefglobal, vrefglobalVa, vrefglobalStandL, vrefglobalAllArg, allglobaljarsname,
                          "vrefglobalvergleichbalken", messungen,"Vref mit und ohne Argumente Vergleich")

    print("------------Beginne Multifile Analysis---------------------")
    guavajarsname = []
    for filename in os.listdir(multifileguava):
        guavajarsname.append(filename)
    springjarsname = []
    for filename in os.listdir(multifilespring):
        springjarsname.append(filename)
    guavagrosse = download.datei_groesse(multifileguava)
    springgroesse = download.datei_groesse(multifilespring)
    guava = pd.DataFrame(columns=guavajarsname)
    spring = pd.DataFrame(columns=springjarsname)
    for i in range(messungen):
        subfatjar.runMultiFile(fatjar, multifileguava)
        df = pd.read_csv('performance-report.csv')
        inStDataframm(guava, df, guavajarsname)
        subfatjar.runMultiFile(fatjar, multifilespring)
        df2 = pd.read_csv('performance-report.csv')
        inStDataframm(spring, df2, springjarsname)
    liniendiagramm.multifilelinie(guava, spring, guavajarsname, springjarsname, "multifile", messungen, guavagrosse, springgroesse, "Multifile Analysis")

    print("-----------------------Beginne Auswerung des Benchmarks der Gruppe-------------------------------")
    # Einrichtung der benötigten Variablen
    gruppe5jarsname = []
    for filename in os.listdir(group5jars):
        gruppe5jarsname.append(filename)
    gruppe5jargroesse = download.datei_groesse(group5jars)
    vrefgruppe5 = pd.DataFrame(columns=gruppe5jarsname)
    vdgruppe5 = pd.DataFrame(columns=gruppe5jarsname)
    wmcgruppe5 = pd.DataFrame(columns=gruppe5jarsname)
    loopgruppe5 = pd.DataFrame(columns=gruppe5jarsname)


    for i in range(messungen):
        subfatjar.runAllSingle(fatjar, group5jars)
        df = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefgruppe5, df, gruppe5jarsname)
        wmcDataframm(wmcgruppe5, df, gruppe5jarsname)
        loopDataframm(loopgruppe5, df, gruppe5jarsname)
        vdDataframm(vdgruppe5, df, gruppe5jarsname)
    boxplot.boxplotD(vrefgruppe5, gruppe5jarsname, "vrefgruppe5boxplot", messungen, "Vref Boxplot Gruppe5")
    boxplot.boxplotD(wmcgruppe5, gruppe5jarsname, "wmcgruppe5boxplot", messungen, "Wmc Boxplot Gruppe5")
    boxplot.boxplotD(loopgruppe5, gruppe5jarsname, "loopgruppe5boxplot", messungen, "Loop Boxplot Gruppe5")
    boxplot.boxplotD(vdgruppe5, gruppe5jarsname, "vdecgruppe5boxplot", messungen, "Vdec Boxplot Gruppe5")
    liniendiagramm.simpleline(vrefgruppe5, gruppe5jarsname, "vrefgruppe5linien", messungen, gruppe5jargroesse, "Vref Gruppe5 Benchmark")
    liniendiagramm.scatterdiagramm(vrefgruppe5, gruppe5jarsname, "vrefgruppe5regression", messungen, gruppe5jargroesse,
                                   "Vref Gruppe5 Benchmark")
    liniendiagramm.simpleline(vdgruppe5, gruppe5jarsname, "vdecgruppe5linien", messungen, gruppe5jargroesse, "Vdec Gruppe5 Benchmark")
    liniendiagramm.scatterdiagramm(vdgruppe5, gruppe5jarsname, "vdecgruppe5regression", messungen, gruppe5jargroesse,
                                   "Vdec Gruppe5 Benchmark")
    liniendiagramm.simpleline(wmcgruppe5, gruppe5jarsname, "wmcgruppe5linien", messungen, gruppe5jargroesse, "Wmc  Gruppe5 Benchmark")
    liniendiagramm.scatterdiagramm(wmcgruppe5, gruppe5jarsname, "wmcgruppe5regression", messungen, gruppe5jargroesse,
                                   "Wmc Gruppe5 Benchmark")
    liniendiagramm.simpleline(loopgruppe5, gruppe5jarsname, "loopgruppe5linien", messungen, gruppe5jargroesse, "Loop Gruppe5 Benchmark")
    liniendiagramm.scatterdiagramm(loopgruppe5, gruppe5jarsname, "loopgruppe5regression", messungen, gruppe5jargroesse,
                                   "Loop Gruppe5 Benchmark")
    liniendiagramm.allbenchmarklinie(vrefgruppe5, vdgruppe5, wmcgruppe5, loopgruppe5, gruppe5jarsname,
                                     "Gruppe5-Benchmark",
                                     messungen, gruppe5jargroesse, "Diagramm aller Metriken der Gruppe 5")

    boxplot.boxplotallmetrics(vrefgruppe5, wmcgruppe5, loopgruppe5, vdgruppe5, gruppe5jarsname, "boxplotallmetricsgruppe5", messungen, "Boxplot aller Metrics Gruppe5 Benchmark")

    # Speziale Analyse von vref mit Argumente auf denn Gruppe5 benchmark
    print("------------Beginne auswertung mit speziellen Argumenten auf dem Gruppe5 Benchmark---------------------")
    vrefgruppe5StandL = pd.DataFrame(columns=gruppe5jarsname)
    vrefgruppe5Va = pd.DataFrame(columns=gruppe5jarsname)
    vrefgruppe5AllArg = pd.DataFrame(columns=gruppe5jarsname)

    for i in range(messungen):
        subfatjar.runSingleStoreAndLoad(fatjar, group5jars)
        df = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefgruppe5StandL, df, gruppe5jarsname)
        subfatjar.runSingleInfo(fatjar, group5jars)
        df2 = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefgruppe5Va, df2, gruppe5jarsname)
        subfatjar.runAllArgument(fatjar, group5jars)
        df3 = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefgruppe5AllArg, df3, gruppe5jarsname)
    liniendiagramm.scatterdiagramm(vrefgruppe5AllArg, gruppe5jarsname, "vrefargsgruppe5regression", messungen,
                                   gruppe5jargroesse,
                                   "Vref all Argumente Gruppe5 Benchmark")
    liniendiagramm.scatterdiagramm(vrefgruppe5Va, gruppe5jarsname, "vrefinfogruppe5regression", messungen,
                                   gruppe5jargroesse,
                                   "Vref Argument Info Gruppe5 Benchmark")
    liniendiagramm.scatterdiagramm(vrefgruppe5StandL, gruppe5jarsname, "vrefstandlgruppe5regression", messungen,
                                   gruppe5jargroesse,
                                   "Vref Argument StoreAndLoad Gruppe5 Benchmark")
    liniendiagramm.allvreflinie(vrefgruppe5, vrefgruppe5Va, vrefgruppe5StandL, vrefgruppe5AllArg, gruppe5jarsname,
                                "vrefgruppe5vergleich", messungen, gruppe5jargroesse,
                                "Vref mit und ohne Argumente Vergleich auf dem Gruppe5 Benchmark")
    balkenplot.balkenVref(vrefgruppe5, vrefgruppe5Va, vrefgruppe5StandL, vrefgruppe5AllArg, gruppe5jarsname,
                          "vrefgruppe5vergleichbalken", messungen, "Vref mit und ohne Argumente Vergleich Gruppe5 Benchmark")


    print("----------------------Auswertung beendet-----------------------------------------------------\n")
    print("Die Graphen sind im Ordner Ergebnisse im Verzeichniss:" + home)


