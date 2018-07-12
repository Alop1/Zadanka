from abc import ABCMeta, abstractmethod
import random
import sys


class Game(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_game(self): pass

    @abstractmethod
    def set_drown_numbers(self): pass

    @abstractmethod
    def drawn_players_numbers(self): pass


class GameMode1(Game):
    def __init__(self, game_number, players):
        print "---**Let's start the game. Good luck everyone!**--"
        self.game_number = game_number
        self.mode = 1
        self.drown_numbers = []
        self.players = players
        self.stats = StatsMaker(self, players)
        # self.stats.show_scope()
        # self.stats.show_player_stats()

    def start_game(self):
        self.set_drown_numbers()
        self.drawn_players_numbers()
        # print "wylosowane liczby to ", self.drown_numbers

    def drawn_players_numbers(self):
        for player in self.players:
            player.set_bet_number(self.mode, self.game_number)
            player.set_lucky_lose_numbers_in_game(self.drown_numbers)

    def set_drown_numbers(self):
        self.drown_numbers = [random.randint(1, 10) for x in xrange(self.game_number)]


class GameMode2(Game):
    def __init__(self, game_number, players):
        print "---**Let's start the game. Good luck everyone!**--"
        self.game_number = game_number
        self.mode = 2
        self.drown_numbers = []
        self.players = players

        self.stats2 = StatsMaker(self, players)

    def start_game(self):
        for game in xrange(self.game_number):
            self.set_drown_numbers()
            self.drawn_players_numbers()
        for player in self.players:
            player.set_lucky_lose_numbers_in_game(self.drown_numbers)

    def drawn_players_numbers(self):
        for player in self.players:
            player.set_bet_number(self.mode)

    def set_drown_numbers(self):
        self.drown_numbers.append(random.randint(1, 10))


class Player(object):
    def __init__(self):
        self.name = raw_input("What is your name? ")
        self.bet_numbers = []
        self.lucky_numbers_per_game = []
        self.lose_numbers_per_game = []

    def set_bet_number(self, mode=1, game_number=0):
        if mode == 1:
            self.bet_numbers = raw_input(self.name + ", please type " + str(game_number) + " bet numbers, each followed by coma: ")
            self.bet_numbers = self.bet_numbers.split(",")
            print self.bet_numbers
        elif mode == 2:
            new_number = int(raw_input(self.name + ", please type your bet number: "))
            self.bet_numbers.append(new_number)
            print self.bet_numbers

    def set_lucky_lose_numbers_in_game(self, drown_numbers, mode=2):
            for i in xrange(len(self.bet_numbers)):
                if int(self.bet_numbers[i]) == drown_numbers[i]:
                    self.lucky_numbers_per_game.append(self.bet_numbers[i])
                else:
                    self.lose_numbers_per_game.append(self.bet_numbers[i])




class StatsMaker():
    def __init__(self, game, players):
        self.game = game
        self.players = players



    def show_scope(self):
        print "\nTOTAL NUMBER OF PLAYERS: ", len(self.players)
        print "TOTAL NUMBER OF GAMES: ", self.game.game_number, "\n\n"

    def show_general_stats(self):
        if self.game.mode == 1:
            print "GAME\t WIN NUMBER"
            i = 1
            for winner_number in self.game.drown_numbers:
                print i, "\t\t", winner_number
                i += 1

    def show_player_stats(self):
        print "\nPLAYER \t BET \t WIN \t LOSE"
        for player in self.players:
            print player.name + " \t\t\t" + str(player.lucky_numbers_per_game) + "\t" + str(player.lose_numbers_per_game)

    def show_stats_per_round(self):
        for round_no in xrange(self.game.game_number):
            bet_number = []
            winners = []
            for player in self.players:
                bet_number.append(player.bet_numbers[round_no])
                if player.bet_numbers[round_no] == self.game.drown_numbers[round_no]:
                    winners.append(player.name)
            print "\nGAME NUMBER:", round_no + 1
            print "BET NUMBERS: ", bet_number
            print "WIN NUMBER:  ",  self.game.drown_numbers[round_no]
            displayed_winners = winners if winners else "None"
            print "WINNERS: ", displayed_winners




def main(argv):
    print argv
    #create player()
    player1 = Player()
    player2 = Player()

    # game_mode1 = GameMode1(5, [player1, player2])
    # game_mode1.start_game()
    # game_mode1.stats.show_scope()
    # game_mode1.stats.show_general_stats()
    # game_mode1.stats.show_player_stats()

    game_mode2 = GameMode2(5, [player1, player2])
    game_mode2.start_game()
    game_mode2.stats2.show_scope()
    game_mode2.stats2.show_stats_per_round()
    game_mode2.stats2.show_player_stats()




if __name__ == "__main__":
    main(sys.argv[1:])
