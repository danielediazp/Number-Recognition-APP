"""This file runs the APP."""

import pygame
from .menu import MainMenu
from .configurations import RESOLUTION
from .screen_state import CURRENT_STATE

#  pylint: disable=locally-disabled, no-member


def execute() -> None:
    """Executes the UI."""
    #  Icon.
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
