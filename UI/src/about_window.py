"""Defines the AboutWindow class that will be used to render the About Window.

Typical example usage:
    pygame.init()
    about_window = AboutWindow(surface=surface)
    about_window.update()
"""

import sys
import pygame
import webbrowser

from .button import Button
from .change_button_color import change_buttons_color
from .screen_state import CURRENT_STATE

class AboutWindow:
    """Defines the behavior of the About Window.

    Methods:
        __init__
        _handle_events
        update
    """
    def __init__(self, surface: pygame.display) -> None:
        self._surface = surface
        self._github_button = Button("Github", (250, 500), "Visit the Github repository!")
        self._back_button = Button("Back", (590, 560), "Go back to the main menu!")
        self._buttons = [self._github_button, self._back_button]
        self._background = pygame.image.load("UI/assets//MainMenu_background.png.png")
        self._font = pygame.font.Font("UI/assets//Fonts/Oswald-Regular.ttf", 100)
        
    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if self._github_button.check_surface(mouse_position):
                    webbrowser.open("https://github.com/danielediazp/Number-Recognition-APP")
                elif self._back_button.check_surface(mouse_position):
                    CURRENT_STATE.pop()
                    CURRENT_STATE[0].update()
    
    def update(self):
        pygame.display.set_caption("About")
        title_text = self._font.render("About", True, "#39FF14")
        
        while True:
            self._surface.blit(self._background, (0,0))
            self._surface.blit(title_text, (93, 45))
            self._github_button.update(self._surface)
            self._back_button.update(self._surface)
            mouse_position = pygame.mouse.get_pos()
            change_buttons_color(self._buttons, mouse_position, self._surface)
            self._handle_events()
            pygame.display.update()
