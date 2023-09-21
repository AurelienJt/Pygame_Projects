import pygame
from Libraries.Lib_General.lib_button import LayeredButton
from Libraries.Lib_General.lib_general import text_pos,button_pos

class Main_Menu():
    def __init__(self,window):
        
        self.menu_id = "MainMenu"
        self.current_menu = self.menu_id
        
        #General
        self.surface = pygame.surface.Surface((window.get_width(), window.get_height()))
        self.surface.fill((41, 43, 47))
        
        self.menu_button_font = pygame.font.SysFont("arialblack", 40)
        self.menu_title_font = pygame.font.SysFont("arialblack", 60)
        self.games_button = LayeredButton("Game Library", 500, 80, (350, 220), 5, self.menu_button_font, (41,43,47), (100, 100, 100), (41,43,47))
        self.credits_button = LayeredButton("Credits", 500, 80, (350 ,420), 5, self.menu_button_font, (41,43,47), (100,100,100), (41,43,47))
        
        self.menu_title = self.menu_title_font.render("Pygame Projects", True, (255,255,255))
        
    def render(self):
        self.surface.blit(self.menu_title, (text_pos("x_center",self.surface,self.menu_title),60))
        self.current_menu = self.menu_id
        
        if self.games_button.draw(self.surface):
            self.current_menu = "GameSelector"
            
        if self.credits_button.draw(self.surface):
            pass