"""Defines the behavior of the Help Window. The help window opens within
the Prediction Window. The Help Window allows the user to return to the Prediction
Window, or switch back to the Main menu state. The purpose of the Help Window is to
explain the user how he should be drawing the digits in the scree.

    Typical usage:
        help_window = HelpWindow(surface=surface)
"""

import sys
import pygame
from .screen_state import CURRENT_STATE
from .change_button_color import change_buttons_color
from .button import Button
from .mouse_tracker import MouseTracker


class HelpWindow:
    """Defines the behavior of the help window.

    Methods:
        __init__
        _handle_events
        update
    """

    #  Help Window set up.
    _WINDOW_BACKGROUND_PATH = (
        "../Number-Recognition-APP/UI/assets/Backgrounds/helpWindow.png"
    )
    _WINDOW_FONT_PATH = (
        "../Number-Recognition-APP/UI/assets/Fonts/oswald/Oswald-Heavy.ttf"
    )
    _WINDOW_FONT_SIZE = 40
    _WINDOW_CAPTION = "Help Window"
    _WINDOW_TITLE = "User Guide"
    _WINDOW_TITLE_POSITION = (145, 10)
    _WINDOW_TEXT_COLOR = "White"
    #  Buttons set up.
    _BACK_MENU_TEXT = "Main Menu"
    _BACK_MENU_POSITION = (620, 600)
    _BACK_PREDICTION_TEXT = "Back"
    _BACK_PREDICTION_POSITION = (180, 600)
    #  Mouse Tracker set up
    _MOUSE_TRACKER_IMAGE_PATH = (
        "../Number-Recognition-APP/UI/assets/Backgrounds/sadface.png"
    )

    def __init__(self, surface: pygame.display) -> None:
        """Construct the Prediction Window object.

        Args:
            surface: screen
        """
        self._surface = surface
        self._back_prediction = Button(
            HelpWindow._BACK_PREDICTION_TEXT, HelpWindow._BACK_PREDICTION_POSITION
        )
        self._back_menu = Button(
            HelpWindow._BACK_MENU_TEXT, HelpWindow._BACK_MENU_POSITION
        )
        self._buttons = [self._back_menu, self._back_prediction]
        self._font = pygame.font.Font(
            HelpWindow._WINDOW_FONT_PATH, HelpWindow._WINDOW_FONT_SIZE
        )
        self._background = pygame.image.load(HelpWindow._WINDOW_BACKGROUND_PATH)

    def _handle_events(self) -> None:
        """Handle the events happening in the screen."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if self._back_prediction.check_surface(mouse_position):
                    CURRENT_STATE.pop()
                    CURRENT_STATE[len(CURRENT_STATE) - 1].update()
                if self._back_menu.check_surface(mouse_position):
                    CURRENT_STATE.pop()
                    CURRENT_STATE.pop()
                    CURRENT_STATE[0].update()

    def update(self) -> None:
        """Executes the Help Window."""
        self._surface.fill("Black")

        pygame.display.set_caption(HelpWindow._WINDOW_CAPTION)

        tile_text = self._font.render(
            HelpWindow._WINDOW_TITLE, True, HelpWindow._WINDOW_FONT_SIZE
        )

        mouse_tracker = MouseTracker(HelpWindow._MOUSE_TRACKER_IMAGE_PATH)

        while True:
            self._surface.blit(self._background, (0, 0))
            self._surface.blit(tile_text, HelpWindow._WINDOW_TITLE_POSITION)
            self._back_prediction.update(self._surface)
            self._back_menu.update(self._surface)
            mouse_position = pygame.mouse.get_pos()
            mouse_tracker.update(mouse_position, self._surface)
            change_buttons_color(self._buttons, mouse_position, self._surface)
            self._handle_events()
            pygame.display.update()
