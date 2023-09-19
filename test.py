import pygame
from Libraries.Lib_General.lib_general import text_pos,button_pos


class Surface():
    def __init__(self,window):
        self.surface = pygame.surface.Surface((window.get_width(),window.get_height()))
        self.surface.fill((41,43,47))
        self.text_font = pygame.font.SysFont("arialblack",40)
        self.text = self.text_font.render("Testing Surface",True,(255,255,255))
        self.surface.blit(self.text,(text_pos("center",self.surface,self.text)))


