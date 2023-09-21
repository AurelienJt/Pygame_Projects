import pygame
from sys import exit
import copy
from Libraries.Lib_General.lib_button import LayeredButton
from Libraries.Lib_General.lib_general import text_pos,button_pos
from Libraries.Windows.game_selector_menu import Game_Selector
from Libraries.Windows.main_menu import Main_Menu

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
main_menu = Main_Menu(win)

running = True
while running:
    
    if current_menu != previous_menu[-1]:
        previous_menu.append(current_menu)
  
    if current_menu == "MainMenu":
        main_menu.render()
        win.blit(main_menu.surface,(0,0))
        pygame.display.set_caption(current_menu)
        current_menu = main_menu.current_menu

    if current_menu == "GameSelector":
        game_selector.render()
        win.blit(game_selector.surface,(0,0))
        pygame.display.set_caption(current_menu)
        current_menu = game_selector.current_menu
        
    if back_button.draw(win):
        current_menu = previous_menu[-2]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()


    clock.tick(FPS)
    pygame.display.update()
