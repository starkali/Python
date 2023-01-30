#Inheritance
class Car:
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed):
        # Этот метод отвечает за инициализацию экземпляров класса после их создания.
        # Инициализация — приведение цифрового устройства или его программы в состояние готовности к использованию.
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print('Car is created')
        
    def drive(self, city):
        print(self.name + ' is driving to ' + city)
        
    def change_color(self, new_color):
        self.color = new_color

class Truck(Car):
    def __init__(self, name, color, year, is_crashed):
        Car.__init__(self, name, color, year, is_crashed)
