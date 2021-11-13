from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, par, name):
        self.par = par
        self.name = name
        
    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.expense)


class Coat(Clothes):
    def __init__(self, par, name='пальто'):
        super().__init__(name, par)
        self.par = par

    @property
    def expense(self):
        return round(self.par / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, par):
        super().__init__(par, name='костюм')
        self.par = par

    @property
    def expense(self):
        return self.par * 2 + 0.3


coat = Coat(50)
suit = Suit(1.73)
for clothe in (coat, suit):
    print(f'Расход ткани на {clothe.name} {clothe.par} размера -',
          clothe.__str__(), 'метра')
print(coat.expense)
print(suit.expense)



