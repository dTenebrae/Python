# Реализовать класс Stationery (канцелярская принадлежность). Определить
# в нем атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.


class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисую ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисую карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисую маркером')


smth = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

smth.draw()
pen.draw()
pencil.draw()
handle.draw()
