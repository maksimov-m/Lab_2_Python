class BadInitValue(Exception):
    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message


class BadCountException(Exception):
    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message


class BadEqualeException(Exception):
    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message