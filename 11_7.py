class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - (self.b * other.b),  self.b * other.a)

    def __str__(self):
        return f'{self.a} + {self.b}i'


z1 = ComplexNumber(1, -2)
z2 = ComplexNumber(3, 4)

print(z1, z2)
print(z1 + z2)
