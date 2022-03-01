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
Einstellung wie wo die Datein gepeichert werden sollen und den Path zur Fatjar wird in der main.py angepasst.
Die Einstellungen werden unter den Kommentare Einstellungen vorgenommen.

Das Skript lässt sich wie folgt ausführen. 
1: Konsole
  - Öffnen sie die Konsole im Verzeichniss wo die main.py liegt. Dan geben sie denn Befehl python main.py an.
2: Pycharm
  - Öffnen sie das Projekt in Pycharm. Öffnen sie die main.py und führen diese in Pycharm aus.

Beachtetn Sie das die abhängigkeiten installiert sind. Auch darf der Ordner "BenchmarkGroup5" im ausgewählten Verzeichniss nicht exiestieren. Sonst bricht das Programm mit einen Fehler meldung ab.



## Ergebnisse

Die Ergebnisse liegen im Ordner Ergebnisse, dort liegt auch die performance-report.csv. Diese nicht öffen wenn das Programm läuft. In dieser Datei wird nichts gepeichert und wird während des Durchlauf des Programms mehrmals überschrieben.