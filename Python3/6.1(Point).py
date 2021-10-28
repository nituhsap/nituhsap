class Point:
    __a = ['*', '*']

    def set_a(self, x, y):
        b = [x, y]
        self.__a = b
    def set_x(self, x):
        b = self.__a
        b[0] = str(x)
        self.__a = b
    def set_y(self, y):
        b = self.__a
        b[1] = str(y)
        self.__a = b

    def get_a(self):
        b = self.__a
        return self.__a
    def get_x(self):
        b = self.__a
        return ' '.join(b[0])
    def get_y(self):
        b = self.__a
        return ' '.join(b[1])








