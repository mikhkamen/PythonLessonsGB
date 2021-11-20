class MyError(Exception):
    def __init__(self, text):
        self.text = text


# Пример:
try:
    n = int(input("Введите делимое: \n"))
    m = int(input('Введите делитель: \n'))
    l = n / m
    if m == 1:
        raise MyError("На единицу  делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except MyError:
    print(MyError)
else:
    print(l)
