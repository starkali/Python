# # Inheritance
#
# class Car:
#
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         # Этот метод отвечает за инициализацию экземпляров класса после их создания.
#         # Инициализация — приведение цифрового устройства или его программы в состояние готовности к использованию.
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         print('Car is created')
#
#     def drive(self, city):
#         print(self.name + ' is driving to ' + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#         print('Color is changed to ' + new_color)
#
#
# class Truck(Car):
#
#     wheels_number = 6
#
#     def __init__(self, name, color, year, is_crashed):
#         Car.__init__(self, name, color, year, is_crashed)
#         print('Truck is created')
#
#     def drive(self, city):
#         print('Truck ' + self.name + ' is driving to ' + city)
#
#     def load_cargo(self, weight):
#         print('The cargo is loaded. Weight is ' + str(weight) + ' kg')
#
#
# man_truck = Truck('Man', 'White', 2015, False)
#
# man_truck.drive('New York')
# print(man_truck.wheels_number)
# print(man_truck.color)
# man_truck.change_color('Red')
# print(man_truck.color)
# man_truck.load_cargo(2000)


# Polymorphism


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Class successor must implement this method')

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying woof')

class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying meow')


class Mouse(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying pee-pee-pee')


class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying nothing')


spike = Dog('Spike')
tom = Cat('Tom')
jerry = Mouse('Jerry')

pet_list = [spike, tom, jerry]

for pet in pet_list:
    pet.speak()

def pet_voice(pet):
    pet.speak()

pet_voice(spike)
pet_voice(tom)
pet_voice(jerry)

freddy = Fish('Freddy')
pet_voice(freddy)