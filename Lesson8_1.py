# == Лото ==
#
# Правила игры в лото.
#
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
#
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
#
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5
# случайных цифр, расположенных по возрастанию. Все цифры в карточке уникальны.
# Пример карточки:
#
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
#
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
#
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
#
# Пример одного хода:
#
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
#
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html


from random import randrange, sample


class Players:
    def __init__(self, name='CPU'):
        self.name = name
        self.won = False
        self.cpu = True if self.name == 'CPU' else False
        self.__left = 15
        nums = list(sample(range(1, 91), 15))
        self.numbers = [sorted(nums[_:_ + 5]) for _ in range(0, 15, 5)]
        for lst in self.numbers:
            for _ in range(4):
                lst.insert(randrange(len(lst) + 1), '  ')

    @property
    def show_card(self):
        if self.cpu:
            header = '-- Карточка компьютера ---\n'
        else:
            header = '------ Ваша карточка -----\n'
        return header + ' '.join(
            [str(num) if isinstance(num, str) or num > 9 else (' ' + str(num))
             for num in self.numbers[0]]) + '\n' + ' '.join(
            [str(num) if isinstance(num, str) or num > 9 else (' ' + str(num))
             for num in self.numbers[1]]) + '\n' + ' '.join(
            [str(num) if isinstance(num, str) or num > 9 else (' ' + str(num))
             for num in self.numbers[2]]) + '\n' + '-' * 26

    def check_list(self, barrel, y_flag):
        change_flag = False
        for i, part in enumerate(self.numbers):
            if barrel in part:
                if y_flag:
                    self.numbers[i] = [num if num != barrel else chr(215) * 2
                                       for num in part]
                change_flag = True
                self.__left -= 1
        if self.__left == 0:
            self.won = True
        return change_flag


class Game:
    def __init__(self):
        self.barrel_list = [num for num in range(1, 91)]

    @property
    def get_barrel(self):
        while self.barrel_list:
            yield self.barrel_list.pop(randrange(len(self.barrel_list)))

    @property
    def barrels_left(self):
        return len(self.barrel_list)


game_lost = False
player1 = Players('Vasiliy')
player2 = Players()
new_game = Game()
for barrel in new_game.get_barrel:
    print(f'\nНовый бочонок: {barrel} (осталось {new_game.barrels_left})\n')
    print(player1.show_card)
    print(player2.show_card)
    for player in [player1, player2]:
        if player.cpu:
            player.check_list(barrel, True)
        else:
            while True:
                pressed_key = input('\nЗачеркнуть цифру? (y/n)')
                if pressed_key not in ('y', 'n'):
                    print('Некорректный ввод')
                else:
                    break
            if pressed_key == 'y':
                if not (player.check_list(barrel, True)):
                    game_lost = True
            elif pressed_key == 'n' and player.check_list(barrel, False):
                game_lost = True
        if game_lost:
            print('Вы проиграли')
            exit(0)
        if player.won:
            print(f'{player.name} победил!')
            exit(0)
