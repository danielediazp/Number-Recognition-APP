"""This class define the behavior of ther Main menu buttons. This class is a child class
of the Button class Please refer to button.py for details.

    Typical usage example:

"""

import pygame
from .button import Button


class MenuButton(Button):
    """Define the behavior and displays the Main Menu buttons.

    Methods:
        __init__
        display_description
    """

    #  Description text set up.
    _DESCRIPTION_TEXT_FONT_PATH = (
        "../Number-Recognition-APP/UI/assets/Fonts/oswald/Oswald-Demi-BoldItalic.ttf"
    )
    _DESCRIPTION_TEXT_FONT_COLOR = "#39FF14"
    _DESCRIPTION_TEXT_SIZE = 20

    def __init__(self, label: str, coord: tuple[int, int], description: str) -> None:
        """Constructs the MenuButton object.

        Args:
           label: The text inside the button.
           coord: x,y position of the button in the pygame surface.
           description: The text that will display once the button is hover by the user  mouse.
        """
        Button.__init__(self, label, coord)
        self._description = description
        self._description_font = pygame.font.Font(
            MenuButton._DESCRIPTION_TEXT_FONT_PATH, MenuButton._DESCRIPTION_TEXT_SIZE
        )
        self._description_text = self._description_font.render(
            self._description, True, MenuButton._DESCRIPTION_TEXT_FONT_COLOR
        )
        self._description_rect = self._description_text.get_rect(
            center=(coord[0] + 295, coord[1] + 10)
        )

    def display_description(
        self, coord: tuple[int, int], surface: pygame.display
    ) -> None:
        """Displays the description of the button next to the button in the screen."""
        if self.check_surface(coord):
            surface.blit(self._description_text, self._description_rect)
