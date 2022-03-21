class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        print("Начало отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Начало записи")

class Pencil(Stationery):
    def draw(self):
        print("Начало черчения")

class Handle(Stationery):
    def draw(self):
        print("Начало рисования")


pens = Pen("Ручка")
pens.draw()

pels = Pencil("Карандаш")
pels.draw()

hads = Handle("Маркер")
hads.draw()