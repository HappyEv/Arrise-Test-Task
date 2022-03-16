class Bear:
    def __init__(self, id, name, type, age):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__age = age

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age