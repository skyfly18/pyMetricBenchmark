import os
import requests
import importlib.resources as res

def makeOrdner(path):
    try:
        homename = "BenchmarkGroup5"
        home = os.path.join(path, homename)
        os.mkdir(home)
        globeljarsname = "globeljars"
        globeljars = os.path.join(home,globeljarsname)
        os.mkdir(globeljars)
        return True
    except:
        return False


def download():
    for filename in os.listdir(res.path()):
        with open(os.path.join(res.path(),filename),'r') as file:
            for line in file.readline():
                if "#" != line[0]:
                    r = requests.get(line, allow_redirects=True)
                    open('', 'wb').write(r.content)
