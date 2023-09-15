import pygame
from sys import exit
from Libraries.Lib_General.lib_button import LayeredButton

pygame.init()

WIDTH = 600
HEIGHT = 1200

# pygame variables
info = pygame.display.Info()
win = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()
FPS = 60

# user interface
menu_button_font = pygame.font.SysFont("arialblack", 40)
games_button = LayeredButton("games", 500, 80, (350, 220), 5, menu_button_font, (41,43,47), (100, 100, 100), (41,43,47))
credits_button = LayeredButton("credits", 500, 80, (350, 420), 5, menu_button_font, (41,43,47), (100,100,100), (41,43,47))

# general variables
current_menu = "main_enu" # MainMenu, Hangman, Tetris, etc...


running = True
while running:
    if current_menu == "main_enu":
        pygame.display.set_caption("Main Menu")
        win.fill((41,43,47)) # MainMenu Color
        win.blit(pygame.font.SysFont("arialblack", 60).render("Games.Py", True, (255,255,255)), (300, 50)) # TITLE
        win.blit(pygame.font.SysFont("impact", 30).render(str(int(clock.get_fps())), True, (237, 206, 104)), (10, 10)) # FPS
        
        if games_button.draw(win):
            pass
        if credits_button.draw(win):
            pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()


    clock.tick(FPS)
    pygame.display.update()
