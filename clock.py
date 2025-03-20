import time
from datetime import datetime

while True:
    now = datetime.now()
    print("\rCurrent Time:", now.strftime("%H:%M:%S"), end="")
    time.sleep(1)