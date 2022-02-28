import subprocess


def runAllSingle(fatjar, files):
    sub = subprocess.run(
        ['java', '-jar', fatjar, '--batch-mode', '--include-analysis', 'methods.loop', '--include-analysis',
         'VariablesDeclared.count', '--include-analysis', 'methods.vref', '--include-analysis', 'wmc',
         '--evaluate-performance', files], capture_output=True)


def runMultiFile(fatjar, files):
    sub = subprocess.run(
        ['java', '-jar', fatjar,'--multi-file', '--include-analysis', 'Internal Stability',
         '--evaluate-performance', files], capture_output=True)


def runSingleStoreAndLoad(fatjar, files):
    sub = subprocess.run(
        ['java', '-jar', fatjar, '--batch-mode', '--include-analysis', 'methods.vref','--outstoreandloadcount',
         '--evaluate-performance', files], capture_output=True)

def runSingleInfo(fatjar, files):
    sub = subprocess.run(
        ['java', '-jar', fatjar, '--batch-mode',  '--include-analysis', 'methods.vref', '--infozuvariablen',
         '--evaluate-performance', files], capture_output=True)

def runAllArgument(fatjar, files):
    sub = subprocess.run(
        ['java', '-jar', fatjar, '--batch-mode', '--include-analysis', 'methods.loop', '--include-analysis',
         'VariablesDeclared.count', '--include-analysis', 'methods.vref','--outstoreandloadcount', '--infozuvariablen',  '--include-analysis', 'wmc',
         '--evaluate-performance', files], capture_output=True)