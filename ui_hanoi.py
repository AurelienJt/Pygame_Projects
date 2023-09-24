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

        # Define pole properties
        self.POLE_WIDTH = 20
        self.POLE_HEIGHT = 280
        self.POLE_COLOR = (128, 128, 128)  # RGB for grey
        self.margin = 280

        #Define object properties
        

        # Calculate spacing
        self.total_spacing = WIDTH - (3 * self.POLE_WIDTH)
        self.spacing = self.total_spacing // 4

        #Objects
        self.big_color = (250,0,0)
        self.med_color = (0,255,0)
        self.small_color = (0,0,255)
        
        self.big_width = 200
        self.med_width = 150
        self.small_width = 100
        self.obj_height = 50

        #Predefined Positions

        self.layer_big = 1
        self.layer_med = 2
        self.layer_small = 3
        
        self.row_big = 0
        self.row_med = 0
        self.row_small = 0

        
        
        #General
        self.surface = pygame.surface.Surface((window.get_width(), window.get_height()))
        self.surface.fill((41, 43, 47))

        # Persistent UI
        for self.i in range(3):
            pygame.draw.rect(self.surface, self.POLE_COLOR, pygame.Rect((self.i+1)*self.spacing + self.i*self.POLE_WIDTH, self.margin, self.POLE_WIDTH, self.POLE_HEIGHT))

        pygame.draw.rect(self.surface,(0,0,0),pygame.Rect(self.spacing-180,560,2*(self.spacing + self.POLE_WIDTH)+360+self.POLE_WIDTH,5))
        self.menu_title_font = pygame.font.SysFont("arialblack", 60)
        self.menu_title = self.menu_title_font.render("Tour d'Hanoi", True, (255,255,255))

    def render(self):
        #Big Object
        pygame.draw.rect(self.surface,self.big_color,pygame.Rect(self.row_big*(self.spacing+self.POLE_WIDTH)+(self.spacing+(self.POLE_WIDTH//2))-(self.big_width//2),self.margin+self.POLE_HEIGHT-(self.layer_big*self.obj_height),self.big_width,self.obj_height))
        #Med Object
        pygame.draw.rect(self.surface,self.med_color,pygame.Rect(self.row_med*(self.spacing+self.POLE_WIDTH)+(self.spacing+(self.POLE_WIDTH//2))-(self.med_width//2),self.margin+self.POLE_HEIGHT-(self.layer_med*self.obj_height),self.med_width,self.obj_height))
        #Small Object
        pygame.draw.rect(self.surface,self.small_color,pygame.Rect(self.row_small*(self.spacing+self.POLE_WIDTH)+(self.spacing+(self.POLE_WIDTH//2))-(self.small_width//2),self.margin+self.POLE_HEIGHT-(self.layer_small*self.obj_height),self.small_width,self.obj_height))



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