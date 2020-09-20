def argumenty_argsy_kwargsy(x, y=1, *args,**kwargs):
    print(x,y,args, kwargs)
argumenty_argsy_kwargsy(3, a=7)
argumenty_argsy_kwargsy(3,7,a=7)
argumenty_argsy_kwargsy(3,7,8,a=7)
argumenty_argsy_kwargsy()
#argumenty_argsy_kwargsy(7,y=5,5) #SyntaxError: positional argument follows keyword argument