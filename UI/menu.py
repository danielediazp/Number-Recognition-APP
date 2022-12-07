"""Class that define the behavior of the main menu.

    Typical usage:
        pygame.init()
        menu = MainMenu(surface=surface)
        menu.update()
    """

#  pylint: disable=locally-disabled, import-error
import sys
import pygame
from .button import Button
from .prediction_window import PredictionWindow
from .about_window import AboutWindow
from .change_button_color import change_buttons_color
from .screen_state import CURRENT_STATE


#  pylint: disable=locally-disabled, no-member
#  pylint: disable=locally-disabled, too-few-public-methods
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

    def _handle_events(self) -> None:
        """Handles the events happening in the screen. If the button is clicked, then
        a transition occurs.

        Returns:
            Any transition
        """
        for event in pygame.event.get():
            #  If the user quits by the window.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #  Get the user mouse position
                mouse_position = pygame.mouse.get_pos()
                #  Check all buttons.
                if self._prediction_button.check_surface(mouse_position):
                    prediciton_window = PredictionWindow(self._surface)
                    CURRENT_STATE.append(prediciton_window)
                    prediciton_window.update()
                elif self._about_button.check_surface(mouse_position):
                    CURRENT_STATE.append(AboutWindow)
                elif self._exit_button.check_surface(mouse_position):
                    pygame.quit()
                    sys.exit()

    def update(self) -> None:
        """Executes the Main Menu."""
        #  Set the window capition.
        pygame.display.set_caption(MainMenu._MAIN_MENU_TEXT)

        #  Render title
        title_text = self._font.render(
            MainMenu._MAIN_MENU_TEXT, True, MainMenu._MAIN_MENU_TEXT_COLOR
        )

        while True:
            #  Draw the background.
            self._surface.blit(self._background, (0, 0))
            #  Draw the window title.
            self._surface.blit(title_text, MainMenu._MAIN_MENU_TEXT_POSITION)
            #  Draw the buttons.
            self._prediction_button.update(self._surface)
            self._about_button.update(self._surface)
            self._exit_button.update(self._surface)
            #  Get the user mouse position.
            mouse_position = pygame.mouse.get_pos()
            #  Check if the user mouse is hovering a button.
            change_buttons_color(self._buttons, mouse_position, self._surface)
            #  Check for any event.
            self._handle_events()
            #  Update the display.
            pygame.display.update()
