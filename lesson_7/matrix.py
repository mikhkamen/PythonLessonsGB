class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        m_str = ''
        for i in range(len(self.matrix)):
            m_str = m_str + '  '.join(map(str, self.matrix[i])) + '\n'
        return m_str

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        for m in range(len(self.matrix)):
            for n in range(len(self.matrix[m])):
                self.matrix[m][n] = self.matrix[m][n] + other.matrix[m][n]
        return Matrix(self.matrix)


a = Matrix([[50, 80, 45], [15, 71, 20]])
b = Matrix([[20, 10, 40], [45, 50, 100]])
print(f'Матрица a:\n{a.__str__()}\nМатрица b:\n{ b.__str__()}\n'
      f'Их сумма:\n{a.__add__(b)}')



