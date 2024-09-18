class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_pover = __engine_power
        self.__color = __color

    def get_model(self):
        print('Модель:', self.__model)

    def get_horsepower(self):
        print('Мощность двигателя:', self.__engine_pover)

    def get_color(self):
        print('Цвет:', self.__color)

    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print('Владелец:', self.owner)

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print('Нельзя сменить цвет на', new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('WHITE')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
