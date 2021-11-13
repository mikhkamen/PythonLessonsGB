proc = int(input('выручка, $: '))
costs = int(input('издержки, $: '))
if proc < costs:
    print(f'Убытки фирмы составили ${costs - proc}')
elif proc == costs:
    print('Отчетный период закончился с нулевым результатом.')
else:
    print(f'Рентабельность за период составила {round((proc - costs)*100 / proc, 2)} процентов')
    ppp = (proc - costs) / int(input('Какова численность персонала? '))
    print(f'Прибыль на одного человека - примерно ${round(ppp)}.')
