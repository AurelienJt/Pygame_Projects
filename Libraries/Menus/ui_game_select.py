import pygame
from Libraries.Lib_General.lib_general import text_pos, button_pos
from Libraries.Lib_General.lib_button import LayeredButton


class Game_Selector:
    def __init__(self, window):
        # General
        self.menu_id = "GameSelector"
        self.current_menu = self.menu_id
        
        game_menu_button_font = pygame.font.SysFont("impact", 40)
        row_1 = 150
        # Init
        self.surface = pygame.surface.Surface((window.get_width(), window.get_height()))
        self.surface.fill((41, 43, 47))
        self.text_font = pygame.font.SysFont("arialblack", 40)
        # UI Elements
        self.text = self.text_font.render("Game Selector", True, (255, 255, 255))
        self.game_honai_button = LayeredButton(
            "Honai",
            200,
            50,
            (button_pos("x_center_right", self.surface, 150, 45), row_1),
            5,
            game_menu_button_font,
            (93, 207, 123),
            (100, 100, 100),
            (41, 43, 47),
        )
        self.game_hangman_button = LayeredButton(
            "Hangman",
            200,
            50,
            (button_pos("x_center_left", self.surface, 150, 45), row_1),
            5,
            game_menu_button_font,
            (93, 207, 123),
            (100, 100, 100),
            (41, 43, 47),
        )
        
    def render(self):
        self.current_menu = self.menu_id
        #Rendering
        self.surface.blit(self.text, (text_pos("x_center", self.surface, self.text),60))
        if self.game_honai_button.draw(self.surface):
             self.current_menu = "Hanoi"
        if self.game_hangman_button.draw(self.surface):
            pass
        
