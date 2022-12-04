"""Class that define the behavior of the main menu"""

#  pylint: disable=locally-disabled, import-error
from typing import Any
import pygame
from UI.button import Button


#  pylint: disable=locally-disabled, no-member
#  pylint: disable=locally-disabled, too-many-instance-attributes
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
    _MAIN_MENU_BC = "../Number-Recognition-APP/UI/assets/Backgrounds/menubackground.png"
    _MAIN_MENU_TEXT = "Main Menu"
    _MAIN_MENU_FONT_PATH = (
        "../Number-Recognition-APP/UI/assets/Fonts/oswald/Oswald-Extra-LightItalic.ttf"
    )
    _MAIN_MENU_TEXT_COLOR = "#39FF14"
    _MAIN_MENU_TEXT_POSITION = (80, 50)
    #  Menu buttons set up
    _PREDICTION_BUTTON_TEXT = "Predict ?"
    _PREDICTION_BUTTON_POSITION = (250, 250)
    _ABOUT_BUTTON_TEXT = "About the project"
    _ABOUT_BUTTON_POSITION = (250, 400)
    _EXIT_BUTTON_TEXT = "Exit"
    _EXIT_BUTTON_POSITION = (250, 550)

    def __init__(self, surface: pygame.display) -> None:
        """Construct the menu object."""
        self._surface = surface
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
        """Handles the events happening in the screen. If the button is clicked, then
        a transition occurs.

        Returns:
            Any transition
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
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
            self._surface.blit(self._background, (0, 0))
            self._surface.blit(self._title_text, MainMenu._MAIN_MENU_TEXT_POSITION)
            self._prediction_button.update(self._surface)
            self._about_button.update(self._surface)
            self._exit_button.update(self._surface)
            mouse_position = pygame.mouse.get_pos()
            self.change_button_color(mouse_position, self._surface)
            self._handle_events()
            pygame.display.update()
