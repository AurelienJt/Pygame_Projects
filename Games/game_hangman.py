#----------- IMPORTS -----------#
import time
import os
import json
from random import randint
from Libraries.Lib_Hangman.lib_hangman import clear_terminal,game_rules,loading_dots,win_drawing,drawings, recursive_check_guess, recursive_check_rules
#----------- init -----------#
dictionnary_path = os.path.join("Libraries", "Lib_Hangman","lib_dict_hangman.json")

with open(file=dictionnary_path,mode="r") as file:
    word_list = json.load(file)
#----------- main -----------#
total_turns = 0
word = word_list[randint(0,len(word_list))]
guess_list = ''

run = True

class Hangman():
    def __init__(self):
        self.word = "turtle"
        self.known_letters = 0
        self.player_lives = 9
        self.total_turns = 0
        self.guess_list = ''
        self.finished = False

    def play(self, word:str, guess:str):
        self.guess = guess
        self.word = word

        self.total_turns += 1
        Hangman.check_guess(self)
        Hangman.check_won(self)


    def check_guess(self):
        self.guess_list += guess
        if self.guess not in self.word:
            self.player_lives -= 1
            print(f"Bummer, that was not in the word, you have {self.player_lives} lives left.")
            str(input("~Press [Enter]~"))
        else:
            if self.guess == self.word:
                print(f"You win ! You won in {self.total_turns} turns")
                exit()
            print(f"Good job ! {self.guess} was in the word")
            str(input("~Press [Enter]~"))

    def check_won(self):
        self.known_letters = 0

        for character in self.word:
            if character in self.guess_list:
                self.known_letters += 1

        if self.known_letters == len(self.word):
            self.finished = True
    

    def display(self, guess_list:str):
        self.guess_list = guess_list

        for character in self.word:
            if character in self.guess_list:
                print(f"{character} ", end="")
            else:
                print("_ ", end="")


game_hangman = Hangman()

while run:
    clear_terminal()
    game_hangman.display(guess_list=guess_list)
    guess = input("\n\nGuess a character : ")
    guess_list += guess
    game_hangman.play(guess=guess, word=word)

    if game_hangman.finished:
        clear_terminal()
        print(f"You won ! You won in {total_turns} turns !")
        run = False
#-------- Made by _N1ghtW0lf --------#