"""Defines the  behavior of the Prediction Window. The Prediction
Window opens from the Main Menu Window. This window allows the user
to draw their digits in the display. Once the user draws their digits
in the screen, the image gets pre-process and fit into the neural network.
The prediction in then display to the user. This window allows a two-way
transaction between the Main Menu window and itself. Also, allows for the
transaction between the Prediction Window and Help Window.

    Typical usage:
        prediction_window = PredictionWindow(surface=surface)
        prediction_window.update()
"""

import sys
import time
import pygame
import tensorflow as tf
import cv2 as cv
import numpy as np
from PIL import Image
from resizeimage import resizeimage
from .button import Button
from .configurations import RESOLUTION
from .screen_state import CURRENT_STATE
from .change_button_color import change_buttons_color
from .help_window import HelpWindow
from .mouse_tracker import MouseTracker


class PredictionWindow:
    """Defines the behavior of the Prediction Window.

    Methods:
        __init__
         _handle_events
        _set_default_screen
        _surface_to_image
        _predict_image
        _display_prediction
        _handle_pause_menu
        _pause_menu
        update
    """

    #  Back button set up.
    _BACK_BUTTON_TEXT = "Back"
    _BACK_BUTTON_POSITION = (180, 500)
    #  Help button set up.
    _HELP_BUTTON_TEXT = "Help"
    _HELP_BUTTON_POSITION = (620, 500)
    #  Window caption set up.
    _WINDOW_CAPTION = "Prediction Window"
    #  Window label set up.
    _WINDOW_TEXT = "Write Your Digits"
    _WINDOW_TEXT_COLOR = "#39FF14"
    _WINDOW_TEXT_POSITION = (145, 10)
    _WINDOW_FONT_PATH = (
        "../Number-Recognition-APP/UI/assets/Fonts/oswald/Oswald-Heavy.ttf"
    )
    #  Load neural network.
    _MODEL = tf.keras.models.load_model("../Number-Recognition-APP/digits_recognition")
    #  Prediction Labels.
    _PREDICTION_LABELS = [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
    ]
    #  Screen circle set up.
    _CIRCLE_COLOR = "#FFFFFF"
    _CIRCLE_RADIUS = 30
    #  Transaction mode.
    _TRANSACTION_MODE = True
    _TRANSACTION_MODE_TEXT_0 = "Press any key to go"
    _TRANSACTION_MODE_TEXT_1 = "back to drawing mode."
    _TRANSACTION_MODE_TEXT_POSITION_0 = (100, 100)
    _TRANSACTION_MODE_TEXT_POSITION_1 = (90, 200)
    #  Pause Window Mouse Tracker set up.
    _MOUSE_TRACKER_IMAGE_PATH = (
        "../Number-Recognition-APP/UI/assets/Backgrounds/pen.png"
    )

    def __init__(self, surface: pygame.display):
        self._surface = surface
        self._back_button = Button(
            PredictionWindow._BACK_BUTTON_TEXT, PredictionWindow._BACK_BUTTON_POSITION
        )
        self._help_button = Button(
            PredictionWindow._HELP_BUTTON_TEXT, PredictionWindow._HELP_BUTTON_POSITION
        )
        self._buttons = [self._back_button, self._help_button]
        self._font = pygame.font.Font(PredictionWindow._WINDOW_FONT_PATH, 70)

    def _handle_events(self) -> None:
        """Handles all the events happening in the screen."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self._set_default_screen()
                else:
                    PredictionWindow._TRANSACTION_MODE = True
                    self._pause_menu()

    def _set_default_screen(self) -> None:
        """Sets the prediction drawing screen back to default after evert drawing."""
        pygame.display.set_caption(PredictionWindow._WINDOW_CAPTION)
        title_text = self._font.render(
            PredictionWindow._WINDOW_TEXT, True, PredictionWindow._WINDOW_TEXT_COLOR
        )
        self._surface.fill("Black")
        self._surface.blit(title_text, PredictionWindow._WINDOW_TEXT_POSITION)
        pygame.display.update()
        time.sleep(0.60)
        self._surface.fill("Black")
        pygame.display.flip()

    def _surface_to_image(self) -> np.array:
        """Converts the pygame display into a numpy array. This function converts the pygame
        surface into a np array."""
        pixels = pygame.image.tostring(self._surface, "RGBA")
        image = Image.frombytes("RGBA", RESOLUTION, pixels)
        image = resizeimage.resize_cover(image, [28, 28])
        image = np.asarray(image)
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        (_, image) = cv.threshold(image, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        image = image / 255
        image = np.reshape(image, (1, 28, 28, 1))
        return image

    def _predict_image(self) -> str:
        """Fits the user drawing to the network."""
        image = self._surface_to_image()
        prediction = PredictionWindow._MODEL.predict(image)
        prediction_idx = np.argmax(prediction)
        print(prediction_idx)
        return PredictionWindow._PREDICTION_LABELS[prediction_idx]

    def _display_prediction(self, prediction: str) -> None:
        """Prompt the number prediction to the user in the screen."""
        text = f"Number is {prediction}"
        prediction_text = self._font.render(
            text, True, PredictionWindow._WINDOW_TEXT_COLOR
        )
        prediction_text_rect = prediction_text.get_rect(
            center=(RESOLUTION[0] / 2, RESOLUTION[1] / 2)
        )
        self._surface.blit(prediction_text, prediction_text_rect)
        pygame.display.update()
        time.sleep(0.50)

    def _handle_pause_menu(self) -> None:
        """Executes the transaction that the user wants to perform."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                PredictionWindow._TRANSACTION_MODE = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if self._help_button.check_surface(mouse_position):
                    help_window = HelpWindow(self._surface)
                    CURRENT_STATE.append(help_window)
                    help_window.update()
                if self._back_button.check_surface(mouse_position):
                    CURRENT_STATE.pop()
                    CURRENT_STATE[0].update()

    def _pause_menu(self) -> None:
        """Allows the user to change the window state. The user clear the screen,
        go back to the Main Menu Window, or open the Prediction Window.
        """
        transaction_mode_text_0 = self._font.render(
            PredictionWindow._TRANSACTION_MODE_TEXT_0,
            True,
            PredictionWindow._WINDOW_TEXT_COLOR,
        )

        transaction_mode_text_1 = self._font.render(
            PredictionWindow._TRANSACTION_MODE_TEXT_1,
            True,
            PredictionWindow._WINDOW_TEXT_COLOR,
        )

        mouse_tracker = MouseTracker(PredictionWindow._MOUSE_TRACKER_IMAGE_PATH)

        while PredictionWindow._TRANSACTION_MODE:
            self._surface.fill("Black")
            self._surface.blit(
                transaction_mode_text_0,
                PredictionWindow._TRANSACTION_MODE_TEXT_POSITION_0,
            )
            self._surface.blit(
                transaction_mode_text_1,
                PredictionWindow._TRANSACTION_MODE_TEXT_POSITION_1,
            )
            self._help_button.update(self._surface)
            self._back_button.update(self._surface)
            mouse_position = pygame.mouse.get_pos()
            mouse_tracker.update(mouse_position, self._surface)
            pygame.display.flip()
            change_buttons_color(self._buttons, mouse_position, self._surface)
            self._handle_pause_menu()

        self.update()

    def update(self) -> None:
        """Executes the Prediction Window."""
        self._set_default_screen()

        window_time = 0
        drawing_time = 0
        drawing = False

        while True:
            if window_time - drawing_time >= 2 and drawing:
                prediction = self._predict_image()
                self._display_prediction(prediction)
                self._set_default_screen()
                window_time = 0
                drawing_time = 0
                drawing = False
                continue

            window_time = time.process_time()

            self._handle_events()

            if pygame.mouse.get_pressed()[0]:
                mouse_position = pygame.mouse.get_pos()
                pygame.draw.circle(
                    self._surface,
                    PredictionWindow._CIRCLE_COLOR,
                    mouse_position,
                    PredictionWindow._CIRCLE_RADIUS,
                )
                pygame.display.flip()
                drawing_time = time.process_time()
                drawing = True
