

class Square:

    def __init__(self, side):
        self.side = side


    @property
    def side(self):
        return self.__side


    @side.setter
    def side(self, value):
        if value < 0:
            raise ValueError("Bok nie może być mniejszy od 0")
        self.__side = value

    @property
    def area(self):
        return self.side ** 2

    def __add__(self, other):
        return Square(self.side + other.side)

    def __gt__(self, other):
        return self.side > other.side

    def __repr__(self):
        return f"Square({self.side})"

s = Square(10)
s2 = Square(20)

print("sss", s._Square__side)

# s.side = 10

print(s.area)


print(s + s2)
print(s > s2)