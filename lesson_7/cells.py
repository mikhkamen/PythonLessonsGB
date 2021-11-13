class Cells:
    def __init__(self, number):
        self.number = number
        self.cell = '*'

    def __sub__(self, other):
        if self.number >= other.number:
            return Cells(self.number - other.number)
        print(f'Количество клеток в первом объекте ({self.number}) меньше,'
              f' чем во втором ({other.number}).\nБудет создан объект Cells(0)')
        return Cells(0)

    def __mul__(self, other):
        return Cells(self.number * other.number)

    def __truediv__(self, other):
        return Cells(int(round(self.number / other.number, 0)))

    def __add__(self, other):
        return Cells(self.number + other.number)

    def make_order(self, n):
        rest = self.number
        while rest > n:
            print(n * self.cell)
            rest -= n
        print(rest * self.cell, '\n')


cells_1 = Cells(20)
cells_2 = Cells(23)

cells_res_add = cells_1.__add__(cells_2)
print(cells_res_add.number)

cells_res_sub = cells_1.__sub__(cells_2)
print(cells_res_sub.number)

cells_res_mul = cells_1.__mul__(cells_2)
print(cells_res_mul.number)

cells_res_div = cells_1.__truediv__(cells_2)
print(cells_res_div.number)

cells_1.make_order(7)
cells_2.make_order(6)
