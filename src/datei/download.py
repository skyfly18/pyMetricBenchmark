import os
import importlib.resources as res
import pathlib as path
from urllib import request

# Erstelle die Ordner wo gearbeitet werden
def makeordner(home):
    os.mkdir(home)
    globeljarsname = "globaljars"
    csvfile = "ergebniss"
    group5 = "group5"
    multifileg = "multifileguava"
    multifilesp = "multifilespring"
    globeljars = os.path.join(home, globeljarsname)
    os.mkdir(globeljars)
    os.mkdir(os.path.join(home, csvfile))
    os.mkdir(os.path.join(home, group5))
    os.mkdir(os.path.join(home, multifileg))
    os.mkdir(os.path.join(home, multifilesp))


def download(home):
    for filename in os.listdir(res.path()):
        jarfile = os.path.join(home, filename)
        with open(os.path.join(res.path(), filename), 'r') as file:
            for line in file.readline():
                if "#" != line[0]:
                    name = line.rsplit('/')
                    jarname = name.pop().rsplit('\n')
                    down = os.path.join(jarfile, jarname[0])
                    request.urlretrieve(line, down)


# Downloade alle datein die in den Textfiles stehen
def download_init(home):
    pathhome = path.PurePath("./txtfiles")
    for filename in os.listdir(pathhome):
        jarfile = os.path.join(home, filename)
        jarfile2 = os.path.join(pathhome, filename)
        with open(jarfile2, 'r') as file:
            for line in file:
                if "#" != line[0] and " " != line[0]:
                    filename = line.rsplit('/')
                    jarname = filename.pop().rsplit('\n')
                    down = os.path.join(jarfile, jarname[0])
                    request.urlretrieve(line, down)


# Berechne die jar größen
def datei_groesse(jardir):
    jardict = {}
    for filename in os.listdir(jardir):
        jarpath = os.path.join(jardir, filename)
        kb = round(os.path.getsize(jarpath) / 1024, 3)
        jardict[filename] = kb
    return jardict
