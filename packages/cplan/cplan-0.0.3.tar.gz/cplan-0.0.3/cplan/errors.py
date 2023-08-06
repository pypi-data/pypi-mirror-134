class nameNotFoundError(Exception):
    def __init__(self, name):
        self.name = name
        self.__str__()

    def __str__(self):
        return 'The {} parameter does not exist'.format(self.name)


class NotIterableError(Exception):
    def __init__(self):
        # self.name = name
        self.__str__()

    def __str__(self):
        return 'This is not an iteration object'
