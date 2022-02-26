import benchmarkGroup5
import os
from datei import download
def entrypoint() -> None:
    benchmarkGroup5()


if __name__ == '__main__':
    homename = "BenchmarkGroup5"
    path = os.path.expanduser('~')
    print(path)
    home = os.path.join(path, homename)
    download.makeOrdner(home)
    download.download_init(home)
    benchmarkGroup5.benchmarkGroup5()
