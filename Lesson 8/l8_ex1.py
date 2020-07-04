from random import sample


class Player:
    """Class for players, on initialization a card for each player is created"""

    def __init__(self, name):
        self.name = name
        self.card = Card()


class Card:
    """Class for players card, has the following functions:
    __init to create a card
    c_print to print card in terminal
    cross to cross out number
    num_count to calculate gow many numbers are left"""

    def __init__(self):
        self.card = [0 for i in range(0, 27)]
        numbers = sample(range(1, 91), 16)
        for i in range(0, 3):
            numbers[i*5:(i+1)*5] = sorted(numbers[i*5:(i+1)*5])
        k = 0
        for i in range(0, 3):
            pos = sorted(sample(range(i*9, (i+1)*9-1), 5))
            for j in pos:
                self.card[j] = int(numbers[k])
                k += 1

    def c_print(self):
        i = 0
        for j in self.card:
            if j == 0:
                print('  ', end='')
            elif j < 10:
                print(' ', j, end='')
            elif j == 99:
                print('--', end='')
            else:
                print(j, end='')
            print(' ', end='')
            i += 1
            if i == 8 or i == 17:
                print('\n', end='')
        print('\n----------------------------')

    def cross(self, num):
        if num in self.card:
            self.card[self.card.index(num)] = 99

    def num_count(self):
        nums = 0
        for el in self.card:
            if 0 < el < 91:
                nums += 1
        return nums


class Game:
    """Class for game operation.
    game_start main function that launches and operates the game
    check_gen - generator, that returns random unique numbers for game
    game_end function finishes the game, is called if someone loses"""

    def check_gen(self):
        for el in sample(range(1, 91),90):
            yield el

    def game_start(self, pl1, pl2):
        turn = 1
        print('LET THE BATTLE BEGIN!!!')
        for num in Game.check_gen(self):
            print(f'\nit is {turn} turn, {90-turn} numbers are left')
            print(f'------{pl1.name}\'s card is------')
            pl1.card.c_print()
            print(f'-------{pl2.name}\'s card is--------')
            pl2.card.c_print()
            pl_ans = input(f'do you want to cross number {num} (y/n)?\n')
            if pl_ans == 'y' and num in pl1.card.card:
                pl1.card.cross(num)
            elif pl_ans == 'n' and num not in pl1.card.card:
                pass
            else:
                Game.game_end(self, pl2)
            pl2.card.cross(num)
            if pl1.card.num_count() == 0:
                Game.game_end(self, pl1)
            if pl2.card.num_count() == 0:
                Game.game_end(self, pl2)
            turn += 1

    def game_end(self, player):
        print(f'{player.name} has won, the game is over')
        exit()


"""Main code"""
me = Player('Nikita')
pc = Player('Mac')
g = Game()
g.game_start(me, pc)



