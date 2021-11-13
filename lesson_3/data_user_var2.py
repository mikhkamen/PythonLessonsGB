def data_user(name='John', surname='surname',  year_birth='year of birthday',
              town='town', email='email', phone_numb='phone_number'):
    print(f'{name} {surname}, {year_birth} года рождения,'
          f' проживает в г.{town}, email: {email}, телефон {phone_numb}')


data_user(**{'name': input('Имя?\n'), 'surname': input('Фамилия?\n'),
             'year_birth': input('Год рождения?\n'), 'town': input('Город?\n'),
             'email': input('email?\n'), 'phone_numb': input('Телефон?\n')})
