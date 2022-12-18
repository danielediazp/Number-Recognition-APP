"""Changes the color of the buttons in the screen. This function is used in the
within Main Menu class, the Prediction Window class, the About Window class,
and the Help  Window class.
"""

import pygame
from .button import Button
from .menu_buttons import MenuButton


def change_buttons_color(
    buttons: list[MenuButton], mouse_position: tuple[int, int], surface: pygame.display
) -> None:
    """Checks if the user mouse is hovering any buttons in the screen.

    Args:
        buttons: A list containing all the buttons on the screen.
        mouse_position: Position of the user mouse.
        surface: Screen.
    """
    for button in buttons:
        button.change_color(mouse_position)
        try:
            button.display_description(mouse_position, surface)
        except:
            button.update(surface)
            continue
        button.update(surface)
