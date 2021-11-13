class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = 'Sergey'
        self.surname = 'Ivanoff'
        self.position = 'Director'
        self._income = {"wage": int(), "bonus": int()}

    def worker(self, name, surname, position, _income):
        return name, surname, position, _income


class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)
        self.name = 'Sergey'
        self.surname = 'Ivanoff'
        self.position = 'Director'
        self._income = {"wage": 55000, "bonus": 25000}

    def get_full_name(self, name, surname):
        return (name + ' ' + surname)

    def get_total_income(self, _income):
        return _income['wage'] + _income['bonus']


worker_1 = Worker('Sergey', 'Ivanoff', 'Director', {'wage': 55000, 'bonus': 25000})
print(worker_1.name)
print(worker_1.position)
print(worker_1.worker('Sergey', 'Ivanoff', 'Director', {'wage': 55000, 'bonus': 25000}))
worker_2 = Worker('Ivan', 'Petroff', 'Street Cleaner', {'wage': 12500, 'bonus': 0})
print(worker_2.worker('Ivan', 'Petroff', 'Street Cleaner', {'wage': 12500, 'bonus': 0}))

director = Position('Sergey', 'Ivanoff', 'Director', {'wage': 55000, 'bonus': 25000})
street_cleaner = Position('Ivan', 'Petroff', 'Street Cleaner', {'wage': 12500, 'bonus': 0})
si = director.get_full_name('Sergey', 'Ivanoff')
salary_si = director.get_total_income({'wage': 55000, 'bonus': 25000})
ip = street_cleaner.get_full_name('Ivan', 'Petroff')
salary_ip = street_cleaner.get_total_income({'wage': 12500, 'bonus': 0})
print(f'Директор {si} получил зарплату {salary_si},'
      f' а дворник {ip} - {salary_ip} (премию ему не дали).\n')
print('Доступ к методу родительского класса: ')
lst_director = director.worker('Sergey', 'Ivanoff', 'Director', {'wage': 55000, 'bonus': 25000})
print(lst_director)
