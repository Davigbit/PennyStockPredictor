import subprocess

variables = ['BTE.py', 'Interests.py', 'NaturalGas.py', 'SPY.py', 'WTI.py']

for filename in variables:
    subprocess.run(['python', filename])