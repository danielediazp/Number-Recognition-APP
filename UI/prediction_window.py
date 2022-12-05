"""Defines the transitions between Main Menu and Prediction Window.

    Typical usage:
        prediction_window = PredictionWindow(surface=sufrace)
        prediction_window.update()
"""

#  pylint: disable=locally-disabled, import-error
import sys
import time
import pygame
import tensorflow as tf
import cv2 as cv
import numpy as np
from PIL import Image
from resizeimage import resizeimage
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

    def update(self) -> None:
        """Executes the Prediction Window."""
        #  Render the title.
        tile_text = self._font.render(
            PredictionWindow._WINDOW_TEXT, True, PredictionWindow._WINDOW_TEXT_COLOR
        )

        while True:
            self._surface.fill("Black")
            self._surface.blit(tile_text, PredictionWindow._WINDOW_TEXT_POSITION)
            pygame.display.update()
