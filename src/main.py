import benchmarkGroup5
import os
from datei import download
import sys


def entrypoint() -> None:
    if len(sys.argv) == 4:
        if os.path.isdir(sys.argv[1]): raise Exception("Ein vorhandener Ordner")
        if not os.path.isfile(sys.argv[2]): raise Exception("Keine jar file")
        if int(sys.argv[3]) <= 0: raise Exception("Anzahl der wiederholungen unter 0")
        home = sys.argv[1]
        fatjar = sys.argv[2]
        messungen = sys.argv[3]
        download.makeordner(home)
        download.download_init(home)
        benchmarkGroup5.benchmarkGroup5(fatjar, home, messungen)
    else:
        print("Zu wenige Argumente")


if __name__ == '__main__':
    # Einstellungen
    homename = "BenchmarkGroup5"  # Name des root Ordners wo das Skript daten speichert
    path = os.path.expanduser('~')  # Path wo der root Ordner liegen soll
    fatjar = os.path.expanduser('~/Dokumente/framework/analysis-application.jar')  # Pfad zur Fatjar der analysis
    messungen = 1  # Anzahl der wiederholen der Messung

    home = os.path.join(path, homename)
    download.makeordner(home)
    download.download_init(home)
    benchmarkGroup5.benchmarkGroup5(fatjar, home, messungen)
