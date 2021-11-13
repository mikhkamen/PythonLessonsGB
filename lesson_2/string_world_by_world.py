my_line = input('Введите строку: ').split()
for i in range(len(my_line)):
    my_line[i] = str(my_line[i])[:10]  # Ограничение длины строки
    print(f'{i + 1}.{my_line[i]}')  # Вывод строк с нумерацией
