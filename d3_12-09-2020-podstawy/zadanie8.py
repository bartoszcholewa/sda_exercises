import datetime
import time
import random

trafienia = 0
while True:
    hit = random.randint(0, 100)
    if hit >= 50 and hit <= 60:
        print(f"=== TRAFIENIE o {datetime.datetime.now()} =====")
        print(f"{hit}, (Trafienia: {trafienia})")
        trafienia += 1
    else:
        print(f"{hit}, (Trafienia: {trafienia})")
    time.sleep(1)