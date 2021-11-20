from datetime import datetime as dt
import pandas as pd


class MyError(Exception):
    def __init__(self, text):
        self.text = text


class Waybill:
    def __init__(self, date, name, count, price):
        self.name = name
        self.price = price
        self.date = date
        self.count = count

    def display_accept(self):
        total_price = int(self.count) * float(self.price)
        print(f'{self.date} поступило на склад {self.count} {self.name}  по цене {self.price}'
              f' на общую сумму {total_price}')

    def waybill(self):
        return f'{self.date},{self.name},{self.count},{float(self.price)},\n'


class Goods:
    def __init__(self, file_name):
        self.file_name = file_name
        self.df_g = pd.read_csv(self.file_name, header=0)

    def display_total_count(self):
        total_count = self.df_g['count'].sum()
        return f'{total_count}'

    def display_total_sum(self):
        self.df_g['total'] = self.df_g['count'] * self.df_g['price']
        total_sum = self.df_g['total'].sum()
        return f'{total_sum}'


class Computers(Goods):
    def __init__(self, file_name):
        super().__init__(file_name)
        df_g = pd.read_csv(self.file_name, header=0)
        self.df_g = df_g.loc[df_g['name'] == 'computer']

    def display_total_count(self):
        super().display_total_count()
        return f'{super().display_total_count()}'


class Printers(Goods):
    def __init__(self, file_name):
        super().__init__(file_name)
        df_g = pd.read_csv(self.file_name, header=0)
        self.df_g = df_g.loc[df_g['name'] == 'printer']

    def display_total_count(self):
        super().display_total_count()
        return f'{super().display_total_count()}'


def valid_1_2(text):
    err = True
    while err:
        try:
            val = int(input(text + '\n'))
            if val not in (1, 2):
                raise MyError('Только 1 или 2!')
        except ValueError:
            err = True
            print("Вы ввели не число")
        except MyError:
            err = True
            print(MyError('Только 1 или 2!'))
        else:
            err = False
            return val


def extract_date():
    err = True
    while err:
        try:
            date = input('Введите дату в формате гггг-мм-дд\n')
            data = list(map(int, date.split('-')))
            if len(data) != 3:
                raise MyError('Неверный формат!')
            elif valid_date(data)[0]:
                raise MyError(valid_date(data)[1])
        except ValueError:
            err = True
            print("Только цифры!")
        except MyError:
            err = True
            print(f'{MyError(valid_date(data)[1])}')
        else:
            err = False
            return f'{data[0]}-{data[1]}-{data[2]}'


def valid_date(data):
    err = False
    while not err:
        day = data[2]
        month = data[1]
        year = data[0]
        if day > 31:
            err = True
            print(f'Неверно указан день')
            return err, f'Неверно указан день'
        elif month > 12:
            err = True
            return err, f'Неверно указан месяц'
        elif year < 0:
            err = True
            return err, f'Неверно указан год.'
        elif month in (4, 6, 9, 11) and day > 30:
            err = True
            return err, f'В месяце с номером {month} не может быть более 30 дней'
        elif not((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month == 2 and day > 28:
            err = True
            return err, f'В феврале невисокосного года не может быть более 28 дней'
        elif month == 2 and day > 29:
            err = True
            return err, f'Даже в високосном году в феврале не может быть более 29 дней'
        else:
            err = False
            return err, f'{year}-{month}-{day}'


reg = 0
typ = 0
job = True
while job:
    reg = valid_1_2('Накладная - 1, отчет - 2')
    if reg == 1:
        cont = True
        while cont:
            typ = valid_1_2('computer - 1, printer - 2')
            if typ == 1:
                name = 'computer'
            else:
                name = 'printer'
            dat = input('Сегодня - 1, другая дата - "Enter"\n')
            if dat == '1':
                date = dt.now().date()
            else:
                # date = input('Введите дату в формате гггг-мм-дд\n')
                date = extract_date()
            wb = Waybill(date, name, count=input('count?\n'), price=input('price?\n'))
            with open('goods.csv', 'a+') as f:
                f.write(wb.waybill())
            wb.display_accept()
            c = input('Continue? y - YES\n')
            if c != 'y':
                cont = False
    else:
        goods = Goods('goods.csv')
        print(f'На складе находится {goods.display_total_count()} единиц оргтехники')
        print(f'Общая стоимость находящейся на складе оргтехники {goods.display_total_sum()} руб.')
        comp = Computers('goods.csv')
        printer = Printers('goods.csv')
        print(f'На складе находится {comp.display_total_count()} компьютеров')
        print(f'Общая стоимость находящихся на складе компьютеров {comp.display_total_sum()} руб')
        print(f'На складе находится {printer.display_total_count()} принтеров')
        print(f'Общая стоимость находящихся на складе принтеров {printer.display_total_sum()} руб')
    n = input('Continue? y = YES, "Enter" - закрыть программу - ')
    if n != 'y':
        df = pd.read_csv('goods.csv', header=0)
        df = df.sort_values('date')
        df.to_csv('goods.csv', index=False)
        job = False
quit()


