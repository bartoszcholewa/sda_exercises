"""
Operacje logiczne na list, set, dict, tuple, str
"""


def operands(a, b):
    print('===', type(a), '===')
    try:
        add = a + b
        print(f'  +  : Success, {add}')
    except Exception as e:
        print(f'  +  : Fail, {str(e)}')

    try:
        minus = a - b
        print(f'  -  : Success, {minus}')
    except Exception as e:
        print(f'  -  : Fail, {str(e)}')

    try:
        minus = a & b
        print(f'  &  : Success, {minus}')
    except Exception as e:
        print(f'  &  : Fail, {str(e)}')

    try:
        minus = a | b
        print(f'  |  : Success, {minus}')
    except Exception as e:
        print(f'  |  : Fail, {str(e)}')


# List:
list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']
operands(list_1, list_2)

# Set:
set_1 = {1, 2, 3, 'd'}
set_2 = {'a', 'b', 'c', 'd'}
operands(set_1, set_2)

# Dict:
dict_1 = {1: 1, 2: 2, 3: 3}
dict_2 = {'a': 'a', 'b': 'b', 'c': 'c'}
operands(dict_1, dict_2)

# Tuple:
tuple_1 = (1, 2, 3)
tuple_2 = ('a', 'b', 'c')
operands(tuple_1, tuple_2)

# String
string_1 = '123'
string_2 = 'abc'
operands(string_1, string_2)

