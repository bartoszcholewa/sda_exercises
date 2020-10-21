def mnoznik(n):
    def func(a):
        new_list = []
        for i in range(1,n+1):
            new_list.append(a * i)
        return new_list
    return func

make_5 = mnoznik(10)
print(make_5("A"))