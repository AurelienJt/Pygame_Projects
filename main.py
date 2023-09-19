import pygame
from sys import exit
from Libraries.Lib_General.lib_button import LayeredButton
from Libraries.Lib_General.lib_general import text_pos

pygame.init()

HEIGHT = 600
WIDTH = 1200

# pygame variables
info = pygame.display.Info()
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

# user interface
menu_button_font = pygame.font.SysFont("arialblack", 40)
menu_title_font = pygame.font.SysFont("arialblack", 60)
games_button = LayeredButton("Game Library", 500, 80, (350, 220), 5, menu_button_font, (41,43,47), (100, 100, 100), (41,43,47))
credits_button = LayeredButton("Credits", 500, 80, (350, 420), 5, menu_button_font, (41,43,47), (100,100,100), (41,43,47))

menu_title = menu_title_font.render("MultiGameBox", True, (255,255,255))

# general variables
current_menu = "MainMenu" # MainMenu, Hangman, Tetris, etc...

running = True
while running:
  
    if current_menu == "MainMenu":
        pygame.display.set_caption(current_menu)
        win.fill((41,43,47)) # MainMenu Color
        win.blit(menu_title, (text_pos("x_center",win,menu_title),60))
        # win.blit(menu_title,(text_pos.width,text_pos.height)) # TITLE
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
