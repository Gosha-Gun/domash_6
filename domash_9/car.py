class car:
    def __init__(self,color ,name ,speed= 0, is_police= False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Вы начали движение")

    def stop(self):
        self.speed = 0
        print("вы остановились")

    def turn(self,direction= None):
        if direction == None:
            print("Вы повернули в неизвестном направлении")
        else:
            print(f"Вы повернули {direction}")
        self.speed /= 1.5

    def show_speed(self):
        print(f"Ваша текущая скорость: {self.speed}")

class TownCar(car):
    def show_speed(self):
        if self.speed > 60:
            print("Пожалуйста снизте скорость")
        print(f"Ваша текущая скорость: {self.speed}")

class WorkCar(car):
    def show_speed(self):
        if self.speed > 40:
            print("Пожалуйста снизте скорость")
        print(f"Ваша текущая скорость: {self.speed}")


class SportCar(car):
    pass

class PoliceCar(car):
    pass



marusia = SportCar("Red","Marusia",200,True)

marusia.go()
marusia.show_speed()
marusia.turn("Направо")
marusia.show_speed()

retro = TownCar("Green","retro",100,)

retro.show_speed()
retro.turn()
retro.turn("Назад")
retro.show_speed()