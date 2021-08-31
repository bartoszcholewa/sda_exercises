from itertools import groupby
string = 'baaaallleee'
ret = ''
for name, group in groupby(string, lambda x: x):
    l = len(list(group))
    ret += name + str(l) if l > 1 else ret + name
print(ret)