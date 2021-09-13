"""
My classes
"""


class LittleClass:
    """ My little class """
    def __init__(self, name: str) -> None:
        self._name: str = name

    def big_name(self) -> str:
        """ Returns name upper case """
        return self._name.upper()