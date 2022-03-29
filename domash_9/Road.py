class Road:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width



    def mass(self,width_sm):
        out = self.__length*self.__width*25*width_sm // 1000
        print(f"{out} т")



big_Road = Road(5000,20)
big_Road.mass(5)


litle_Road = Road(1000,10)
litle_Road.mass(4)

amazing_Road = Road(15000,40)
amazing_Road.mass(10)