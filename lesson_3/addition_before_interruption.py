def is_number(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def sum_list(s):
    a = []
    summa = 0
    long = True
    inp = True
    b = input()
    b_str = b.split()
    for i in range(len(b_str)):
            if is_number(b_str[i]) and inp:
                a.append(float(b_str[i]))
            elif b_str[i] == s and inp:
                summa = sum(a)
                long = False
                return [summa, long]
            else:
                a = []
                print('Ошибка. Можно вводить только числа, пробелы и символ прерывания.')
                break
    summa = sum(a)
    return [summa, long]


result = 0
k = input('  Введите любой символ или набор символов (кроме чисел),\n'
          'по которому вычисления прекратятся.\n'
          'Это могут быть буквы, специальные символы, \n'
          'слова или комбинации букв, цифр и символов. \n')
s_list = [0, True]
while s_list[1]:
    result += s_list[0]
    print(f'Промежуточный результат равен {result} \nПродолжайте.')
    s_list = sum_list(k)
result += s_list[0]
print(f'Общая сумма введенных чисел равна {result} \nСпасибо, до новых встреч!')
