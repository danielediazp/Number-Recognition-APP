"""Class that define the behavior of the main menu"""

from typing import Any
import pygame
from pygame.locals import *
from buttons import Button
from configurations import RESOLUTION

surface = pygame.display.set_mode(RESOLUTION)


class MainMenu:
    """Class designed to represent the transition between states in the UI.

    Methods:
        __init__
        _handle_events
        _change_button_color
        predict
        about
        update
    """

    #  Menu object set up
    _MAIN_MENU_DIMENSIONS = (1350, 850)
    _MAIN_MENU_BC = "../UI/assets/BC/menubc.png"
    _MAIN_MENU_TEXT = "Main Menu"
    _MAIN_MENU_FONT_PATH = "../UI/assets/Fonts/oswald/Oswald-Extra-LightItalic.ttf"
    _MAIN_MENU_TEXT_COLOR = "#39FF14"
    #  Menu buttons set up
    _PREDICTION_BUTTON_TEXT = "Predict ?"
    _PREDICTION_BUTTON_POSITION = (655, 250)
    _ABOUT_BUTTON_TEXT = "About the project"
    _ABOUT_BUTTON_POSITION = (655, 400)
    _EXIT_BUTTON_TEXT = "Exit"
    _EXIT_BUTTON_POSITION = (655, 550)

    def __init__(self) -> None:
        """Construct the menu object."""
        self._prediction_button = Button(
            MainMenu._PREDICTION_BUTTON_TEXT, MainMenu._PREDICTION_BUTTON_POSITION
        )
        self._about_button = Button(
            MainMenu._ABOUT_BUTTON_TEXT, MainMenu._ABOUT_BUTTON_POSITION
        )
        self._exit_button = Button(
            MainMenu._EXIT_BUTTON_TEXT, MainMenu._EXIT_BUTTON_POSITION
        )
        self._buttons = [self._prediction_button, self._about_button, self._exit_button]
        self._background = pygame.image.load(MainMenu._MAIN_MENU_BC)
        self._font = pygame.font.Font(MainMenu._MAIN_MENU_FONT_PATH, 100)

        self._title_text = self._font.render(
            MainMenu._MAIN_MENU_TEXT, True, MainMenu._MAIN_MENU_TEXT_COLOR
        )

    def _handle_events(self) -> Any:
        """Handles the events happening in the screen. If the button is clicked, then a transition occurs.

        Returns:
            Any transition
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if self._prediction_button.check_surface(mouse_position):
                    pygame.quit()
                elif self._about_button.check_surface(mouse_position):
                    pygame.quit()
                elif self._exit_button.check_surface(mouse_position):
                    pygame.quit()

    def change_button_color(
        self, mouse_position: tuple[int, int], surface: pygame.display
    ) -> None:
        """Checks if the user mouse is hovering any buttons in the screen.

        Args:
            mouse_position: position of the user mouse.
            surface: screen
        """
        for button in self._buttons:
            button.change_color(mouse_position)
            button.update(surface)

    def update(self) -> None:
        """Executes the Main Menu."""
        render = True
        while render:
            surface.blit(self._background, (0, 0))
            surface.blit(self._title_text, (320, 50))
            self._prediction_button.update(surface)
            self._about_button.update(surface)
            self._exit_button.update(surface)
            self._handle_events()
            mouse_position = pygame.mouse.get_pos()
            self.change_button_color(mouse_position, surface)
            pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    menu = MainMenu()
    menu.update()
