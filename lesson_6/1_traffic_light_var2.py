import time


class TrafficLight:
    def __init__(self):
        self.__color = {'red': int(), 'yellow': int(), 'green': int()}

    def running(self, __color):
        for key in __color.keys():
            print(key)
            time.sleep(__color.get(key))


trafficLight = TrafficLight()
while True:
    trafficLight.running({'red': 7, 'yellow': 2, 'green': 5})
