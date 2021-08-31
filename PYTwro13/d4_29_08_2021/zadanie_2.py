""" DefaultDict """
from collections import defaultdict

# Normal dict:

zwierzeta = {
    "pies": "1",
    "kot": "2",
    "kon": "3",
    "slon": "4"
}

try:
    print(zwierzeta['pies'], zwierzeta['bocian'])
except KeyError as e:
    print(e)


zwierzeta2 = defaultdict(list)

print(zwierzeta2['kotki'])
print(zwierzeta2)
