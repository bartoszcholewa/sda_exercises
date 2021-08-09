def its_a_trap():
    a = [0, 1, 2]
    b = []
    for x in range(3, 11):
        b.append(a)
        a.pop(0)
        a.append(x)
    print(a)


its_a_trap()


def element_list(n, num_of_elements):
    return [x for x in range(n, n + num_of_elements)]


def its_not_a_trap(num_of_lists=4, num_of_elements=3):
    return [element_list(n, num_of_elements) for n in range(1, num_of_lists + 1)]


print(its_not_a_trap(10, 5))
