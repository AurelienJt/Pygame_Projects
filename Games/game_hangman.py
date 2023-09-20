#----------- IMPORTS -----------#

import time
import os
import json
from random import randint
from Libraries.Lib_Hangman.lib_hangman import clearTerminal,game_rules,loadingDots,win_drawing,drawings

#----------- Init -----------#
dictionnary_path = os.path.join("Libraries", "Lib_Hangman","lib_dict_hangman.json")

with open(file=dictionnary_path,mode="r") as file:
    word_list = json.load(file)

#---------- VARIABLES ----------#

game_word = word_list[randint(0,len(word_list)-1)]
game_word_letters = len(game_word)
guess_list = ''
game_turns = 9
drawings_index = 0
total_turns = 0

#------------- MAIN -------------#
os.system('clear')


print("\n- Welcome to Hangman !\n")
time.sleep(1)
print(game_word, "\n")
player_name = str(input("- Please tell me, what is your name ?\n\n"))
time.sleep(0.5)
print("\n- Ah I see. Pleased to meet you", player_name.capitalize(), "!\n\n~Press [Enter] to continue~")
str(input())

clearTerminal()
try :
    answer = int(input("\n- Do you know the rules of Hangman?\n\n~Please enter 1 or 2~\n\n[1]: Yes\n[2]: No\n\n"))
except ValueError:
    print("Error. Please enter either 1 or 2")

if answer == 2:
    clearTerminal()

    print("\n- Here are the rules !\n")
    print(game_rules, "\n~Press [Enter] to continue~\n")
    str(input())


clearTerminal()
loadingDots()
print("\n- Well, let's play !\n")
time.sleep(0.5)
clearTerminal()

#------------- GAME -------------#

#print ("\n-------------------------------------------------------------------------\n")
#print(startDrawing,"\n")
#print("Your word has", game_word_letters, "letters")
#print("\nYour guesses were :", guess_list, "\n")

while game_turns > 0:
    unknown_letters = 0

    for characters in game_word:        
        if characters in guess_list:
            print(characters + " ", end="")

        else :
            print("_ ", end="")
            unknown_letters += 1

    if unknown_letters == 0:
        clearTerminal()

        print ("\n-------------------------------------------------------------------------")
        print(win_drawing, "\n")
        print("Good job, you won in", total_turns, "turns !! \nThe word was", game_word, "\n\n")
        
        break            

    guess_letter = input("\n\nGuess a character : ")
    if len(guess_letter) > 1:
        print("Only insert one character please.")
        exit()
    guess_list += guess_letter             
    total_turns += 1

    clearTerminal()
    print ("\n-------------------------------------------------------------------------\n")
    print(drawings[drawings_index],"\n")
    print("Your word has", game_word_letters, "letters")
    print("\nYour guesses were :", guess_list, "\n")

    if guess_letter not in game_word:  
        game_turns -= 1     
        drawings_index += 1   
        print ("Bummer, you're wrong..")  
        print ("You have", + game_turns, "guesses left !\n")
 
        if game_turns == 0:
            print ("You killed him, what a horrible person you are...\nThe word was", game_word, "\n")

#-------- Made by _N1ghtW0lf --------#