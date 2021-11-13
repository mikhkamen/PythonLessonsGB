def neg_power(a, b):
    if b == 0:
        return 1
    if b == -1:
        return 1/a
    if b != 1:
        return (1/a) * neg_power(a, b + 1)


inp = False
while not inp:
    try:
        x = float(input('Первое число?\n'))
        inp = True
    except ValueError:
        print(f'Вы ввели не число.'
              f'Операция возведения в степень определена только для чисел.')

if x < 0:
    x = -x
    print(f'Нарушено условие задачи. Основание степени должно быть положительным.\n'
          f' Будет вычислено при x = {x}\n')
elif x == 0:
    print('Любая степень числа 0 равна 0, кроме равной 0.\n 0^0 = 1')

inp = False
while not inp:
    try:
        y = int(input('Второе число?\n'))
        inp = True
    except ValueError:
        print(f'Вы ввели не число.'
              f'Операция возведения в степень определена только для чисел.')

if x == 0:
    print('Повторяю: любая степень числа 0 равна 0, кроме равной 0.\n 0^0 = 1')
    quit()
if y > 0:
    y = -y
    print(f'Нарушено условие задачи. Степень числа должна быть отрицательной.\n'
          f' Будет вычислена  {y} степень числа {x}\n')

print(f'{x} в степени {y} равно {neg_power(x, y)}')
