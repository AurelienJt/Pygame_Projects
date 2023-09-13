import time
import os

guessLetter = "x"
gameWord = "xxx"

wordList = ["apple", "banana", "cat", "dog", "fish", "house", "jump", "kite", "lemon", "mouse", "panda", "queen", "rabbit", "snake", "turtle", "unicorn", "violin", "water", "xylophone", "zebra"]

startDrawing ="""
  +----+
       |
       |
       |
       |
       |
=========
"""
drawings = ["""
  +----+
       |
       |
       |
       |
       |
=========
""", """
  +----+
  |    |
       |
       |
       |
       |
=========
""", """
  +----+
  |    |
  0    |
       |
       |
       |
=========
""", """
  +----+
  |    |
  0    |
  |    |
       |
       |
=========
""", """
  +----+
  |    |
  0    |
  |\   |
       |
       |
=========
""", """
  +----+
  |    |
  0    |
 /|\   |
       |
       |
=========
""", """
  +----+
  |    |
  0    |
 /|\   |
 /     |
       |
=========
""", """
  +----+
  |    |
  0    |
 /|\   |
 / \   |
       |
=========
""", """
  +----+
  |    |
  💀   |
       |
       |
       |
=========
"""]

winDrawing = """
 \ 0 /   
   | 
  / \ 
"""

gameRules = """
--------------------------------- Rules ---------------------------------

  - You have to guess a word in a limited amount of errors

  - Each round you guess a letter, if the word contains this letter,
      it will appear instead of a [ _ ] character
      If the character does not match, an error will be counted
  
  - An error is symbolized by the drawing of a hangman gaining limbs

  - Guess the word and win !

  - Win with the fewest errors possible to get the best score !

  - Have fun !


---------------------- This was made by _N1ghtW0lf ----------------------
"""

def loadingDots():
  print("Drawing...")
  clearTerminal()
  print("Drawing..")
  clearTerminal()
  print("Drawing.")
  clearTerminal()
  print("Drawing")
  clearTerminal()
  print("Choosing word...")
  clearTerminal()
  print("Choosing word..")
  clearTerminal()
  print("Choosing word.")
  clearTerminal()
  print("Choosing word")
  clearTerminal()
  print("Loading...")
  clearTerminal()
  print("Loading..")
  clearTerminal()
  print("Loading.")
  clearTerminal()
  print("Loading")
  clearTerminal()
  time.sleep(0.5)

def clearTerminal():
    time.sleep(0.5)
    os.system('clear')

def checkGuess(amountOfGuesses):
  if guessLetter in gameWord:
    print("- Nice ! You got that one right")
  else:
    print("- Bummer, that was wrong...")