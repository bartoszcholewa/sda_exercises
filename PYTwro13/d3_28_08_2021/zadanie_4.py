"""
Pliki binarne
"""

# define a dictionary
my_dict = {
    "lion": ["male", "45", "5"],
    "panther": ["female", "30", "2"],
    "bear": ["male", "100", "15"],
    "zebra": ["female", "70", "6"],
}
print(my_dict, type(my_dict))

# save a dictionary as text file
with open("my_dict.txt", "w") as file:
    file.write(str(my_dict))

# save dictionary as binary file (i.e. serialise it)
import pickle
with open("my_dict.pkl", "wb") as file:
    # pickle.dump saves an object (here my_dict) to the binary file (here text_dict.pkl)
    pickle.dump(my_dict, file)

# read my_dict.txt
with open("my_dict.txt", "r") as file:
    new_dict_txt = file.readlines()
    # we need a custom parsing
    # ...
print(new_dict_txt, type(new_dict_txt))

# read my_dict.pkl
with open("my_dict.pkl", "rb") as file:
    new_dict_pkl = pickle.load(file)
print(new_dict_pkl, type(new_dict_pkl))