"""Defines the behavior of the Help Window. The help window opens within
the Predictio Window. The Help Window allows the user to clear the Prediction
Window, or switch back to the Main menu state.

    Typical usage:
        help_window = HelpWindow(surface=surface)
"""

import pygame
from .screen_state import CURRENT_STATE
from .change_button_color import change_buttons_color
from .button import Button


class HelpWindow:
    """Defines the behavior of the help window.

    Methods:
        __init__
        _handle_events
        update
    """

    #  Help Window set up.
    _WINDOW_FONT_PATH = (
        "../Number-Recognition-APP/UI/assets/Fonts/oswald/Oswald-Heavy.ttf"
    )
    _WINDOW_FONT_SIZE = 40
    _WINDOW_CAPTION = "Help Window"
    _WINDOW_BACKGROUND = ""
    _WINDOW_TITLE = "How to use?"
    _WINDOW_TITLE_POSITION = (145, 10)
    _WINDOW_TEXT_COLOR = "White"
    #  Buttons set up.
    _BACK_MENU_TEXT = "Open Main Menu"
    _BACK_MENU_POSITION = (620, 500)
    _BACK_PREDICTION_TEXT = "Back"
    _BACK_PREDICTION_POSITION = (180, 500)

    def __init__(self, surface: pygame.display) -> None:
        """Construct the Prediction Window object.

        Args:
            surface: screen
        """
        self._surface = surface
        self._back_prediction = Button(HelpWindow._BACK_PREDICTION_TEXT, HelpWindow._BACK_PREDICTION_POSITION)
        self._back_menu = Button(HelpWindow._BACK_MENU_TEXT, HelpWindow._BACK_MENU_POSITION)
        self._buttons = [self._back_menu, self._back_prediction]
        self._font = pygame.font.Font(HelpWindow._WINDOW_FONT_PATH, HelpWindow._WINDOW_FONT_SIZE)

    def _handle_events(self) -> None:
        """Handle the events happening in the screen."""
        for event in pygame.event.get():
            #  If the user quits by the window.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #  Get the user mouse position.
                mouse_position = pygame.mouse.get_pos()
                #  Check all buttons.
                if self._back_prediction.check_surface(mouse_position):
                    CURRENT_STATE.pop()
                    CURRENT_STATE[len(CURRENT_STATE) - 1].update()
                if self._back_menu.check_surface(mouse_position):
                    CURRENT_STATE.pop()
                    CURRENT_STATE.pop()
                    CURRENT_STATE[0].update()

    def update(self) -> None:
        """Executes the Help Window."""
        #  Reset the window.
        self._surface.fill("Black")
        #  Set the captio.
        pygame.display.set_caption(HelpWindow._WINDOW_CAPTION)

        #  Render the text.
        tile_text = self._font.render(HelpWindow._WINDOW_TITLE, True, HelpWindow._WINDOW_FONT_SIZE)

        while True:
            #  Display the title.
            self._surface.blit(tile_text, HelpWindow._WINDOW_TITLE_POSITION)
            #  Display the buttons.
            self._back_prediction.update(self._surface)
            self._back_menu.update(self._surface)
            #  Get the user mouse position.
            mouse_position = pygame.mouse.get_pos()
            #  Check if the user mouse is hovering the mouse.
            change_buttons_color(self._buttons, mouse_position, self._surface)
            #  Check the events.
            self._handle_events()
            #  Update the display.
            pygame.display.update()

