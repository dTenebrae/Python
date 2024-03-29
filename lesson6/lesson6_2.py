# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для
# покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины
# полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, road_length, road_width):
        self._length = road_length
        self._width = road_width

    def asphalt_mass(self, asphalt_thickness, sq_m=25):
        return self._width * self._length * asphalt_thickness * sq_m


new_road = Road(5000, 20)
print(f'{new_road.asphalt_mass(5) // 1000} ton')
