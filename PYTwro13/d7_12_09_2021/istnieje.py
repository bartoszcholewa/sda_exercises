from os import path


def istnieje(a):
    if path.exists(a):
        return 50
    else:
        return 200
