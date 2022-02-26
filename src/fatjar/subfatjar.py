import subprocess
import os

def runAllSingle(fatjar, files,home ):

    subprocess.call(['java','-jar', fatjar, '--batch-mode', '--include-analysis', 'methods.loop', '--include-analysis', 'VariablesDeclared.count', '--include-analysis', 'methods.vref', '--include-analysis','wmc','--evaluate-performance',files])

