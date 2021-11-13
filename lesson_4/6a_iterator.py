from itertools import count

k = int(input('Введите число, с которого начнется последовательность: \n'))
print('Нажимайте "Enter" для вывода очередного элемента последовательности. \n'
      'Когда надоест, нажмите любую клавишу и после нее "Enter"')

my_iter = count(k)
for el in my_iter:
    s = input()
    if s != '':
        quit()
    print(el, end='')
