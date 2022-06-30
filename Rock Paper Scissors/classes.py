from enum import Enum
import random
import pyfiglet


class Options(Enum):
    NONE = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class WinModes(Enum):
    Draw = 0
    BOT_Wins = 1
    USER_Wins = 2


class Game:
    def __init__(self):
        self.user_score = 0
        self.bot_score = 0
        self.versuses = {
            Options.ROCK: Options.PAPER,
            Options.PAPER: Options.SCISSORS,
            Options.SCISSORS: Options.ROCK,
        }
        self.__limit = -1

    def set_limit(self, number):
        self.__limit = number

    def is_win(self):
        if self.__limit == -1:
            return 0
        if self.bot_score >= self.__limit:
            return -1
        elif self.user_score >= self.__limit:
            return 1
        else:
            return 0

    def get_selected_option(self, target_string):
        if target_string.lower().strip() == "rock":
            return Options.ROCK
        elif target_string.lower().strip() == "paper":
            return Options.PAPER
        elif target_string.lower().strip() == "scissors":
            return Options.SCISSORS
        else:
            return Options.NONE

    def play_always_bot_wins(self, user):
        if type(user) == str:
            user = self.get_selected_option(user)
        elif not (type(user) == type(Options.NONE)):
            raise ValueError("An Error In Play")

        self.bot_score += 1

        return self.versuses[user]

    def play_round(self, user):
        if type(user) == str:
            user = self.get_selected_option(user)
        elif not (type(user) == type(Options.NONE)):
            raise ValueError("An Error In Play")

        bot_choice = random.choice(
            [Options.ROCK, Options.PAPER, Options.SCISSORS])

        if bot_choice == user:
            return bot_choice, WinModes.Draw
        elif bot_choice == self.versuses[user]:
            self.bot_score += 1
            return bot_choice, WinModes.BOT_Wins
        else:
            self.user_score += 1
            return bot_choice, WinModes.USER_Wins

    def show_status(self):
        # fonts = (pyfiglet.FigletFont.getFonts())
        # target_font = random.choice(fonts)
        # print(target_font)
        target_font = 'rounded'
        print('=' * 70)
        result = (pyfiglet.figlet_format(
            f"BOT : USER\n        {self.bot_score} : {self.user_score}", font=target_font))
        print(result)
        print('=' * 70)
