import sys, os
print(os.path.dirname(__file__))

def get_data(how_much):
    with open("/home/bartosz/Dropbox/SDA/PYTwro11/linux/sda-exercises/d8_27_09_2020/src/dane.txt", "r") as f:
        return f.read(how_much)

def get_avg(how_much):
    data = get_data(how_much)
    numbers = [int(x) for x in data]
    return sum(numbers) / len(numbers)
