#----------- IMPORTS -----------#

from random import *
import time
from hangmanLib import *
import os

#---------- VARIABLES ----------#

gameWord = wordList[randint(0, 19)]
gameWordLetters = len(gameWord)
guessList = ''
gameTurns = 8
drawingsIndex = 0
totalTurns = 0

#------------- MAIN -------------#
os.system('clear')


print("\n- Welcome to Hangman !\n")
time.sleep(1)
playerName = str(input("- Please tell me, what is your name ?\n\n"))
time.sleep(0.5)
print("\n- Ah I see. Pleased to meet you", playerName.capitalize(), "!\n\n~Press [Enter] to continue~")
str(input())

clearTerminal()

answer = int(input("\n- Do you know the rules of Hangman?\n\n~Please enter 1 or 2~\n\n[1]: Yes\n[2]: No\n\n"))

if answer == 2:
    clearTerminal()

    print("\n- Here are the rules !\n")
    print(gameRules, "\n~Press [Enter] to continue~\n")
    str(input())


clearTerminal()
#loadingDots()
print("\n- Well, let's play !\n")
time.sleep(0.5)
clearTerminal()

#------------- GAME -------------#

print ("\n-------------------------------------------------------------------------\n")
print(startDrawing,"\n")
print("Your word has", gameWordLetters, "letters")
print("\nYour guesses were :", guessList, "\n")

while gameTurns > 0:
    failedGuesses = 0

    for characters in gameWord:        
        if characters in guessList:
            print(characters + " ", end="")

        else :
            print("_ ", end="")
            failedGuesses += 1

    if failedGuesses == 0:
        clearTerminal()

        print ("\n-------------------------------------------------------------------------")
        print(winDrawing, "\n")
        print("Good job, you won in", totalTurns, "turns !! \nThe word was", gameWord, "\n\n")
        
        break            

    guessLetter = input("\n\nGuess a character or a word : ")
    guessList += guessLetter                    
    totalTurns += 1

    clearTerminal()
    print ("\n-------------------------------------------------------------------------\n")
    print(drawings[drawingsIndex],"\n")
    print("DI:", drawingsIndex)
    print("FG:", failedGuesses)
    print("Your word has", gameWordLetters, "letters")
    print("\nYour guesses were :", guessList, "\n")

    if guessLetter not in gameWord:  
        gameTurns -= 1     
        drawingsIndex += 1   
        print ("Bummer, you're wrong..")  
        print ("You have", + gameTurns, "guesses left !\n")
 
        if gameTurns == 0:
            print ("\nYou killed him, what a horrible person you are...\nThe word was", gameWord)

#-------- Made by _N1ghtW0lf --------#