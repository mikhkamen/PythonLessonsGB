class Road:
    def __init__(self):
        self._length = float()              # Длина дороги в километрах
        self._width = float()               # Ширина дороги в метрах
        self._thickness = int()             # Толщина асфальта в сантиметрах

    def mass(self, _length, _width, _thickness):
        return _length * _width * _thickness * 25


road = Road()
print(f'Требуется {road.mass(20, 7.5, 6)} тонн асфальта')
