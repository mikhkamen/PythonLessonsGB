import json

n = 0
sum_profit = 0
dict_firms = {}
with open('7_list_of_firms.txt', 'r', encoding='UTF-8') as f:
    firms = f.readlines()
for firm in firms:
    firm = firm.split()
    profit = int(firm[2]) - int(firm[3])
    if profit >= 0:
        n += 1
        sum_profit += profit
    dict_firms[firm[0]] = profit
with open("firms_profit.json", "w") as write_file:
    print('Это то, что мы записываем в файл в JSON-формате:')
    print(json.dumps([dict_firms, {'average_profit': round(sum_profit / n)}]), '\n')
    json.dump([dict_firms, {'average_profit': round(sum_profit / n)}], write_file)
with open("firms_profit.json", "r") as read_file:
    print('Это то, что мы получаем из JSON-файла (формата):')
    print(json.load(read_file))
