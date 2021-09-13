class OdwrotnieClass:
    """ Odwrotnie class """

    def __init__(self, name):
        self._name = name

    def reverse(self):
        """ Reverse name"""
        return ''.join(reversed(self._name))
