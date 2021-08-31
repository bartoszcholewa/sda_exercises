def sum_all(*args) -> float:
    ret = 0.0
    for number in args:
        ret += number
    return ret


print(sum_all(1, 5, 35, 3.32, 1.42))


def sum_all_2(*args) -> float:
    return sum(args)


print(sum_all_2(1, 5, 35, 3.32, 1.42))
