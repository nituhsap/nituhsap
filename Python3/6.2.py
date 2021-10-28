class Point:
    __a = ['*', '*']

    def set_a(self, x, y):
        b = [x, y]
        self.__a = b
    def set_x(self, x):
        b = self.__a
        b[0] = x
        self.__a = b
    def set_y(self, y):
        b = self.__a
        b[1] = y
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

class Shape:
    def space(self):
        return 0
    def prm(self):
        return 0

class Quadrangle(Shape):
    def __init__(self, p1, p2, p3, p4):
        self.A = p1.distance(p2)
        self.B = p2.distance(p3)
        self.C = p3.distance(p4)
        self.D = p4.distance(p1)
        self.d13 = p1.distance(p3)

    def space(self):
        prm1 = self.A + self.B + self.d13
        prm2 = self.C + self.D + self.d13
        S1 = (prm1*(prm1-self.A)*(prm1-self.B)*(prm1-self.d13))^0,5
        S2 = (prm2*(prm2-self.C)*(prm2-self.D)*(prm2-self.d13))^0,5
        return S1+S2

    def prm(self):
        p = self.A + self.B + self.C + self.D
        return p









