"""This file runs the APP."""

import pygame
from UI.menu import MainMenu
from UI.configurations import RESOLUTION
from UI.screen_state import CURRENT_STATE

if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode(RESOLUTION)
    menu = MainMenu(surface)
    CURRENT_STATE.append(menu)
    menu.update()
