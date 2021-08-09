""" Arksy i kwargsy """
import inspect

def foo_args(*args):
    print(f'{type(args)} {foo_args.__name__}', args, '\n')

print(inspect.getsource(foo_args))
foo_args(10, 20, 30)


def sum_args(*args):
    print(f'{type(args)} {sum_args.__name__}:', sum(args), '\n')

print(inspect.getsource(sum_args))
sum_args(10, 20, 30, 40, 50, 60)



def print_kwargs(**kwargs):
    print(f'{type(kwargs)} {print_kwargs.__name__}: {kwargs}', '\n')
    print(kwargs.values())

print(inspect.getsource(print_kwargs))
print_kwargs(jeden='1', dwa=2, trzy=3, cztery='4')



def argumenty_arksy_kwargsy(x, y=1, *test1, **test2):
    print(f'x={x}, y={y}, args={test1}, kwargs={test2}', '\n')
    for value in test1:
        print('Value:', value)
    for k, v in test2.items():
        print('Key:', k, 'Value:', v)

print('\n')
print(inspect.getsource(argumenty_arksy_kwargsy))
argumenty_arksy_kwargsy(3, a=7)
argumenty_arksy_kwargsy(3, 7, a=7)
argumenty_arksy_kwargsy(3, 7, 8, a=7)
argumenty_arksy_kwargsy(3)
