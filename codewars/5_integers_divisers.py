import math

def list_squared(m, n):
    return_list = list()
    for number in range(m, n+1):
        number_divisors = find_divisors(number)
        number_square_divisors = square_divisors(number_divisors)
        number_sum_square_divisors = sum(number_square_divisors)
        if is_sqrt(number_sum_square_divisors):
            return_list.append([number, number_sum_square_divisors])
    return return_list





def find_divisors(number):
    dividors_list = list()
    i = 1
    while i <= math.sqrt(number):
        if number % i == 0:
            if number / i == i:
                dividors_list.append(i)
            else:
                dividors_list.append(i)
                dividors_list.append(int(number / i))
        i += 1
    dividors_list.sort()
    return dividors_list


def square_divisors(dividors_list):
    squared_divisors_list = map(lambda n: n ** 2, dividors_list)
    return list(squared_divisors_list)


def list_sum(squared_divisors_list):
    return sum(squared_divisors_list)


def is_sqrt(number):
    return math.sqrt(number).is_integer()


# list_squared(1, 250)
# print(find_divisors(42))
# print(square_divisors(find_divisors(42)))
# print(list_sum(square_divisors(find_divisors(42))))
# print(is_sqrt(list_sum(square_divisors(find_divisors(42)))))
print(list_squared(250, 500))