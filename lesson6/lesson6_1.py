# Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный,
# желтый, зеленый. Продолжительность первого состояния (красный) составляет
# 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше
# усмотрение.  Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.


from time import sleep
from itertools import cycle


class ModificationError(Exception):
    pass


class TrafficLight:
    """class usage:
    main_delay - delay for red and green light in sec. Default is 7 sec.
    cycling_number - number of times lights switching. Default is 10 times"""
    __color = ['red', 'yellow', 'green', 'yellow']

    def __check_color(self, prev_color, current_color):
        if prev_color in ('red', 'yellow', 'green'):
            if prev_color in ('red', 'green') \
                    and current_color == 'yellow':
                return True
            elif prev_color == 'yellow' \
                    and current_color in ('red', 'green'):
                return True
        elif not prev_color \
                and current_color in ('red', 'yellow', 'green'):
            return True

    def running(self, main_delay=7, cycling_number=10):
        cycling_colors = cycle(self.__color)
        prev_color = ''
        try:
            for i in range(cycling_number):
                current_color = next(cycling_colors)
                if self.__check_color(prev_color, current_color):
                    print(current_color)
                    prev_color = current_color
                    if current_color == 'red':
                        sleep(main_delay)
                    elif current_color == 'yellow':
                        sleep(2)
                    elif current_color == 'green':
                        sleep(main_delay)
                else:
                    raise ModificationError('ModError:  '
                                            'Someone has modified lights...')
        except ModificationError as me:
            print(me)


new_light = TrafficLight()
new_light.running(cycling_number=10)
