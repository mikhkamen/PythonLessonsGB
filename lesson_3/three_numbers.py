def my_func(a, b, c):
    summ = a + b + c
    summ -= min(a, b, c)
    return summ


x, y, z = float(input('Первое число?\n')),  float(input('Второе число?\n')), float(input('Первое число?\n'))
print(my_func(x, y, z))
