'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('car started')

    def stop(self):
        print('car stopped')

    def turn(self):
        print('car turned')

    def show_speed(self):
        print('the speed is: ', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print('the speed is: ', self.speed)
        else:
            print('the speed is too high')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print('the speed is: ', self.speed)
        else:
            print('the speed is too high')


class PoliceCar(Car):
    pass


my_car = TownCar('100', 'black', 'mercedes', '0')
print('name:', my_car.name)
my_car.go()
my_car.turn()
my_car.show_speed()

other_car = WorkCar('30', 'white', 'truck', '0')
print('\ncolor:', other_car.color)
other_car.show_speed()