"""
Ścieżki, os, pathlib
"""

import os
import pathlib

# directory_name = "mk_dircatalogue"
# print('I am here: ', os.getcwd()) # wypisz aktualną lokacje
# if not os.path.exists(directory_name):
#     print(os.mkdir(directory_name))
# os.chdir(directory_name)
# print(os.getcwd())
#
# dir_1 = '/home/bartosz/Dropbox/SDA/PYTwro11/linux/sda-exercises/PYTwro13/d3_08_2021/'
# dir_2 = '/home/bartosz/Dropbox/SDA/PYTwro11/linux/sda-exercises/PYTwro13/d3_08_2021'
# file_name = 'sample.txt'
# print(os.path.join(dir_1, file_name))
# print(os.path.join(dir_2, file_name))

"""napisz funkcję, która tworzy katalog i w przypadku gdy on istnieje nie rzuca wyjątkiem, tylko wypisuje informacje na 
konsoli, że dany katalog istnieje"""


def create_catalogue_os(path_to_catalogue: str) -> None:
    """
    examples of path_to_catalogue: "/Users/michal/PycharmProjects/testitest", "my_catalogue"
    """
    if os.path.exists(path_to_catalogue):
        os.chdir(path_to_catalogue)
        print(f'Katalog już istnieje: {os.getcwd()}')
    else:
        os.mkdir(path_to_catalogue)
        os.chdir(path_to_catalogue)
        print(f'Katalog utworzony: {os.getcwd()}')


# create_catalogue_os('lubie_placki_os')

def create_catalogue_pathlib(path_to_catalogue: str) -> None:
    path = pathlib.Path(path_to_catalogue)

    """ #1 spodziewaj się błędu istnienia folderu"""
    try:
        path.mkdir()
        print(f'Katalog utworzony: {path.absolute()}')
    except FileExistsError:
        print(f'Katalog już istnieje: {path.absolute()}')

    """ #2 sprawdzaj czy folder istnieje przed utworzeniem"""
    if path.exists():
        print(f'Katalog już istnieje: {path.absolute()}')
    else:
        path.mkdir()
        print(f'Katalog utworzony: {path.absolute()}')

    """ #3 wykorzystaj logikę funkcji tworzenia folderów exist_ok=True """
    path.mkdir(parents=True, exist_ok=True)
    print(f'Katalog istnieje/utworzony: {path.absolute()}')


create_catalogue_pathlib('/home/bartosz/Dropbox/SDA/PYTwro11/linux/sda-exercises/PYTwro13/d3_08_2021/lubie_placki_pathlib')
