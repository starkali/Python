# class Car:
#     wheels_number = 4
#     def __init__(self, name, color, year, is_crashed): 
#         # Этот метод отвечает за инициализацию экземпляров класса после их создания | Инициализация — приведение цифрового устройства или его программы в состояние готовности к использованию.
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
        
#     def drive(self, city):
#         print(self.name + ' is driving to ' + city)
        
#     def change_color(self, new_color):
#         self.color = new_color
    
# opel_car = Car('Opel Tigra', 'Grey', '1999', True)
# opel_car.drive('London')
# mazda_car = Car('Mazda CX7', 'Black', 2014, False)
# mazda_car.drive('Paris')
# mazda_car.change_color('Yellow')
# print(mazda_car.color)
# print(opel_car.drive)
# print(opel_car.wheels_number)
# print(opel_car.name)
# print(opel_car.color)
# print(opel_car.year)
# print(opel_car.is_crashed)

class Circle:
    pi = 3.14
    
    def  __init__(self, radius=1):
        self.radius = radius
        self.circumference = 2 * self.pi * self.radius
        
    def get_area(self):
        return self.pi * (self.radius ** 2)
    
    # def get_circumference(self):
    #     return 2 * self.pi * self.radius
        
circle_1 = Circle(5)
print(circle_1.get_area())
print(circle_1.circumference)
# circle_2 = Circle(3)
# print(circle_2.get_area())
# print(circle_2.get_circumference())
# circle_3 = Circle(5)
# circle_area = circle_3.get_area()
# print(circle_area)
# print(circle_3.get_circumference())