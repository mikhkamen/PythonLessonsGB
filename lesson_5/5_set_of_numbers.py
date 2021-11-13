sum = 0
file_name = input('Укажите имя создаваемого файла без расширения: \n') + '.txt'
with open(file_name, 'w', encoding='UTF-8') as f:
    f.write(input('Введите числа через пробел. \nДля окончания ввода нажмите "Enter": \n'))
with open(file_name, 'r') as f:
    for n in f.read().split():
        sum += int(n)
    print(f'Сумма записанных в файл {file_name} числ равна {sum}')
