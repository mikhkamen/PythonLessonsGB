class MyError(Exception):
    def __init__(self, number):
        self.number = number

    def is_number(self, number):
        is_number = True
        while is_number:
            try:
                if '.' in number:
                    self.number = float(number)
                else:
                    self.number = int(number)
                return self.number
            except ValueError:
                if self.number != 'stop':
                    print(f"Недопустимое значение. \"{self}\" - это строка")
                is_number = False


print('Напечатайте элемент списка."Enter" - ввод.\n'
      'Введите"stop" для окончания и вывода на экран.\n')
my_list = []
item = ''
while item != 'stop':
    item = input()
    my_error = MyError(item)
    if my_error.is_number(item) is not None:
        my_list.append(my_error.is_number(item))
print(my_list)
