my_list = [1, None, 4.5, {None, "Это я, Михаил"}, False, (4, 'это правда', True),
           'не люблю печатать', {'name': 'Michael', 'progress': 'high'}, [str(56), 56, 56.0]]
for i in range(len(my_list)):
    print(f'{my_list[i]} относится к типу{str(type(my_list[i]))[6:-1]}')

