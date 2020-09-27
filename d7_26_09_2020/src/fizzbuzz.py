def fizz_buzz(x):
    if x > 0 and x <= 100:
        if x % 15 == 0:
            return "FizzBuzz"
        elif x % 5 == 0:
            return "Buzz"
        elif x % 3 == 0:
            return "Fizz"
        return x
    return 0