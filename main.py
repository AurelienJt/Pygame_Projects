import pygame
from sys import exit
from Libraries.Lib_General.Buttons import LayeredButton

pygame.init()

WIDTH = 600
HEIGHT = 1200

# pygame variables
info = pygame.display.Info()
win = pygame.display.set_mode((HEIGHT, WIDTH))
clock = pygame.time.Clock()
FPS = 60

# user interface
menuButtonFont = pygame.font.SysFont("arialblack", 40)
gamesButton = LayeredButton("games", 500, 80, (350, 220), 5, menuButtonFont, (41,43,47), (100, 100, 100), (41,43,47))
creditsButton = LayeredButton("credits", 500, 80, (350, 420), 5, menuButtonFont, (41,43,47), (100,100,100), (41,43,47))

# general variables
currentMenu = "MainMenu" # MainMenu, Hangman, Tetris, etc...


running = True
while running:
    if currentMenu == "MainMenu":
        pygame.display.set_caption("MAIN MENU")
        win.fill((41,43,47)) # MainMenu Color
        win.blit(pygame.font.SysFont("arialblack", 60).render("PYPROJECTS HUB", True, (255,255,255)), (300, 50)) # TITLE
        win.blit(pygame.font.SysFont("impact", 30).render(str(int(clock.get_fps())), True, (237, 206, 104)), (10, 10)) # FPS
        
        if gamesButton.draw(win):
            pass
        if creditsButton.draw(win):
            pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()


    clock.tick(FPS)
    pygame.display.update()
