from itertools import count


def iter(b):
    iter = count(1)
    for el in iter:
        if el <= b:
            yield el
        else:
            break


n = int(input('Введите число, факториал которого нужно вычислить: \n'))
fact = 1
for it in iter(n):
    fact *= it
print(f'Факториал числа {n} равен {fact}')
