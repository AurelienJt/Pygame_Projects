import pygame
from Legacies.game_hanoi import Hanoi
from Libraries.Lib_General.lib_general import *
from Libraries.Lib_General.lib_button import LayeredButton

# pygame.init()

# window.get_width() = 1200
# HEIGHT = 600

# info = pygame.display.Info()
# win = pygame.display.set_mode((window.get_width(), HEIGHT))
# clock = pygame.time.Clock()
# FPS = 60
# running = True


class UI_Hanoi:
    def __init__(self, window):
        # General
        self.menu_id = "Hanoi"
        self.current_menu = self.menu_id

        # Define pole properties
        self.POLE_WIDTH = 20
        self.POLE_HEIGHT = 280
        self.POLE_COLOR = (128, 128, 128)  # RGB for grey
        self.margin = 280

        # Define object properties

        # Calculate spacing
        self.total_spacing = window.get_width() - (3 * self.POLE_WIDTH)
        self.spacing = self.total_spacing // 4

        # Objects
        self.big_color = (250, 0, 0)
        self.med_color = (0, 255, 0)
        self.small_color = (0, 0, 255)
        self.button_color = (171, 219, 177)

        self.big_width = 200
        self.med_width = 150
        self.small_width = 100
        self.obj_height = 50

        # Predefined Positions

        self.transit = [None, None]

        self.poles = {0: ["big", "med", "small"], 1: [], 2: []}

        self.layer_big = 1
        self.layer_med = 2
        self.layer_small = 3

        self.row_big = 0
        self.row_med = 0
        self.row_small = 0

        UI_Hanoi.update(self)
        # Buttons
        self.button_font = pygame.font.SysFont("arialblack", 40)

        self.button_s_1 = LayeredButton(
            "1",
            50,
            50,
            (60, 240),
            5,
            self.button_font,
            self.button_color,
            (100, 100, 100),
            (41, 43, 47),
        )
        self.button_s_2 = LayeredButton(
            "2",
            50,
            50,
            (60, 300),
            5,
            self.button_font,
            self.button_color,
            (100, 100, 100),
            (41, 43, 47),
        )
        self.button_s_3 = LayeredButton(
            "3",
            50,
            50,
            (60, 360),
            5,
            self.button_font,
            self.button_color,
            (100, 100, 100),
            (41, 43, 47),
        )

        self.button_d_1 = LayeredButton(
            "1",
            50,
            50,
            (window.get_width() - (60 + 50), 240),
            5,
            self.button_font,
            self.button_color,
            (100, 100, 100),
            (41, 43, 47),
        )
        self.button_d_2 = LayeredButton(
            "2",
            50,
            50,
            (window.get_width() - (60 + 50), 300),
            5,
            self.button_font,
            self.button_color,
            (100, 100, 100),
            (41, 43, 47),
        )
        self.button_d_3 = LayeredButton(
            "3",
            50,
            50,
            (window.get_width() - (60 + 50), 360),
            5,
            self.button_font,
            self.button_color,
            (100, 100, 100),
            (41, 43, 47),
        )

        self.button_play = LayeredButton(
            "Move",
            200,
            50,
            (500, 180),
            5,
            self.button_font,
            self.button_color,
            (100, 100, 100),
            (41, 43, 47),
        )
        self.button_replay = LayeredButton(
            "Play Again",
            300,
            60,
            (450, 380),
            5,
            self.button_font,
            (212, 173, 89),
            (100, 100, 100),
            (41, 43, 47),
        )

        # General
        self.surface = pygame.surface.Surface((window.get_width(), window.get_height()))
        self.surface.fill((41, 43, 47))

        # Persistent UI
        for self.i in range(3):
            pygame.draw.rect(
                self.surface,
                self.POLE_COLOR,
                pygame.Rect(
                    (self.i + 1) * self.spacing + self.i * self.POLE_WIDTH,
                    self.margin,
                    self.POLE_WIDTH,
                    self.POLE_HEIGHT,
                ),
            )

        pygame.draw.rect(
            self.surface,
            (0, 0, 0),
            pygame.Rect(
                self.spacing - 180,
                560,
                2 * (self.spacing + self.POLE_WIDTH) + 360 + self.POLE_WIDTH,
                5,
            ),
        )
        self.menu_title_font = pygame.font.SysFont("arialblack", 60)
        self.menu_title = self.menu_title_font.render(
            "Tour d'Hanoi", True, (255, 255, 255)
        )
        self.finish_message = self.menu_title_font.render(
            "You won! (Kinda easy game...)", True, (255, 0, 0)
        )

    def update(self):
        for key, value_list in self.poles.items():
            if "big" in value_list:
                self.row_big = key
                self.layer_big = value_list.index("big") + 1

            if "med" in value_list:
                self.row_med = key
                self.layer_med = value_list.index("med") + 1

            if "small" in value_list:
                self.row_small = key
                self.layer_small = value_list.index("small") + 1

        print(self.poles)

    def move(self):
        if len(self.poles[self.transit[0]]) > 0:
            target = self.poles[self.transit[0]][-1]
            self.poles[self.transit[0]].pop(-1)
            self.poles[self.transit[1]].append(target)

        print(self.row_big)
        print(self.layer_big)

    def check_rule(self):
        try:
            transferred = self.poles[self.transit[0]][-1]
            if len(self.poles[self.transit[1]]) != 0:
                host = self.poles[self.transit[1]][-1]
                if transferred == "big":
                    return False
                elif transferred == "med" and host == "small":
                    return False
                return True
            else:
                return True
        except:
            return False

    def check_won(self):
        win_situation = ["big", "med", "small"]
        if self.poles[2] == win_situation:
            return True

    def render(self):
        self.current_menu = self.menu_id
        
        self.surface.fill((41, 43, 47))
        for self.i in range(3):
            pygame.draw.rect(
                self.surface,
                self.POLE_COLOR,
                pygame.Rect(
                    (self.i + 1) * self.spacing + self.i * self.POLE_WIDTH,
                    self.margin,
                    self.POLE_WIDTH,
                    self.POLE_HEIGHT,
                ),
            )


        pygame.draw.rect(
            self.surface,
            (0, 0, 0),
            pygame.Rect(
                self.spacing - 180,
                560,
                2 * (self.spacing + self.POLE_WIDTH) + 360 + self.POLE_WIDTH,
                5,
            ),
        )

        if self.button_s_1.draw(self.surface):
            self.transit[0] = 0
        if self.button_s_2.draw(self.surface):
            self.transit[0] = 1
        if self.button_s_3.draw(self.surface):
            self.transit[0] = 2
        if self.button_d_1.draw(self.surface):
            self.transit[1] = 0
        if self.button_d_2.draw(self.surface):
            self.transit[1] = 1
        if self.button_d_3.draw(self.surface):
            self.transit[1] = 2
        if self.button_play.draw(self.surface):
            if UI_Hanoi.check_rule(self):
                UI_Hanoi.move(self)
                UI_Hanoi.update(self)

        # Big Object
        pygame.draw.rect(
            self.surface,
            self.big_color,
            pygame.Rect(
                self.row_big * (self.spacing + self.POLE_WIDTH)
                + (self.spacing + (self.POLE_WIDTH // 2))
                - (self.big_width // 2),
                self.margin + self.POLE_HEIGHT - (self.layer_big * self.obj_height),
                self.big_width,
                self.obj_height,
            ),
        )
        # Med Object
        pygame.draw.rect(
            self.surface,
            self.med_color,
            pygame.Rect(
                self.row_med * (self.spacing + self.POLE_WIDTH)
                + (self.spacing + (self.POLE_WIDTH // 2))
                - (self.med_width // 2),
                self.margin + self.POLE_HEIGHT - (self.layer_med * self.obj_height),
                self.med_width,
                self.obj_height,
            ),
        )
        # Small Object
        pygame.draw.rect(
            self.surface,
            self.small_color,
            pygame.Rect(
                self.row_small * (self.spacing + self.POLE_WIDTH)
                + (self.spacing + (self.POLE_WIDTH // 2))
                - (self.small_width // 2),
                self.margin + self.POLE_HEIGHT - (self.layer_small * self.obj_height),
                self.small_width,
                self.obj_height,
            ),
        )

        self.surface.blit(
            self.menu_title, (text_pos("x_center", self.surface, self.menu_title), 60)
        )
        
        if self.transit[0] is not None:
            self.sender_message = self.button_font.render(str(self.transit[0]+1),True,(255,255,255))
            self.surface.blit(
                self.sender_message,(70,400)
            )
        
        if self.transit[1] is not None:
            self.destination_message = self.button_font.render(str(self.transit[1]+1),True,(255,255,255))
            self.surface.blit(
                self.destination_message,(1100,400)
            )

        # Finish Screen
        if UI_Hanoi.check_won(self):
            self.surface.blit(
                self.finish_message,
                (text_pos("x_center", self.surface, self.finish_message), 200),
            )
            if self.button_replay.draw(self.surface):
                self.poles = {0: ["big", "med", "small"], 1: [], 2: []}
                UI_Hanoi.update(self)
        self.current_menu = self.menu_id
        return self.surface


# v1 = UI_Hanoi(win)

# while running:
#     win.blit(v1.render(), (0, 0))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             pygame.quit()
#             exit()

#     clock.tick(FPS)
#     pygame.display.update()
