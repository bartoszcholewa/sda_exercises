# https://www.codewars.com/kata/54d81488b981293527000c8f
# Best Solution

def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

# My solution
def sum_pairs(ints, s):
    if len(ints) < 1000:
        return iterator(ints, s)
    else:
        return big_iterator(ints, s)


def iterator(ints, s):
    return_dict = {}
    while len(ints) > 1:
        iterations = 0
        first = ints.pop(0)
        for second in ints:
            if first + second == s:
                if iterations in return_dict:
                    iterations += 1
                return_dict[iterations] = [first, second]
            iterations += 1
    iterations = 0
    if return_dict:
        i = min(return_dict, key=return_dict.get)
        return return_dict[i]


def big_iterator(ints, s):
    if s % 2 == 0 and s / 2 in ints:
        ints = list(dict.fromkeys(ints))
        return iterator(ints, s)
    else:
        ints = list(set(ints))
        return iterator(ints, s)
