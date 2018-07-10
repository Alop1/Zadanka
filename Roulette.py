import random
import sys

"""Roulette. Number of players,  number of games and game mode are passed to program via command line
(I.e.: python roulette.py 6 2 1). At the beginning program asks about names of the players and the numbers they bet.
Next depending on game mode following actions are executed:
Mode 1: Program executes all games and finally print  summary in form (example):
TOTAL NUMBER OF PLAYERS: 1
TOTAL NUMBER OF GAMES: 5

RESULTS
GAME	WIN NUMBER
1		24
2		3
3		1
4		1
5		24

PLAYER	BET		WIN		LOSE
John		3, 17, 24	1, 2, 5		3, 4
"""
class Game():
    def __init__(self, game_number, mode, players=[]):
        print "---**Let's start the game. Good luck everyone!**--"
        self.game_number = game_number
        self.mode = mode
        self.winner_numbers = []
        self.players = players
        if self.mode == 1:
            self.follow_mode1_path()
            stats = StatsMaker(self, players)
        elif self.mode == 2:
            self.follow_mode2_path()

                        # todo po kazdym przejsciu gry statystyki dla

    def follow_mode1_path(self):
        self.set_winner_number_model1()
        self.set_betted_number_model1()
        # todo staystyki z caalej gry
        print "zwycieskie liczby to ", self.winner_numbers

    def set_betted_number_model1(self):
        for player in self.players:
            player.set_bet_number(self.mode, self.game_number)
            player.winner_numbers_in_game(self.winner_numbers)


    def set_winner_number_model1(self):
        self.winner_numbers = random.sample(xrange(1, 10), self.game_number)

    def follow_mode2_path(self):
        i = 1
        for game in xrange(self.game_number):
            print "ROUND ", i
            self.update_winner_number_model2()
            self.set_betted_number_model2()
            print "winner numer : ", self.winner_numbers[i - 1]
            i += 1

    def set_betted_number_model2(self):
        for player in self.players:
            player.set_bet_number(self.mode)
            print "player "+ player.name +" bet "+ str(player.bet_number[0])

    def update_winner_number_model2(self):
        self.winner_numbers.append(random.sample(xrange(1, 100), 1)[0])


class Player():
    def __init__(self):
        self.name = raw_input("What is your name? ")
        self.bet_numbers = ''     #mozna stworzyc @property
        self.winner_number_per_game = []
        self.lose_numer_per_game = []

    def set_bet_number(self, mode=1, game_number=1):
        if mode == 1:       #inster all x number
            self.bet_numbers = raw_input(self.name + ", please type " + str(game_number) + " bet numbers, each followed by coma: ")
            self.bet_numbers = self.bet_numbers.split(",")
            print self.bet_numbers
        elif mode == 2:         #inster one number
            self.bet_numbers = raw_input(self.name + ", please type your bet number: ")
            self.bet_numbers = list(self.bet_numbers)

    def winner_numbers_in_game(self, winner_numbers):
        for number in self.bet_numbers:
            if number in winner_numbers:
                self.winner_number_per_game.append(number)
            else:
                self.lose_numer_per_game.append(number)






class StatsMaker():
    def __init__(self, game, players):
        self.game = game
        self.players = players
        self.show_general_stats()
        self.show_player_stats()


    def show_general_stats(self):
        if self.game.mode == 1:
            print "GAME\t WIN NUMER"
            i = 1
            for winner_number in self.game.winner_numbers:
                print i, "\t\t", winner_number
                i += 1
    def show_player_stats(self):
        print "PLAYER \t BET \t WIN \t LOSE"
        for player in self.players:
            print player.name + " \t\t\t" + str(player.winner_number_per_game) +"\t" + str(player.lose_numer_per_game)


            pass
    # todo  dwie rozne staystyki dl agraca i playera




def main(argv):
    print argv
    #create player
    player1 = Player()
    game_mode1 = Game(5, 1, [player1])
    # game_mode2 = Game(5, 2, [player1])
    # stats = StatsMaker(game_mode2, [player1])

    #start game



if __name__ == "__main__":
    main(sys.argv[1:])
