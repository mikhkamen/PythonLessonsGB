def number_days(start, end):
    number = 1
    while start < end:
        start += start * 0.1
        number += 1
    return number


a = int(input('Введите начальный результат: '))
b = int(input('Введите конечный результат: '))
print(f'Результат будет достигнут на {number_days(a, b)}-й день')
