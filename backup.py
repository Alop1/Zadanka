from abc import ABCMeta, abstractmethod
import random
import sys



class Game(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_drown_numbers(self): pass

    @abstractmethod
    def choose_players_number(self): pass



class GameMode1(Game):
    def __init__(self, game_number, mode, players=[]):
        print "---**Let's start the game. Good luck everyone!**--"
        self.game_number = game_number
        self.mode = mode
        self.drown_numbers = []
        self.players = players
        if self.mode == 1:
            self.follow_mode1_path()
            stats = StatsMaker(self, players)
        elif self.mode == 2:
            self.stats2 = StatsMaker(self, players)
            self.follow_mode2_path()
            self.stats2.show_scope()
            self.stats2.show_stats_per_round()
            self.stats2.show_player_stats()



    def follow_mode1_path(self):
        self.set_drown_numbers_model1()
        self.choose_players_number_model1()
        # todo staystyki z caalej gry
        print "wylosowane liczby to ", self.drown_numbers

    def choose_players_number_model1(self):
        for player in self.players:
            player.set_bet_number(self.mode, self.game_number)
            player.set_lucky_lose_numbers_in_game(self.drown_numbers)

    def set_drown_numbers_model1(self):
        self.drown_numbers = [random.randint(1, 10) for x in xrange(self.game_number)]

    def follow_mode2_path(self):
        self.stats2.show_scope()
        i = 1
        for game in xrange(self.game_number):
            self.set_drown_number_model2()
            self.choose_players_numbers_model2()
            # self.stats2.show_stats_per_round(i)
            i += 1
        for player in self.players:
            player.set_lucky_lose_numbers_in_game(self.drown_numbers)
        # self.stats2.show_player_stats()
    def choose_players_numbers_model2(self):
        for player in self.players:
            player.set_bet_number(self.mode)
            # print "player "+ player.name +" bet "+ str(player.bet_numbers[0])


    def set_drown_number_model2(self):
        self.drown_numbers.append(random.randint(1, 100))


class GameMode2(Game):
    def __init__(self, game_number, mode, players=[]):
        print "---**Let's start the game. Good luck everyone!**--"
        self.game_number = game_number
        self.mode = mode
        self.drown_numbers = []
        self.players = players
        if self.mode == 1:
            self.follow_mode1_path()
            stats = StatsMaker(self, players)
        elif self.mode == 2:
            self.stats2 = StatsMaker(self, players)
            self.follow_mode2_path()
            self.stats2.show_scope()
            self.stats2.show_stats_per_round()
            self.stats2.show_player_stats()



    def follow_mode1_path(self):
        self.set_drown_numbers_model1()
        self.choose_players_number_model1()
        # todo staystyki z caalej gry
        print "wylosowane liczby to ", self.drown_numbers

    def choose_players_number_model1(self):
        for player in self.players:
            player.set_bet_number(self.mode, self.game_number)
            player.set_lucky_lose_numbers_in_game(self.drown_numbers)

    def set_drown_numbers_model1(self):
        self.drown_numbers = [random.randint(1, 10) for x in xrange(self.game_number)]

    def follow_mode2_path(self):
        self.stats2.show_scope()
        i = 1
        for game in xrange(self.game_number):
            self.set_drown_number_model2()
            self.choose_players_numbers_model2()
            # self.stats2.show_stats_per_round(i)
            i += 1
        for player in self.players:
            player.set_lucky_lose_numbers_in_game(self.drown_numbers)
        # self.stats2.show_player_stats()
    def choose_players_numbers_model2(self):
        for player in self.players:
            player.set_bet_number(self.mode)
            # print "player "+ player.name +" bet "+ str(player.bet_numbers[0])


    def set_drown_number_model2(self):
        self.drown_numbers.append(random.randint(1, 100))


class Player():
    def __init__(self):
        self.name = raw_input("What is your name? ")
        self.bet_numbers = []     #mozna stworzyc @property
        self.winner_number_per_game = []
        self.lose_numer_per_game = []

    def set_bet_number(self, mode=1, game_number=1):
        if mode == 1:       #inster all x number
            self.bet_numbers = raw_input(self.name + ", please type " + str(game_number) + " bet numbers, each followed by coma: ")
            self.bet_numbers = self.bet_numbers.split(",")
            print self.bet_numbers
        elif mode == 2:         #inster one number
            new_number = int(raw_input(self.name + ", please type your bet number: "))
            self.bet_numbers.append(new_number)
            print self.bet_numbers

    def winner_numbers_in_game(self, drown_numbers, mode=2):
        if mode == 2:
            for i in xrange(len(self.bet_numbers)):
                if int(self.bet_numbers[i]) == drown_numbers[i]:
                    self.winner_number_per_game.append(self.bet_numbers[i])
                else:
                    self.lose_numer_per_game.append(self.bet_numbers[i])




class StatsMaker():
    def __init__(self, game, players):
        self.game = game
        self.players = players
        # self.show_scope()
        if game.mode == 1:
            self.show_scope()
            self.show_general_stats()
            self.show_player_stats()



    def show_scope(self):
        print "\nTOTAL NUMBER OF PLAYERS: ", len(self.players)
        print "TOTAL NUMBER OF GAMES: ", self.game.game_number, "\n\n"

    def show_general_stats(self):
        if self.game.mode == 1:
            print "GAME\t WIN NUMER"
            i = 1
            for winner_number in self.game.drown_numbers:
                print i, "\t\t", winner_number
                i += 1

    def show_player_stats(self):
        print "\nPLAYER \t BET \t WIN \t LOSE"
        for player in self.players:
            print player.name + " \t\t\t" + str(player.winner_number_per_game) +"\t" + str(player.lose_numer_per_game)
    # todo  dwie rozne staystyki dl agraca i playera

    def show_stats_per_round(self):
        for round_no in xrange(self.game.game_number):
            bet_number = []
            winners = []
            for player in self.players:
                bet_number.append(player.bet_numbers[round_no-1])
                if player.bet_numbers[round_no-1] == self.game.drown_numbers[round_no-1]:
                    winners.append(player.name)
            print "\nGAME NUMER:", round_no
            print "BET NUMBERS: ", bet_number
            print "WIN NUMBER:  ",  self.game.drown_numbers[round_no-1]
            print "WINNERS: ", winners




def main(argv):
    print argv
    #create player()
    player1 = Player()
    player2 = Player()
    # game_mode1 = Game(5, 1, [player1, player2])
    game_mode2 = Game(5, 2, [player1,player2])
    # stats = StatsMaker(game_mode2, [player1])

    #start game



if __name__ == "__main__":
    main(sys.argv[1:])
