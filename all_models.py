import random


class Coin_flip:
    def __init__(self, players):
        self.players = players

    def join_(self, new_player, ctx, id):
        self.players.append(new_player)
        if len(self.players) == 2:
            return self.game_start(ctx, id)

    def game_start(self, ctx, id):
        return "В игре под id {}, победил {}".format(id, random.choice(self.players))


class Rock_paper_sizors:
    def __init__(self, players):
        self.game = {}
        self.players = players

    def join_(self, new_player, ctx, id):
        self.players.append(new_player)
        if len(self.players) == 2:
            return "Напишите $$choice + ваш id и выберите"

    def choice(self, who, what_choice):
        self.game[who] = what_choice
        if len(self.game.keys()) == 2:
            return self.winner()
        else:
            return -1

    def winner(self):
        players = []
        for i in self.game.keys():
            players.append((i, self.game[i]))

        print(players)

        first, senond = players

        if first[1] == 'rock' and senond[1] == 'rock':
            return '{} выбрал :rock: и {} выбрал :rock: \n НИЧЬЯ !!!!!!!!!'.format(first[0], senond[0])
        elif first[1] == 'rock' and senond[1] == 'scissors':
            return '{} выбрал :rock: и {} выбрал :scissors: \n ПОБЕДИЛ {} !!!!!!!!!'.format(first[0], senond[0], first[0])
        elif first[1] == 'rock' and senond[1] == 'paper':
            return '{} выбрал :rock: и {} выбрал ::roll_of_paper: \n ПОБЕДИЛ {} !!!!!!!!!'.format(first[0], senond[0], senond[0])

        elif first[1] == 'scissors' and senond[1] == 'rock':
            return '{} выбрал :scissors: и {} выбрал :rock: \n ПОБЕДИЛ {} !!!!!!!!!'.format(first[0], senond[0], senond[0])
        elif first[1] == 'scissors' and senond[1] == 'scissors':
            return '{} выбрал :scissors: и {} выбрал :scissors: \n НИЧЬЯ !!!!!!!!!'.format(first[0], senond[0])
        elif first[1] == 'scissors' and senond[1] == 'paper':
            return '{} выбрал :scissors: и {} выбрал ::roll_of_paper: \n ПОБЕДИЛ {} !!!!!!!!!'.format(first[0], senond[0], first[0])

        elif first[1] == 'paper' and senond[1] == 'rock':
            return '{} выбрал :roll_of_paper: и {} выбрал :rock: \n ПОБЕДИЛ {} !!!!!!!!!'.format(first[0], senond[0], first[0])
        elif first[1] == 'paper' and senond[1] == 'scissors':
            return '{} выбрал :roll_of_paper: и {} выбрал :scissors: \n ПОБЕДИЛ {} !!!!!!!!!'.format(first[0], senond[0], senond[0])
        elif first[1] == 'paper' and senond[1] == 'paper':
            return '{} выбрал :roll_of_paper: и {} выбрал :roll_of_paper: \n НИЧЬЯ !!!!!!!!!'.format(first[0], senond[0])


class Roll_dice:
    def __init__(self, players):
        self.players = players

    def join_(self, new_player, ctx, id):
        self.players.append(new_player)
        if len(self.players) == 2:
            return self.game_start(ctx, id)

    def game_start(self, ctx, id):
        ch = [('⚀', 1), ('⚁', 2), ('⚂', 3), ('⚃', 4), ('⚄', 5), ('⚅', 6)]

        first_player = [self.players[0], ['abc'], 0]
        second_player = [self.players[1], ['abc'], 0]

        first_roll = random.choice(ch)
        first_player[1].append(first_roll[0])
        first_player[2] += first_roll[1]

        second_roll = random.choice(ch)
        first_player[1].append(second_roll[0])
        first_player[2] += second_roll[1]

        first_roll = random.choice(ch)
        second_player[1].append(first_roll[0])
        second_player[2] += first_roll[1]

        second_roll = random.choice(ch)
        second_player[1].append(second_roll[0])
        second_player[2] += second_roll[1]

        if first_player[2] > second_player[2]:
            return '{} выбросил {} {}, сумма очков {} \n{} выбросил {} {}, сумма очков {}\n Победил {}!'.format(
                first_player[0], first_player[1][1], first_player[1][2], first_player[2], second_player[0],
                second_player[1][1], second_player[1][2], second_player[2], first_player[0])

        elif first_player[2] < second_player[2]:
            return '{} выбросил {} {}, сумма очков {} \n{} выбросил {} {}, сумма очков {}\n Победил {}!'.format(
                first_player[0], first_player[1][1], first_player[1][2], first_player[2], second_player[0],
                second_player[1][1], second_player[1][2], second_player[2], second_player[0])

        else:
            return '{} выбросил {} {}, сумма очков {} \n{} выбросил {} {}, сумма очков {}\n Ничья!'.format(
                first_player[0], first_player[1][1], first_player[1][2], first_player[2], second_player[0],
                second_player[1][1], second_player[1][2], second_player[2])
