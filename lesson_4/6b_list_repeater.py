from itertools import cycle

a = list(input('Введите строку: \n'))
print('Сколько раз повторить введенную строку? \n')
k = int(input())
l = 0
m = 1
for el in cycle(a):
    print(el, end='')
    l += 1
    if l < k * len(a):
        if l == m * len(a) and m < k:
            print('\n', end='')
            m += 1
    else:
        quit()
