class Cell:
    def __init__(self, number):
        self.number = number
        self.cell = '*'

    def __sub__(self, other):
        if self.number >= other.number:
            return Cell(self.number - other.number)
        print(f'Операция недопустима: количество клеток\n'
              f' в первом объекте ({self.number}) меньше,'
              f' чем во втором ({other.number})')
        return Cell(-1)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def make_order(self, n):
        rest = self.number
        while rest > n:
            print(n * self.cell)
            rest -= n
        print(rest * self.cell, '\n')


cell_1 = Cell(20)
cell_2 = Cell(23)

res_add = cell_1.__add__(cell_2)
print(res_add.number)

res_sub = cell_1.__sub__(cell_2)
print(res_sub.number)

res_mul = cell_1.__mul__(cell_2)
print(res_mul.number)

res_div = cell_1.__truediv__(cell_2)
print(res_div.number)

cell_1.make_order(7)
cell_2.make_order(6)
