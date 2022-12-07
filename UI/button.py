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

    #  Button object set up.
    _FONT_PATH = "../Number-Recognition-APP/UI/assets/Fonts/oswald/Oswald-Bold.ttf"
    _BUTTON_BC_PATH = "../Number-Recognition-APP/UI/assets/Backgrounds/button2.png"
    _HOVER_COLOR = "#39FF14"
    _BUTTON_COLOR = "White"

    def __init__(self, label: str, coord: tuple[int, int]) -> None:
        """Construct the instance of a Button.

        Args:
            label: The text inside the button.
            coord: x,y position of the button in the pygame surface.
        """
        self._label = label
        self._coord = coord
        self._button_bc = pygame.image.load(Button._BUTTON_BC_PATH).convert_alpha()
        self._font = pygame.font.Font(Button._FONT_PATH, 30)
        self._text = self._font.render(self._label, True, Button._BUTTON_COLOR)
        self._rect = self._button_bc.get_rect(center=coord)
        self._text_rect = self._text.get_rect(center=coord)

    def update(self, surface: pygame.surface) -> None:
        """Draws the Button object in the pygame surface.

        Args:
            surface: pygame screen surface.
        """
        surface.blit(self._button_bc, self._rect)
        surface.blit(self._text, self._text_rect)

    def check_surface(self, coord: tuple[int, int]) -> bool:
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
            coord: x,y position of the user mouse.
        """
        color = (
            Button._HOVER_COLOR if self.check_surface(coord) else Button._BUTTON_COLOR
        )
        self._text = self._font.render(self._label, True, color)
