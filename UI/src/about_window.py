"""Defines the AboutWindow class that will be used to render the About Window.

Typical example usage:
    pygame.init()
    about_window = AboutWindow(surface=surface)
    about_window.update()
"""

import sys
import pygame
from .button import Button


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
            
    
    def update(self):
        return None