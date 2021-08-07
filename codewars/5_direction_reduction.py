def dirReduc(arr):
    vector = {"NORTH": 1, "SOUTH": -1, "EAST": 2, "WEST": -2}
    while True:
        for index, direction in enumerate(arr):
            if len(arr) > index + 1:
                if vector[direction] + vector[arr[index+1]] == 0:
                    arr.pop(index)
                    arr.pop(index)
                    break
            else:
                return arr

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# a = ["SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# a = ["SOUTH", "NORTH", "WEST"]
# a = ["WEST"]
u=["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(a))
print(dirReduc(u))