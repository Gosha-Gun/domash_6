from itertools import cycle
from time import sleep

class TrafficLight:
    __color = []

    def skate(self):
        print(TrafficLight.__color)

    def running(self):
        color_list = ["красный", "жёлтый", "зелёный", "жёлтый"]


        count = 0

        for c in cycle(color_list):

            TrafficLight.__color = c
            TrafficLight.skate(1)

            if c == "красный":
                sleep(7)
            if c == "жёлтый":
                sleep(2)
            if c == "зелёный":
                sleep(5)
            if count >= 15:
                break
            count += 1


light_controll = TrafficLight()
light_controll.running()