from functools import reduce
new_list = [i for i in range(100, 1001) if i % 2 == 0]
mult_all = reduce(lambda x, y: x * y, new_list)
print(new_list)
print(mult_all)
print('В этом числе', len(str(mult_all)), 'знаков.')
