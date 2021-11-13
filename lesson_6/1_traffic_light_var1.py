import time


class TrafficLight:
    def __init__(self):
        self.__color = {'red': int(), 'yellow': int(), 'green': int()}

    @staticmethod
    def running(__color):
        for key in __color.keys():
            print(key)
            time.sleep(__color.get(key))


while True:
    TrafficLight.running({'red': 7, 'yellow': 2, 'green': 5})
