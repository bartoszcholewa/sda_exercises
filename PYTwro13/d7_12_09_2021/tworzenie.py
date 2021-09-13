import os


def create_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        print(f"Creation of the directory {path} failed")
        return

    return "success"


if __name__ == '__main__':
    a = create_dir("tworzenie_dir")
    print(a)
