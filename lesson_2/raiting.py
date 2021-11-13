my_raiting = [8, 6, 5, 5, 3, 1]
my_raiting.append(int(input('Введите число: ')))
for i in range(len(my_raiting)-1, 0, -1):
    if my_raiting[i] > my_raiting[i - 1]:
        my_raiting[i-1], my_raiting[i] = my_raiting[i], my_raiting[i-1]
print(*my_raiting)

