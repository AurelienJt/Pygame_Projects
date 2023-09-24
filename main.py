import pygame
from sys import exit
import copy
from Libraries.Lib_General.lib_button import LayeredButton
from Libraries.Lib_General.lib_general import text_pos,button_pos
from Libraries.Menus.ui_game_select import Game_Selector
from Libraries.Menus.ui_menu import Main_Menu

from ui_hanoi import UI_Hanoi

pygame.init()

HEIGHT = 600
WIDTH = 1200

# pygame variables
info = pygame.display.Info()
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60


# general variables
back_font = pygame.font.SysFont("arialblack", 40)
back_button = LayeredButton("X", 50, 50, (20, 20), 5, back_font, (255,0,0), (100, 100, 100), (41,43,47))
current_menu = "MainMenu" # MainMenu, Hangman, Tetris, etc...
previous_menu = ["MainMenu"]

#Menus
game_selector = Game_Selector(win)
game_honai = UI_Hanoi(win)
main_menu = Main_Menu(win)


running = True
while running:
    
    if current_menu != previous_menu[-1]:
        previous_menu.append(current_menu)
  
    if current_menu == "MainMenu":
        main_menu.render()
        win.blit(main_menu.surface,(0,0))
        current_menu = main_menu.current_menu

    elif current_menu == "GameSelector":
        game_selector.render()
        win.blit(game_selector.surface,(0,0))
        current_menu = game_selector.current_menu

    elif current_menu == "Hanoi":
        game_honai.render()
        win.blit(game_honai.surface,(0,0))
        current_menu = game_honai.current_menu
        
    if current_menu != "MainMenu":
        if back_button.draw(win):
            current_menu = previous_menu[-2]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    pygame.display.set_caption(current_menu)

    clock.tick(FPS)
    pygame.display.update()
