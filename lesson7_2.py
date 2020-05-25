# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и
# рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих
# методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.


from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, name=None):
        self.name = name

    @abstractmethod
    def material(self):
        pass


class Coat(Clothes):
    def __init__(self, size, name=None):
        super().__init__(name)
        self.V = size

    @property
    def material(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height, name=None):
        super().__init__(name)
        self.H = height

    @property
    def material(self):
        return self.H * 2 + 0.3


suit = Suit(5)
print(suit.material)
coat = Coat(10)
print(f'{coat.material:.2f}')
