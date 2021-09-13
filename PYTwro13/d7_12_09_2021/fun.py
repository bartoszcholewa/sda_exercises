import os


def fun():
    try:
        os.path.exists("")
    except NameError:
        return "A"
    except ValueError:
        return "B"
    except KeyError:
        return "C"
    except IndexError:
        return "D"
