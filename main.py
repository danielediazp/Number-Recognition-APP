"""This file runs the APP."""

import pygame
from UI.menu import MainMenu
from UI.configurations import RESOLUTION


if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode(RESOLUTION)
    menu = MainMenu(surface)
    menu.update()
