"""Changes the color of the buttons in the screen. This function is used in the
Main Menu class, the Prediction Window class, and the About Window class."""

#  pylint: disable=locally-disabled, import-error
import pygame
from UI.button import Button


def change_buttons_color(
    buttons: list[Button], mouse_position: tuple[int, int], surface: pygame.display
) -> None:
    """Checks if the user mouse is hovering any buttons in the screen.

    Args:
        buttons: A list containing all the buttons on the screen.
        mouse_position: Position of the user mouse.
        surface: Screen.
    """
    for button in buttons:
        button.change_color(mouse_position)
        button.update(surface)
