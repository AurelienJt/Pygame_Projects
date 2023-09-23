import pygame
from Games.game_hanoi import Hanoi
from Libraries.Lib_General.lib_general import *

pygame.init()

WIDTH = 1200
HEIGHT = 600

info = pygame.display.Info()
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True

class UI_Hanoi():
    def __init__(self,window):
        #General
        self.menu_id = "Hanoi"
        self.current_menu = self.menu_id
        
        #General
        self.surface = pygame.surface.Surface((window.get_width(), window.get_height()))
        self.surface.fill((41, 43, 47))

        self.menu_title_font = pygame.font.SysFont("arialblack", 60)
        self.menu_title = self.menu_title_font.render("Hanoi", True, (255,255,255))

    def render(self):
        self.surface.blit(self.menu_title, (text_pos("x_center",self.surface,self.menu_title),60))
        self.current_menu = self.menu_id

        return self.surface

v1 = UI_Hanoi(win)

while running:
    
    win.blit(v1.render(),(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    clock.tick(FPS)
    pygame.display.update()