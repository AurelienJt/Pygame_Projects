import pygame
from Libraries.Lib_General.lib_general import text_pos, button_pos
from Libraries.Lib_General.lib_button import LayeredButton


class Surface:
    def __init__(self, window):
        # General
        game_menu_button_font = pygame.font.SysFont("impact", 40)
        # Init
        self.surface = pygame.surface.Surface((window.get_width(), window.get_height()))
        self.surface.fill((41, 43, 47))
        self.text_font = pygame.font.SysFont("arialblack", 40)
        # UI Elements
        self.text = self.text_font.render("Testing Surface", True, (255, 255, 255))
        self.game_honai_button = LayeredButton(
            "Honai",
            150,
            45,
            (button_pos("x_center_left", self.surface, 150, 45), 60),
            5,
            game_menu_button_font,
            (255, 0, 0),
            (100, 100, 100),
            (41, 43, 47),
        )
        # Rendering
        
    def render(self):
        self.surface.blit(self.text, (text_pos("center", self.surface, self.text)))
            
        if self.game_honai_button.draw(self.surface):
                pass
