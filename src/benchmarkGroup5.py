import subprocess
from pathlib import Path
import os
from fatjar import subfatjar
import pandas as pd
import numpy as np



def readbenchmetrik():
    df = pd.read_csv('performance-report.csv')



def vrefDataframm(vrefpd, csvdata,jarsname):
    #csvindex=csvdata.loc
    dict={}
    for i in range(len(csvdata)):
        file = csvdata.at[i,"File"]
        if(file == "<framework init> "):
            continue
        spfile = file.rsplit('/')
        jarname = spfile.pop()
        for name in jarsname:
            if name == jarname:
                dict[name] = csvdata.at[i,"methods.vref"]
    series = pd.Series(dict)
    vrefpd.loc[len(vrefpd.index+1)]=series



    print(vrefpd.to_string())


def benchmarkGroup5(fatjar,home,messungen):
    globeljarsname = "globaljars"
    globeljars = os.path.join(home, globeljarsname)

    # Wechsel ins Verzeichniss wo die CSVs abgespeichert werden
    csvfile = "ergebniss"
    os.chdir(os.path.join(home,csvfile))
    allsinglemetrik = {"methods.loop":[],"VariablesDeclared.count":[],"methods.vref":[] ,"wmc":[]}
    allglobaljarsname =[]
    for filename in os.listdir(globeljars):
        allglobaljarsname.append(filename)
    vrefglobal = pd.DataFrame(columns=allglobaljarsname)
    print(vrefglobal.to_string())
    for i in range(messungen):
        #subfatjar.runAllSingle(fatjar,globeljars,home)
        df = pd.read_csv('performance-report.csv')
        vrefDataframm(vrefglobal,df,allglobaljarsname)


    print(df)

    print(os.getcwd())



