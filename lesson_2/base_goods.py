def entry_goods(m):
    product = {"название": input('Введите название товара: '), "цена": float(input('Введите цену товара: ')),
               "количество": int(input('Введите количество товара: ')),
               "ед": input('Введите единицу измерения товара: ')}
    item = (m, product)
    return item


def u_want():
    try:
        a = int(input('\nЕсли Вы хотите дополнить базу данных, введите 1 \n'
                      'Если вы хотите посмотреть базу данных, введите 2 \n'
                      'Если вы хотите посмотреть аналитику, введите 3 \n'
                      'Если вы хотите закончить работу,'' введите 4 \n'))
    except ValueError:
        a = 10
    if a == 1 or a == 2 or a == 3 or a == 4:
        return a
    else:
        print('Можно ввести только число от 1 до 4. Попробуйте еще раз.\n')
        u_want()



def add_goods_to_base(file_path, tup):
    f_obj = open(file_path, 'r+', encoding='utf-8')
    cont = f_obj.read()  # читаем содержимое из файла
    f_obj.close()
    if cont != '':
        cont = '[\n' + cont[2:-2] + ',\n' + str(tup) + '\n]'
    else:
        cont = '[\n' + str(tup) + '\n]'
    f_obj = open(file_path, 'w+', encoding='utf-8')
    f_obj.write(cont)
    f_obj.close()


def an_goods():
    with open('base.txt', 'r+', encoding='utf-8') as f_obj:
        contents = f_obj.read()
        try:
            contents = eval(contents)
        except SyntaxError:
            print('База данных пуста. Сначала введите хотя бы один элемент.')
        anal_goods = {
            'название': list(set([contents[i][1]['название'] for i in range(len(contents))])),
            'цена': list(set([contents[i][1]['цена'] for i in range(len(contents))])),
            'количество': list(set([contents[i][1]['количество'] for i in range(len(contents))])),
            'ед': list(set([contents[i][1]['ед'] for i in range(len(contents))])),
            }
        for key in anal_goods:
            print(f'"{key}":{anal_goods[key]}')


want = 0
content = ''
n = 1
while want != 4:
    want = u_want()
    with open('base.txt', 'r+', encoding='utf-8') as f:
        content = f.read()
        if content != '':
            products = eval(content)
            n = len(products) + 1
        else:
            want = input('\nПрежде чем работать с базой данных, нужно ввести хотя бы один элемент.\n'
                  'Если хотите продолжить,нажмите 1. \nЛюбая другая клавиша - окончание работы.\n')
            if want != '1':
                want = 4
            else:
                want = int(want)
    if want == 1:
        add_goods_to_base('base.txt', entry_goods(n))
        want = 0
    elif want == 2:
        print('[')
        print(str(',\n'.join(map(str, products))))
        print(']')
        want = 0
    elif want == 3:
        an_goods()
        want = 0
    elif want == 4:
        break
quit()
