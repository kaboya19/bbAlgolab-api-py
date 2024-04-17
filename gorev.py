import subprocess
import time
from algolab import API
from config import *
import schedule
import time
import subprocess

def run_once():
    activate_cmd = [
        "C:\\Users\\Bora\\Documents\\GitHub\\bbAlgolab-api-py\\.venv\\Scripts\\python.exe",
        "ornek_soket.py"
    ]
    subprocess.Popen(activate_cmd)

def run_every_five_minutes():
    activate_cmd1 = [
        "C:\\Users\\Bora\\Documents\\GitHub\\bbAlgolab-api-py\\.venv\\Scripts\\python.exe",
        "trade.py"
    ]
    subprocess.Popen(activate_cmd1)


run_once()


schedule.every(5).minutes.do(run_every_five_minutes)
schedule.every(30).seconds.do(run_once)

while True:
    schedule.run_pending()
    time.sleep(1)



