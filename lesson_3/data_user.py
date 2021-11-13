def data_user(*args):
    print(f'{args[0]} {args[1]}, {args[2]}года рождения,'
          f' проживает в г.{args[3]}, email: {args[4]}, телефон {args[5]}')


data_user(input('Имя?\n'), input('Фамилия?\n'), input('Год рождения?\n'),
          input('Город?\n'), input('email?\n'), input('Телефон?\n'))
