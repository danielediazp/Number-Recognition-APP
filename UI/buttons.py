"""Defines the behavior of the buttons use throughout the app.

    Typical usage example:
        exit_button =  Button(label= ("Exit"), coords=(640, 640))
        """

import pygame
import pygame.font


class Button:
    """Class defines the behavior of a button object.

    Methods:
        __init__
        update
        check_surface
        change_color
    """

    #  Class native members
    #  TO DO:
    #  Get a font, and add this to a button config.py file
    _FONT_PATH = "../Number-Recognition-APP/UI/assets/Fonts/Oswald-Bold.tff"
    _BUTTON_BC_PATH = "../Number-Recognition-APP/UI/assets/BC/main_menu.png"
    _BUTTON_BC = pygame.image.load(_BUTTON_BC_PATH).convert_alpha()
    _HOVER_COLOR = "White"
    _BUTTON_COLOR = "#661B1C"
    _TEXT_FONT = pygame.font.Font(_FONT_PATH, 30)

    def __init__(self, label: str, coord: tuple[int, int]) -> None:
        """Construct the instance of a Button.

        Args:
            label: The text inside the button
            coord: x,y possition of the button in the pygame surface.
        """
        self._label = label
        self._coord = coord
        self._text = Button._TEXT_FONT.render(self._label, True, Button._BUTTON_COLOR)
        self._rect = Button._BUTTON_BC.get_rect(center=coord)
        self._text_rect = self._text.get_rect(center=coord)

    def update(self, surface: pygame.surface) -> None:
        """Draws the Button object in the pygame surface.

        Args:
            surface: pygame screen surface.
        """
        surface.blit(Button._BUTTON_BC, self._rect)
        surface.blit(self._label, self._text_rect)

    def _check_surface(self, coord: tuple[int, int]) -> bool:
        """Checks the button surface. If the user mouse is on top of the button surface,
        it returns True.

            Args:
                coord: x,y position of the user mouse.

            Returns:
                True / False
        """
        return (
            self._rect.left <= coord[0]
            and coord[0] <= self._rect.right
            and self._rect.top <= coord[1]
            and coord[1] <= self._rect.bottom
        )

    def change_color(self, coord: tuple[int, int]) -> None:
        """Changes the color of the Button text if the user mouse is hovering the Button.

        Args:
            coord: x,y position of the user mouse."""
        color = (
            Button._HOVER_COLOR if self._check_surface(coord) else Button._BUTTON_COLOR
        )
        self._text = Button._TEXT_FONT.render(self._label, True, color)
