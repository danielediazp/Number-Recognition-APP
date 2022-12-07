"""This file runs the APP."""

import pygame
from .menu import MainMenu
from .configurations import RESOLUTION
from .screen_state import CURRENT_STATE

def run() -> None:
    """Executes the UI."""
    pygame.init()
    surface = pygame.display.set_mode(RESOLUTION)
    menu = MainMenu(surface)
    CURRENT_STATE.append(menu)
    menu.update()
