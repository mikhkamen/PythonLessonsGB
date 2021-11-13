my_list = list(input('Введите список элементов через пробел, в конце нажмите "Enter": ').split())
i = 0
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print('Результат:\n', *my_list)
print(*my_list)
