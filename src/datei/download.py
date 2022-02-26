import os
import requests
import importlib.resources as res
import pathlib as path

def makeOrdner(home):
    try:
        os.mkdir(home)
        globeljarsname = "globaljars"
        csvfile = "ergebniss"
        globeljars = os.path.join(home,globeljarsname)
        os.mkdir(globeljars)
        os.mkdir(os.path.join(home,csvfile))
        return True
    except:
        return False




def download(home):
    for filename in os.listdir(res.path()):
        jarfile = os.path.join(home, filename)
        with open(os.path.join(res.path(),filename),'r') as file:
            for line in file.readline():
                if "#" != line[0]:
                    r = requests.get(line, allow_redirects=True)
                    name = line.rsplit('/')
                    jarname = name.pop().rsplit('\n')
                    down = os.path.join(jarfile, jarname[0])
                    open(down, 'wb').write(r.content)

def download_init(home):
    pathhome = path.PurePath("./txtfiles")
    print(pathhome)
    for filename in os.listdir(pathhome):
        jarfile = os.path.join(home, filename)
        jarfile2 = os.path.join(pathhome, filename)
        with open(jarfile2,'r') as file:
            for line in file:
                if "#" != line[0] and " " !=line[0]:
                    r = requests.get(line, allow_redirects=True)
                    filename = line.rsplit('/')
                    jarname = filename.pop().rsplit('\n')
                    down =os.path.join(jarfile,jarname[0])
                    open(down, 'wb').write(r.content)


