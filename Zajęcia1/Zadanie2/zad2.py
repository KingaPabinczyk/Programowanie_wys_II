class Martix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__ (self):
        return (f"[ {self.a} {self.b} ]\n"
                f"[ {self.c} {self.d} ]")

    def __add__(self, other):
        return Martix(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __mul__(self, other):
        return Martix((self.a*other.a+self.b*other.c),(self.a*other.b+self.b*other.d),(self.c*other.a+self.d*other.c),(self.c*other.b+self.d*other.d))

    def __repr__(self):
        return (f"[ {self.a} {self.b} ] \n"
                f"[ {self.c} {self.d} ] \n")

m1 = Martix(1,2,3,4)
m2 = Martix(2,0,1,2)

m3 = m1 + m2
print("Wynik dodawania macierzy:")
print(m3)
print("\n")
m4 = m1 * m2

print("Wynik mnożenia macierzy:")
print(repr(m4))
