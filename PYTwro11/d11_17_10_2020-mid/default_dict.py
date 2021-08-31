from collections import defaultdict

normal_dict = {}
# print(normal_dict["key"]) # !!! KeyError

default_dict = defaultdict(str)
print("key:", default_dict["key"]) # key:
print(default_dict.items())

default_dict_2 = defaultdict(lambda: "default string")
print("key:", default_dict_2["key"]) # key: default string
print(default_dict.items())