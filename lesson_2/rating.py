my_raiting = 8, 6, 5, 5, 3, 1
my_raiting = list(my_raiting)
my_raiting.append(int(input('Введите число: \n')))
for i in range(len(my_raiting)-1, 0, -1):
    if my_raiting[i] > my_raiting[i-1]:
        my_raiting[i - 1], my_raiting[i] = my_raiting[i], my_raiting[i - 1]
my_raiting = tuple(my_raiting)
print('Новый рейтинг: ', f'{my_raiting}'[1:-1])

# i = len(my_raiting)-1
# my_raiting[i] > my_raiting[i-1] and i > 0:
#     my_raiting[i-1], my_raiting[i] = my_raiting[i], my_raiting[i-1]
#     i -= 1
# print(*my_raiting)
