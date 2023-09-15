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
menu_title_font = pygame.font.SysFont("arialblack", 60)
games_button = LayeredButton("games", 500, 80, (350, 220), 5, menu_button_font, (41,43,47), (100, 100, 100), (41,43,47))
credits_button = LayeredButton("credits", 500, 80, (350, 420), 5, menu_button_font, (41,43,47), (100,100,100), (41,43,47))

menu_title = menu_title_font.render("PYPROJECTS HUB", True, (255,255,255))
# general variables
current_menu = "MainMenu" # MainMenu, Hangman, Tetris, etc...


def text_pos(position:str,win):
    height =  win.get_height()
    width = win.get_width()
    return (width/2, height/2)

running = True
while running:
    if current_menu == "MainMenu":
        pygame.display.set_caption("MAIN MENU")
        win.fill((41,43,47)) # MainMenu Color
        win.blit(menu_title,(200,200)) # TITLE
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
