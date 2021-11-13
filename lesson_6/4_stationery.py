class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('pencil')

    def draw(self):
        print('Запуск отрисовки карандашом')


class Pen(Stationery):
    def __init__(self):
        super().__init__('pen')

    def draw(self):
        print('Запуск отрисовки ручкой')


class Handle(Stationery):
    def __init__(self):
        super().__init__('handle')

    def draw(self):
        print('Запуск отрисовки маркером')


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()

