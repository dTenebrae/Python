# Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).  А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
# WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который
# должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
# к атрибутам, выведите результат. Выполните вызов методов и также
# покажите результат.


class Car:
    speed = 0
    color = ''
    is_police = False

    def go(self):
        print('Driving...')

    def stop(self):
        print('Stopping...')

    def turn(self, direction):
        print('Turning', direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Speed limit is 60! Your speed is', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Speed limit is 40! Your speed is', self.speed)


class PoliceCar(Car):
    pass


towncar1 = TownCar()
towncar1.speed = 70
towncar1.color = 'blue'
towncar1.go()
towncar1.turn('left')
towncar1.stop()
towncar1.show_speed()
print(f'Current speed: {towncar1.speed}, Color: {towncar1.color}\n')

workcar1 = WorkCar()
workcar1.speed = 60
workcar1.color = 'red'
workcar1.go()
workcar1.turn('left')
workcar1.stop()
workcar1.show_speed()
print(f'Current speed: {workcar1.speed}, Color: {workcar1.color}\n')

policecar1 = PoliceCar()
policecar1.speed = 100
policecar1.color = 'black'
policecar1.is_police = True
policecar1.go()
policecar1.turn('left')
policecar1.stop()
policecar1.show_speed()
print(f'Current speed: {policecar1.speed}, Color: {policecar1.color}, '
      f'Is it Police: {policecar1.is_police}\n')

sportcar1 = SportCar()
sportcar1.speed = 120
sportcar1.color = 'orange'
sportcar1.go()
sportcar1.turn('right')
sportcar1.stop()
sportcar1.show_speed()
print(f'Current speed: {sportcar1.speed}, Color: {sportcar1.color}\n')
