import time


class Car:
    # создаем атрибуты класса
    def __init__(self, name: str, color: str, speed: int, is_police=False, perm_speed=40):
        self.is_police = is_police
        self.direction = {'l': 'налево', 'r': 'направо'}
        self.name = name
        self.color = color
        self.speed = speed
        self.engine = False
        self.perm_speed = perm_speed
        self.is_police = is_police

        # создаем методы класса
    @staticmethod
    def start():
        k = input("Чтобы завести двигатель, введите 'on'\n")
        if k == 'on':
            self.engine = True
            print("др-др-др-др-р-р.... завелся !")
        return self.engine

    @staticmethod
    def go():
        if self.engine:
            self.speed = int(input('С какой скоростью поедем? \n'))
            if self.speed > self.max_speed:
                self.speed = self.max_speed
                print(f'Так быстро наш {self.color} {self.name} не умеет.'
                      f' Поедем {self.max_speed}. Едем прямо.')
        else:
            print('С выключенным двигателем мы никуда не поедем!')
            self.start()

    @staticmethod
    def stop(self):
        self.speed = 0
        print('Стоп, приехали.')

    @staticmethod
    def turn(self):
        print(f'Наш {self.color} {self.name} повернул {self.direction.get(k)}')

    def show_speed(self):
        print(f'Наш {self.color} {self.name} движется со скоростью {self.speed} км в час')
        if self.speed > self.perm_speed:
            print('Вы превысили разрешенную скорость!')

    def siren(self, is_police):
        if self.is_police:
            while self.speed < self.perm_speed:
                time.sleep(5)
                print(f'Что мы плетемся еле-еле? Прибавь скорости.\n')
                n = input()
                if n == 'y':
                    self.speed += 50
                    self.show_speed()
            time.sleep(6)
            print('Включи сирену, задолбали эти крики о превышении скорости.')
            l = input()
            if l == 'y':
                print('звук сирены: уау-уау-уау')
                self.perm_speed = self.speed


class TownCar(Car):
    def __init__(self, name: str, color: str, max_speed: int, speed=0, perm_speed=60):
        super().__init__(name, color, speed)
        self.max_speed = max_speed
        self.perm_speed = perm_speed
        self.speed = speed

    def show_speed(self):
        if self.speed == 0:
            print(f"Наш {self.color} {self.name} стоит на месте. Может, прибавишь газу?\n")
            self.go()
        elif self.speed > self.perm_speed:
            print(f'Наша скорость - {self.speed} км в час')
            print(f'Это больше разрешенной скорости для {str(type(self))[17:-2]} {self.perm_speed} км/час.\n'
                  'Нас оштрафуют!!')
            n = input("Снизить скорость?  'y' - да, 'Enter' - нет")
            if n == 'y':
                self.speed = self.perm_speed
                self.show_speed()
            else:
                print('Ну, как хочешь, деньги-то твои...')
                print(f'Наш {self.color} {self.name} движется со скоростью {self.speed} км в час')
        else:
            print(f'Наш {self.color} {self.name} движется со скоростью {self.speed}')


class WorkCar(Car):
    def __init__(self, name: str, color: str, speed=0, max_speed=80, perm_speed=40):
        super().__init__(name, color, speed)
        self.max_speed = max_speed
        self.perm_speed = perm_speed
        self.speed = speed

    def show_speed(self):
        if self.speed == 0:
            print(f"Наш {self.color} {self.name} стоит на месте. Может, прибавишь газу?\n")
            self.go()
        elif self.speed > self.perm_speed:
            print(f'Наша скорость - {self.speed} км в час')
            print(f'Это больше разрешенной скорости для {str(type(self))[17:-2]} {self.perm_speed} км/час.\n'
                  'Нас оштрафуют!!')
            n = input("Снизить скорость?  'y' - да, 'Enter' - нет")
            if n == 'y':
                self.speed = self.perm_speed
                self.show_speed()
            else:
                print('Ну, как хочешь, деньги-то твои...')
                print(f'Наш {self.color} {self.name} движется со скоростью {self.speed} км в час')
        else:
            print(f'Наш {self.color} {self.name} движется со скоростью {self.speed}')


class SportCar(Car):
    def __init__(self, name: str, color: str, max_speed: int, speed=0, perm_speed=100):
        super().__init__(name, color, speed)
        self.max_speed = max_speed
        self.speed = speed
        self.perm_speed = perm_speed

    def show_speed(self):
        print(f'Наш красавчик {self.color} {self.name} едет со скоростью {self.speed}')
        if self.speed > self.perm_speed:
            print('Многовато, конечно, но нам ведь наплевать? Максимум - оштрафуют.\n'
                  'Если догонят...\n'
                  f'  Или лучше сбрось хотя бы до {self.perm_speed} Меня мутит от страха.')
            n = input(f"Прошу тебя...  'y' - да,'Enter' - нет")
            if n == 'y':
                self.speed = self.perm_speed
                self.show_speed()
                time.sleep(3)
                print('Спасибо...')
            else:
                print('Господи, спаси и помилуй!')
                print(f'Наш {self.color} {self.name} движется со скоростью {self.speed} км в час')


class PoliceCar(Car):
    def __init__(self, name,  max_speed, __color='police', speed=0, perm_speed=60):
        super().__init__(name, __color, speed)
        self.max_speed = max_speed
        self.speed = speed
        self.is_police = True
        self.perm_speed = perm_speed


print('Выберите авто.\n1 - легковая машина\n'
      '2 - грузовик\n3 - спорткар (скоростная машина для богатых,\n'
      '    которым плевать на штрафы)\n'
      '4 - полицейская машина (если включить сирену, предупреждений\n'
      '    о превышении скорости не будет')
a = int(input())
color = 'color'
s_obj = Car('name', 'color', 0)
name = input('Марка машины?\n')
if a != 4:
    color = input('Цвет машины?\n')
max_speed = int(input('Максимальная скорость машины?\n'))
if a == 1:
    s_obj = town_car = TownCar(name, color, max_speed)
    if town_car.max_speed > 180:
        print(f'Так быстро этот тип машин не ездит. Пусть будет 180 км/час')
    town_car.max_speed = 180
elif a == 2:
    s_obj = work_car = WorkCar(name, color, max_speed)
    if work_car.max_speed > 90:
        print(f'Так быстро этот тип машин не ездит. Пусть будет 90 км/час')
    work_car.max_speed = 90
elif a == 3:
    s_obj = sport_car = SportCar(name, color, max_speed)
    if sport_car.max_speed > 290:
        print(f'Так быстро даже этот тип машин не ездит.\n '
              f'Пусть будет 290 км/час - чуть медленнее полицейских машин')
    sport_car.max_speed = 290

elif a == 4:
    color = 'police'
    max_speed = 300
    s_obj = police_car = PoliceCar(name, max_speed)

print(f'{str(type(s_obj))[17:-2]} {s_obj.color} {s_obj.name},\n'
      f' скорость до {s_obj.max_speed} км/час - хороший выбор.\n'
      f'Прокатимся?')
print(s_obj.is_police)

s_obj.start()
s_obj.go()
s_obj.show_speed()
if s_obj.is_police:
    s_obj.siren(s_obj)
while s_obj.speed > 0:
    time.sleep(5)
    k = input("Повернем? 'l' - налево, 'r' - направо\n"
              "'q' - остановка и конец программы\n")
    if k == 'q':
        s_obj.stop(s_obj)
        quit()
    s_obj.turn(s_obj)
    s_obj.show_speed()
    s_obj.siren(s_obj)






