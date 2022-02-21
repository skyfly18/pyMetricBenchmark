import benchmarkGroup5
import os
from datei import download
def entrypoint() -> None:
    benchmarkGroup5()


if __name__ == '__main__':
    path = os.path.expanduser('~\Documents')
    print(path)
    download.makeOrdner(path)
    benchmarkGroup5.benchmarkGroup5()