def sum_arguments(max_value, args):
    ret = 0
    for x in args:
        if isinstance(x, int):
            if isinstance(max_value, int):
                if x < max_value:
                    ret += x
            else:
                if x < 10:
                    ret += x
    return ret

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError("Prosze wprowadzac litery")
    return x.capitalize()
