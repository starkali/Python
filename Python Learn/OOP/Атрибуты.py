class Car:
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed): 
        # Этот метод отвечает за инициализацию экземпляров класса после их создания | Инициализация — приведение цифрового устройства или его программы в состояние готовности к использованию.
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        
mazda_car = Car(name='Mazda CX7', color='Black', year=2020, is_crashed=True)
print(mazda_car.name)
print(mazda_car.color)
print(mazda_car.year)
print(mazda_car.is_crashed)
print(mazda_car.wheels_number)
print('-'*20)
bmw_car = Car(name='BMW', color='White', year=2015, is_crashed=False)
print(bmw_car.name)
print(bmw_car.color)
print(bmw_car.year)
print(bmw_car.is_crashed)
print(bmw_car.wheels_number)
