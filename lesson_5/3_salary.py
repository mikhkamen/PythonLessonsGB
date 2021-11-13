less_then_20 = []
sum_salary = 0
n = 0
with open('3_salary.txt', encoding='UTF-8') as f:
    for line in f:
        if int(line.split()[1]) < 20000:
            less_then_20.append(line.split()[0])
        sum_salary += int(line.split()[1])
        n += 1

print(f'Общая сумма начисленной зарплаты составила {sum_salary} руб. \n'
      f'на {n} сотрудников, в среднем {round(sum_salary / n)} руб. на человека.\n')
print(f'Сотрудники', ','.join(less_then_20), 'получили меньше 20000 руб.')
