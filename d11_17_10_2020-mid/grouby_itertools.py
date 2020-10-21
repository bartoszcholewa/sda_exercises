from itertools import groupby

menu = [("fruit", "orange"),
        ("fruit", "banana"),
        ("drink", "beer"),
        ("drink", "tea"),
        ("fruit", "apple"),
        ("fruit", "apple")]
lista_produktow = dict()
for name, group in groupby(sorted(menu), lambda x: x[0]):
    #lista_produktow[list(group)[0]] = list(group)[1]
    # print(name)
    print(list(group))
#print(lista_produktow)