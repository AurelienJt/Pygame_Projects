import time
import os

guess_letter = ""
game_word = ""
total_turns = 0

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

win_drawing = """
  \🥳/   
   | 
  / \ 
"""

game_rules = """
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

def loading_dots():
  print("Drawing")
  clear_terminal()
  print("Drawing.")
  clear_terminal()
  print("Drawing..")
  clear_terminal()
  print("Drawing...")
  clear_terminal()
  print("Choosing word")
  clear_terminal()
  print("Choosing word.")
  clear_terminal()
  print("Choosing word..")
  clear_terminal()
  print("Choosing word...")
  clear_terminal()
  print("Loading")
  clear_terminal()
  print("Loading.")
  clear_terminal()
  print("Loading..")
  clear_terminal()
  print("Loading...")
  clear_terminal()
  time.sleep(0.5)

def clear_terminal():
    time.sleep(0.5)
    os.system('clear')

def recursive_check_rules():
  clear_terminal()
  try :
      answer = int(input("\n- Do you know the rules of Hangman?\n\n~Please enter 1 or 2~\n\n[1]: Yes\n[2]: No\n\n"))
  except ValueError:
      print("Error. Please enter either 1 or 2")

  if answer == 1 or answer == 2:
     if answer == 1:
        pass
     if answer == 2:
            clear_terminal()

            print("\n- Here are the rules !\n")
            print(game_rules, "\n~Press [Enter] to continue~\n")
            str(input())
  else :
      str(input("\nError. Please enter 1 or 2\n\n~Press [Enter] to continue~\n"))
      recursive_check_rules()

def win():
    clear_terminal()
    print ("\n-------------------------------------------------------------------------")
    print(win_drawing, "\n")
    print("Good job, you won in", total_turns, "turns !! \nThe word was", game_word, "\n\n")
    exit()    

def recursive_check_guess():
    guess_letter = input("\n\nGuess a character : ")
    if len(guess_letter) > 1:
        if guess_letter == game_word:
            win()
        str(input("\nOnly insert one character please.\n\n~Press [Enter] to continue~\n"))
        recursive_check_guess()