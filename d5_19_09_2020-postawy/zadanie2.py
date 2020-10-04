def sumujacy(*cyferki):
    return sum(cyferki)

#print(sumujacy())
#print(sumujacy(7,9))
#print(sumujacy(1,2,3,4,5))

def info_kwargs(**kwargs):
    print(kwargs)

info_kwargs(a=3)
info_kwargs()
info_kwargs(x=4, q=1)
info_kwargs(q,w=12) #NameError: name 'q' is not defined
