numbers = list(map(int, input('Введите число: ')))
i, number_max = 1, numbers[0]
while i < len(numbers):
    if numbers[i] > number_max:
        number_max = numbers[i]
    i += 1
print('Самая большая цифра -', number_max)
