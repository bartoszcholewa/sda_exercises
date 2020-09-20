def foo(lst=None):
    #lst.append('a')
    #lst = lst + ['a']
    if lst is None:
        lst = []
    lst.append('a')
    print(lst)
    return lst
foo()
foo()
foo()
foo()
foo()