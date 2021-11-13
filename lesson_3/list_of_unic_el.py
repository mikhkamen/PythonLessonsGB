from itertools import count

iterator = (count(7, 1))

print('\nНажимайте "Enter" для вывода следующего значения итератора.\n'
      'Когда надоест, для выхода нажмите любую клавишу и после нее "Enter')

k = ''
p = []
while k == '':
    f = iterator
    p.append(next(f))
    print(*p)
    k = input()
quit()
