line = 'line'
list_line = []
inp = True
file_name = input('Введите имя файла без расширения. Если файл не существует, он будет создан\n')
print('Введите текст построчно. Перевод строки -"Enter".\n'
      'Для окончания ввода нажмите "Enter"\n')
file_name = file_name + '.txt'
while inp:
    line = input()
    if line != '':
        line += '\n'
        list_line.append(line)
    else:
        par = input('Если вы хотите записать в пустой файл, нажмите "W" \n'
                    'Если вы хотите добавить текст к уже существующему, нажмите "a"\n')
        mf = open(file_name, par, encoding='UTF-8')
        for line in list_line:
            mf.writelines(line)
        mf.close()
        inp = False
print(f'Текст записан в файл {file_name}')
