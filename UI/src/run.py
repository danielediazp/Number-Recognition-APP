"""This file runs the APP."""

import pygame
from .menu import MainMenu
from .configurations import RESOLUTION
from .screen_state import CURRENT_STATE



def execute() -> None:
    """Executes the UI."""
    icon = (
        "../Number-Recognition-APP/UI/assets/Backgrounds/pen.png"
    )
    image_icon = pygame.image.load(icon)
    pygame.init()
    surface = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_icon(image_icon)
    menu = MainMenu(surface)
    CURRENT_STATE.append(menu)
    menu.update()
