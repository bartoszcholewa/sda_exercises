import random
import os
file = "zadanie2.txt"
size = 0
while not size >= 1048576:
    f = open(file, "a")
    f.write(str(random.randint(10000, 99999)) + "\n")
    f.close()
    size = os.path.getsize(file)
    if size % 10000 == 0:
        print(size)