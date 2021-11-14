class Date:
    def __init__(self, day_month_year: str):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        return list(map(int, day_month_year.split('-')))

    def __str__(self):
        return f'{date.extract(self.day_month_year)}'


def is_valid(day, month, year):
    if 31 < day < 0:
        return f'Неверно указан день'
    elif 0 > month > 12:
        return f'Неверно указан месяц'
    elif year < 0:
        return f'Неверно указан год.'
    elif month in (4, 6, 9, 11) and day > 30:
        return f'В месяце с номером {month} не может быть более 30 дней'
    elif not((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month == 2 and day > 28:
        return f'В феврале невисокосного года не может быть более 28 дней'
    elif month == 2 and day > 29:
        return f'Даже в високосном году в феврале не может быть более 29 дней'

    return f'Вы ввели валидную дату'


date_for_example = '01-12-1960'
date = Date(date_for_example)
date_lst = date.extract(date_for_example)
print(f'Введенная дата {date_for_example} в формате [д, м, гггг]: {date_lst}')
print(date.__str__()[1:-1])
print(is_valid(date_lst[0], date_lst[1], date_lst[2]))
print()
print(is_valid(31, 4, 2021))   # 31 апреля
print(is_valid(29, 2, 2021))   # 29 февраля невисокосного года
print(is_valid(29, 2, 2020))   # 29 февраля високосного года
print(is_valid(30, 2, 2020))   # 30 февраля
print(is_valid(29, 2, 1900))   # 1900 - невисокосный год
print(is_valid(29, 2, 2000))   # 2000 - високосный год
