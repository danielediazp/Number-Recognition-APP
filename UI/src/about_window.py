"""Defines the AboutWindow class that will be used to render the About Window.

Typical example usage:
    pygame.init()
    about_window = AboutWindow(surface=surface)
    about_window.update()
"""

import sys
import webbrowser
import pygame

from .button import Button
from .change_button_color import change_buttons_color
from .screen_state import CURRENT_STATE


class AboutWindow:
    """Defines the behavior of the About Window.

    Methods:
        __init__
        _handle_events
        update
    """

    def __init__(self, surface: pygame.display) -> None:
        """Inits AboutWindow with the surface to draw on.
        
        Args:
            surface (pygame.display): Surface to draw on.
        """
        self._surface = surface
        self._github_button = Button("GitHub", (210, 560))
        self._back_button = Button("Back", (590, 560))
        self._buttons = [self._github_button, self._back_button]
        self._background = pygame.image.load(
            "../Number-Recognition-APP/UI/assets/Backgrounds/MainMenu_background.png"
        )
        self._title_font = pygame.font.Font(
            "../Number-Recognition-APP/UI/assets/Fonts/oswald/Oswald-Regular.ttf", 100
        )
        self._body_font = pygame.font.Font("../Number-Recognition-APP/UI/assets/Fonts/oswald/Oswald-Regular.ttf", 20)

    def _handle_events(self) -> None:
        """Handles the events of the About Window."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if self._github_button.check_surface(mouse_position):
                    webbrowser.open(
                        "https://github.com/danielediazp/Number-Recognition-APP"
                    )
                elif self._back_button.check_surface(mouse_position):
                    CURRENT_STATE.pop()
                    CURRENT_STATE[0].update()

    def update(self):
        """Uodates the About Window. Used to manage the state of the window."""
        pygame.display.set_caption("About")
        title_text = self._title_font.render("About", True, "#39FF14")
        body_text = self._body_font.render("A number-recognition app made in Python. For more information, visit the GitHub repository.", True, "#FFFFFF")

        while True:
            self._surface.blit(self._background, (0, 0))
            self._surface.blit(title_text, (93, 45))
            self._surface.blit(body_text, (93, 275))
            self._github_button.update(self._surface)
            self._back_button.update(self._surface)
            mouse_position = pygame.mouse.get_pos()
            change_buttons_color(self._buttons, mouse_position, self._surface)
            self._handle_events()
            pygame.display.update()
