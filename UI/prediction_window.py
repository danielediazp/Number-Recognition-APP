"""Defines the transitions between Main Menu and Prediction Window.

    Typical usage:
        prediction_window = PredictionWindow(surface=sufrace)
        prediction_window.update()
"""

#  pylint: disable=locally-disabled, import-error
import sys
import pygame
import tensorflow as tf
import cv2 as cv
import numpy as np
from UI.button import Button
from UI.change_button_color import change_buttons_color
from UI.configurations import RESOLUTION


#  pylint: disable=locally-disabled, no-member
#  pylint: disable=locally-disabled, too-few-public-methods
class PredictionWindow:
    """Defines the behavior of the Prediction Window.

    Methods:
        __init__
        update
        _handle_events
    """

    #  Back button set up.
    _BACK_BUTTON_TEXT = "Back"
    _BACK_BUTTON_POSITION = (400, 700)
    #  Clear button set up.
    _CLEAR_BUTTON_TEXT = "Clear Window"
    _CLEAR_BUTTON_POSITION = (1000, 700)
    #  Window label set up.
    _WINDOW_TEXT = "Writte Your Digits"
    _WINDOW_TEXT_COLOR = "#39FF14"
    _WINDOW_TEXT_POSITION = (300, 10)
    _WINDOW_FONT_PATH = (
        "../Number-Recognition-APP/UI/assets/Fonts/oswald/Oswald-Heavy.ttf"
    )
    #  Load neural network.
    _MODEL = tf.keras.models.load_model("../Number-Recognition-APP/digits_recognition")
    #  COLORS
    _NEON = "#39FF14"
    _RED = "#FF0000"
    _BOUNDRIES = 10
    # set up for Digit recognition
    _PRDICT = True
    _DRAWING = False
    _X_COORDS = []
    _Y_COORDS = []
    def __init__(self, surface: pygame.display):
        self._surface = surface
        self._back_button = Button(
            PredictionWindow._BACK_BUTTON_TEXT, PredictionWindow._BACK_BUTTON_POSITION
        )
        self._clear_button = Button(
            PredictionWindow._CLEAR_BUTTON_TEXT, PredictionWindow._CLEAR_BUTTON_POSITION
        )
        self._buttons = [self._back_button, self._clear_button]
        self._font = pygame.font.Font(PredictionWindow._WINDOW_FONT_PATH, 100)

    def _handle_events(self) -> None:
        """Handles the events happening in the screen"""
        for event in pygame.event.get():
            #  If the user quits by the window.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #  Check if the user wants to press a button.
            """if event.type == pygame.MOUSEBUTTONDOWN:
                #  Get the user mouse positon.
                mouse_position = pygame.mouse.get_pos()
                #  Check all buttons.
                if self._clear_button.check_surface(mouse_position):
                    self.update()
                if self._back_button.check_surface(mouse_position):
                    pygame.quit()
                    sys.exit()"""
            #  Draw a circle while the user mouse is down.
            if event.type == pygame.MOUSEMOTION and PredictionWindow._DRAWING:
                coords = pygame.mouse.get_pos()
                pygame.draw.circle(self._surface, PredictionWindow._NEON, coords, 4, 0)
                PredictionWindow._X_COORDS.append(coords[0])
                PredictionWindow._Y_COORDS.append(coords[1])

            if event.type == pygame.MOUSEBUTTONDOWN:
                PredictionWindow._DRAWING = True

            if event.type == pygame.MOUSEBUTTONUP and len(PredictionWindow._X_COORDS) > 0:
                PredictionWindow._DRAWING = False
                #  Once done make a prediciton.
                PredictionWindow._X_COORDS = sorted(PredictionWindow._X_COORDS)
                PredictionWindow._Y_COORDS = sorted(PredictionWindow._Y_COORDS)
                #  Create the rectangle.
                rect_left_x = max(PredictionWindow._X_COORDS[0] - PredictionWindow._BOUNDRIES, 0)
                rect_right_x = min(RESOLUTION[0], PredictionWindow._X_COORDS[-1] + PredictionWindow._BOUNDRIES)
                rect_left_y = max(PredictionWindow._Y_COORDS[0] - PredictionWindow._BOUNDRIES, 0)
                rect_right_y = min(PredictionWindow._Y_COORDS[-1] + PredictionWindow._BOUNDRIES, RESOLUTION[1])
                #  Clear the list.
                PredictionWindow._X_COORDS.clear()
                PredictionWindow._Y_COORDS.clear()
                if PredictionWindow._PRDICT:
                    #  get the image and transpose this image.
                    image = np.array(pygame.PixelArray(self._surface))[rect_left_x:rect_right_x,
                            rect_left_y:rect_right_y].T.astype(np.float32)
                    #  Resize the image.
                    image = cv.resize(image, (28, 28))
                    #  Add 10 pixeles to not lose any information.
                    image = np.pad(image, (10, 10), "constant", constant_values=0)
                    #  Resize again.
                    image = cv.resize(image, (28, 28)) / 255
                    #  Predict .
                    prediction = np.argmax(PredictionWindow._MODEL.predict(image.reshape(1, 28, 28, 1)))
                    #  Render the prediction.
                    prediction_text = self._font.render(str(prediction), True, PredictionWindow._RED,
                                                        PredictionWindow._NEON)
                    self._surface.blit(prediction_text, (rect_left_x, rect_right_y))
            pygame.display.update()

    def update(self) -> None:
        """Executes the Prediction Window."""
        #  Render the title.
        title_text = self._font.render(
            PredictionWindow._WINDOW_TEXT, True, PredictionWindow._WINDOW_TEXT_COLOR
        )

        self._surface.fill("black")
        pygame.display.update()
        while True:
            self._handle_events()

