class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return Complex(a, b)

    def __repr__(self):
        if self.b == 0:
            return f'{self.a}'
        elif self.b < 0:
            return f'{self.a} - {-self.b}i'
        elif a == 0:
            return f'{self.b}'
        else:
            return f'{self.a} + {self.b}i'


def is_number(string):
    if string.isdigit():
        string = int(string)
        return string
    else:
        try:
            string = float(string)
            return string
        except ValueError:
            string = 0
            return string


a = input('Первое чило: действительная часть:\n')
b = input('мнимая часть:\n')
c = input('Второе чило: действительная часть:\n')
d = input('мнимая часть:\n')
lst = [a, b, c, d]
for i in range(len(lst)):
    lst[i] = is_number(lst[i])

complex1 = Complex(lst[0], lst[1])
complex2 = Complex(lst[2], lst[3])
print(f'Первое число: x = {complex1.__repr__()}\n'
      f'Второе число: y = {complex2.__repr__()}')
print()
print(f'Их сумма x + y = {complex1.__add__(complex2)}')
print()
print(f'Их произведение x * y = {complex1.__mul__(complex2)}')

