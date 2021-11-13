from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param, name):
        self.param = param
        self.name = name
        
    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.expense)


class Coat(Clothes):
    def __init__(self, param, name='пальто'):
        super().__init__(name, param)
        self.param = param
        self.name = 'пальто'

    @property
    def expense(self):
        return self.param / 6.5 + 0.5

    def __str__(self):
        return str(self.expense)


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param, name='костюм')
        self.param = param
        self.name = 'костюм'

    @property
    def expense(self):
        return self.param * 2 + 0.3

    def __str__(self):
        return str(self.expense)


a = Coat(52)
b = Suit(1.80)
for char in (a, b):
    print(f'Расход ткани на {char.name} {char.param} '
          f'размера - {char.__str__()} метра')
print(a.expense)
print(b.expense)



