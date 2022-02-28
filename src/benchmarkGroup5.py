import os
import pandas as pd
from src.matplot import boxplot, liniendiagramm
from src.datei import download
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
    # Java befehle als String
    multifilestring = "java -jar /path/fatjar --multi-file --include-analysis Internal Stability \n " \
                      "--evaluate-performance /path/jars\n"

    singelAllstring = "java -jar /path/fatjar --batch-mode --include-analysis methods.loop --include-analysis " \
                      "VariablesDeclared.count --include-analysis methods.vref --include-analysis wmc\n " \
                      "--evaluate-performance /path/jars\n "

    singelStstring = "java -jar /path/fatjar --batch-mode --include-analysis methods.vref \n " \
                     "--outstoreandloadcount --evaluate-performance /path/jars\n "

    singelInfostring = "java -jar /path/fatjar --batch-mode --include-analysis methods.vref --infozuvariablen \n " \
                       "--evaluate-performance /path/jars\n "

    singelAllArgstring = "java -jar /path/fatjar --batch-mode --include-analysis methods.vref --infozuvariablen  \n" \
                         "--outstoreandloadcount  --evaluate-performance /path/jars\n "
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
    print("---------Beginne auswertung des gemeinsamen Benchmark-------------")
    for i in range(messungen):
        subfatjar.runAllSingle(fatjar, globeljars)
        df = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefglobal, df, allglobaljarsname)
        wmcDataframm(wmcglobal, df, allglobaljarsname)
        loopDataframm(loopglobal, df, allglobaljarsname)
        vdDataframm(vdglobal, df, allglobaljarsname)
    boxplot.boxplotD(vrefglobal, allglobaljarsname, "vrefglobalboxplot", messungen, "Vref Global", singelAllstring)
    boxplot.boxplotD(wmcglobal, allglobaljarsname, "wmcglobalboxplot", messungen, "Wmc Global", singelAllstring)
    boxplot.boxplotD(loopglobal, allglobaljarsname, "loopglobalboxplot", messungen, "Loop Global", singelAllstring)
    boxplot.boxplotD(vdglobal, allglobaljarsname, "vdecglobalboxplot", messungen, "Vdec Global", singelAllstring)
    liniendiagramm.simpleline(vrefglobal, allglobaljarsname, "vrefgloballinien", messungen, globaljargroesse, "Vref", singelAllstring)
    liniendiagramm.scatterdiagramm(vrefglobal, allglobaljarsname, "vrefglobalregrasson", messungen, globaljargroesse,
                                   "Vref", singelAllstring)
    liniendiagramm.simpleline(vdglobal, allglobaljarsname, "vdecgloballinien", messungen, globaljargroesse, "Vdec", singelAllstring)
    liniendiagramm.scatterdiagramm(vdglobal, allglobaljarsname, "vdecglobalregrasson", messungen, globaljargroesse,
                                   "Vdec", singelAllstring)
    liniendiagramm.simpleline(wmcglobal, allglobaljarsname, "wmcgloballinien", messungen, globaljargroesse, "Wmc", singelAllstring)
    liniendiagramm.scatterdiagramm(wmcglobal, allglobaljarsname, "wmcglobalregrasson", messungen, globaljargroesse,
                                   "Wmc", singelAllstring)
    liniendiagramm.simpleline(loopglobal, allglobaljarsname, "loopgloballinien", messungen, globaljargroesse, "Loop")
    liniendiagramm.scatterdiagramm(loopglobal, allglobaljarsname, "loopglobalregrasson", messungen, globaljargroesse,
                                   "Loop", singelAllstring)
    liniendiagramm.allbenchmarklinie(vrefglobal, vdglobal, wmcglobal, loopglobal, allglobaljarsname, "Global-Benchmark",
                                     messungen, globaljargroesse, "Diagramm aller Metriken der Gruppe 5", singelAllstring)

    # Speziale Analyse von vref mit Argumente auf Global benchmark
    print("------------Beginne auswertung mit speziellen argumente auf den gemeinsammen Benchmark---------------------")
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
    liniendiagramm.scatterdiagramm(vrefglobalAllArg, allglobaljarsname, "vrefargslobalregrasson", messungen, globaljargroesse,
                                   "Vref all Argumente", singelAllArgstring)
    liniendiagramm.scatterdiagramm(vrefglobalVa, allglobaljarsname, "vrefinfolobalregrasson", messungen, globaljargroesse,
                                   "Vref Argument Info", singelInfostring)
    liniendiagramm.scatterdiagramm(vrefglobalStandL, allglobaljarsname, "vrefstandlglobalregrasson", messungen, globaljargroesse,
                                   "Vref Argument StoreAndLoad", singelStstring)
    liniendiagramm.allvreflinie(vrefglobal,vrefglobalVa, vrefglobalStandL, vrefglobalAllArg, allglobaljarsname, "vrefglobalvergleich", messungen, globaljargroesse, "Vref mit und ohne Argumente Vergleich auf dem gemeinsamen Benchmark")




