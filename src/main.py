import benchmarkGroup5
import os
from datei import download
def entrypoint() -> None:
    benchmarkGroup5()


if __name__ == '__main__':

    # Einstellungen
    homename = "BenchmarkGroup5" # Name des root Ordners wo das Skript daten speichert
    path = os.path.expanduser('~') # Path wo der root Ordner liegen soll
    fatjar = os.path.expanduser('~/Dokumente/framework/analysis-application.jar') # Pfad zur Fatjar der analysis
    messungen = 2 #Anzahl der wiederholen der Messung

    print(path)


    home = os.path.join(path, homename)
    download.makeOrdner(home)
    download.download_init(home)
    benchmarkGroup5.benchmarkGroup5(fatjar,home,messungen)
