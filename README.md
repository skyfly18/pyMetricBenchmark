# pyMetricBenchmark
Dieses Skript Anlysisiert Laufzeiten der Metriken der Gruppe5 des Fachprojekts ["fachproject-metrics-framework"] (https://github.com/sse-labs/fachproject-metrics-framework).
Dafür führt das Skript das Framework mithilfe von subprocess aus und liest die performance-report.csv ein.
Danach werden die Ergebnisse mithilfe von pandas und matplotlib dargestellt.

## Abhängigkeiten

Dieses Programm hängt davon ab das Fachproject-metrics-framework als ein fatjar vorliegt. Auch muss java über die konsole aufrufbar sein.

Die Python abhängigkeiten sind

...

    python >=3.8
    pandas >= 1.4.0
    numpy >= 1.22
    matplotlib >= 3.5.0
    psutil >= 5.3.0
    py-cpuinfo >= 8.0.0
    scikit-learn >= 1.0.0
...

## Ausführen

Das Skript lässt sich


## Ergebnisse

Die Ergebnisse liegen im Ordner Ergebnisse, dort liegt auch die performatscsv