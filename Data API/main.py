import subprocess

variables = ['BTE.py', 'Interest.py', 'NaturalGas.py', 'SPY.py', 'WTI.py']

for filename in variables:
    subprocess.run(['python', filename])