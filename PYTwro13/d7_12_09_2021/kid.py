class Kid:
    def __init__(self, first_name, second_name):
        self.__first_name = first_name
        self.__second_name = second_name
        self._marks = []

    def __str__(self):
        return f"{self.__first_name} {self.__second_name}"

    def get_mark(self, mark):
        self._marks.append(mark)

