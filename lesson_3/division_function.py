def division(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print('На ноль делить нельзя !\n'
              'Будет выведен результат деления на 10\n')
        res = a / 10
        return res

x, y = float(input('Введите делимое: \n')), float(input('Введите делитель: \n'))
print(f'Результат деления делимого на делитель равен {division(x, y)}')

