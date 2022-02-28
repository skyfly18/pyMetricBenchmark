import os
import pandas as pd
from src.matplot import boxplot, liniendiagramm
from datei import download
from src.fatjar import subfatjar


def vrefDataframm(vrefpd, csvdata, jarsname):
    # csvindex=csvdata.loc
    dict = {}
    for i in range(len(csvdata)):
        file = csvdata.at[i, "File"]
        if (file == "<framework init> "):
            continue
        spfile = file.rsplit('/')
        jarname = spfile.pop()
        for name in jarsname:
            if name == jarname:
                dict[name] = csvdata.at[i, "methods.vref"]
    series = pd.Series(dict)
    vrefpd.loc[len(vrefpd.index + 1)] = series


def loopDataframm(vrefpd, csvdata, jarsname):
    # csvindex=csvdata.loc
    dict = {}
    for i in range(len(csvdata)):
        file = csvdata.at[i, "File"]
        if (file == "<framework init> "):
            continue
        spfile = file.rsplit('/')
        jarname = spfile.pop()
        for name in jarsname:
            if name == jarname:
                dict[name] = csvdata.at[i, "methods.loop"]
    series = pd.Series(dict)
    vrefpd.loc[len(vrefpd.index + 1)] = series


def wmcDataframm(vrefpd, csvdata, jarsname):
    # csvindex=csvdata.loc
    dict = {}
    for i in range(len(csvdata)):
        file = csvdata.at[i, "File"]
        if (file == "<framework init> "):
            continue
        spfile = file.rsplit('/')
        jarname = spfile.pop()
        for name in jarsname:
            if name == jarname:
                dict[name] = csvdata.at[i, "wmc"]
    series = pd.Series(dict)
    vrefpd.loc[len(vrefpd.index + 1)] = series


def vdDataframm(vrefpd, csvdata, jarsname):
    # csvindex=csvdata.loc
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
    vrefpd.loc[len(vrefpd.index + 1)] = series


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

    # Analysis der gemeinsames Benchmark
    allglobaljarsname = []
    for filename in os.listdir(globeljars):
        allglobaljarsname.append(filename)
    globaljargroesse = download.datei_größe(globeljars, allglobaljarsname)
    vrefglobal = pd.DataFrame(columns=allglobaljarsname)
    vdglobal = pd.DataFrame(columns=allglobaljarsname)
    wmcglobal = pd.DataFrame(columns=allglobaljarsname)
    loopglobal = pd.DataFrame(columns=allglobaljarsname)
    for i in range(messungen):
        subfatjar.runAllSingle(fatjar, globeljars)
        df = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefglobal, df, allglobaljarsname)
        wmcDataframm(wmcglobal, df, allglobaljarsname)
        loopDataframm(loopglobal, df, allglobaljarsname)
        vdDataframm(vdglobal, df, allglobaljarsname)
    boxplot.boxplotD(vrefglobal, allglobaljarsname, "vrefglobalboxplot", messungen, "Vref Global")
    boxplot.boxplotD(wmcglobal, allglobaljarsname, "wmcglobalboxplot", messungen, "Wmc Global")
    boxplot.boxplotD(loopglobal, allglobaljarsname, "loopglobalboxplot", messungen, "Loop Global")
    boxplot.boxplotD(vdglobal, allglobaljarsname, "vdecglobalboxplot", messungen, "Vdec Global")
    liniendiagramm.simpleline(vrefglobal, allglobaljarsname, "vrefgloballinien", messungen, globaljargroesse, "Vref")
    liniendiagramm.scatterdiagramm(vrefglobal, allglobaljarsname, "vrefglobalregrasson", messungen, globaljargroesse, "Vref")
    liniendiagramm.simpleline(vdglobal, allglobaljarsname, "vdecgloballinien", messungen, globaljargroesse, "Vdec")
    liniendiagramm.scatterdiagramm(vdglobal, allglobaljarsname, "vdecglobalregrasson", messungen, globaljargroesse, "Vdec")
    liniendiagramm.simpleline(wmcglobal, allglobaljarsname, "wmcgloballinien", messungen, globaljargroesse, "Wmc")
    liniendiagramm.scatterdiagramm(wmcglobal, allglobaljarsname, "wmcglobalregrasson", messungen, globaljargroesse, "Wmc")
    liniendiagramm.simpleline(loopglobal, allglobaljarsname, "loopgloballinien", messungen, globaljargroesse, "Loop")
    liniendiagramm.scatterdiagramm(loopglobal, allglobaljarsname, "loopglobalregrasson", messungen, globaljargroesse, "Loop")
    liniendiagramm.allbenchmarklinie(vrefglobal, vdglobal, wmcglobal, loopglobal, allglobaljarsname, "Global-Benchmark",
                                     messungen, globaljargroesse, "Diagramm aller Metriken der Gruppe 5")

    # Speziale Analyse von vref mit Argumente auf Global benchmark



    print(os.getcwd())
