import platform
import psutil
from io import StringIO
from cpuinfo import get_cpu_info
import subprocess


def system_infos(messungen):
    uname = platform.uname()
    infos = StringIO()
    infos.write("System: " + uname.system + "\n")
    infos.write("Release: " + uname.release + "\n")
    infos.write("Version: " + uname.version + "\n")
    infos.write("Machine: " + uname.machine + "\n")
    infos.write("Processor: " + get_cpu_info()["brand_raw"] + "\n")
    infos.write("Total cores: " + str(psutil.cpu_count()) + "\n")
    infos.write("Total Ram: " + str(round(psutil.virtual_memory().total / (1024.0 ** 3), 3)) + " GB" + "\n")
    javainfo = subprocess.run(["java", "--version"], capture_output=True)
    infos.write("------Java------\n")
    infos.write(javainfo.stdout.decode("utf-8"))
    infos.write("------Daten der Messung------\n")
    infos.write("Anzahl der Messungen: " + str(messungen) + "\n")
    return infos.getvalue()
