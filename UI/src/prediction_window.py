"""Defines the transitions between Main Menu and Prediction Window.

    Typical usage:
        prediction_window = PredictionWindow(surface=surface)
        prediction_window.update()
"""

#  pylint: disable=locally-disabled, relative-beyond-top-level
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
        "Sevent",
        "Eight",
        "Nine",
    ]
    #  Screen circle set up.
    _CIRCLE_COLOR = "#FFFFFF"
    _CIRCLE_RADIUS = 30

    def __init__(self, surface: pygame.display):
        self._surface = surface
        self._back_button = Button(
            PredictionWindow._BACK_BUTTON_TEXT, PredictionWindow._BACK_BUTTON_POSITION
        )
        self._clear_button = Button(
            PredictionWindow._CLEAR_BUTTON_TEXT, PredictionWindow._CLEAR_BUTTON_POSITION
        )
        self._buttons = [self._back_button, self._clear_button]
        self._font = pygame.font.Font(PredictionWindow._WINDOW_FONT_PATH, 70)

    def _set_default_screen(self) -> None:
        """Sets the prediction drawing screen back to default after evert drawing."""
        #  Set the screen name.
        pygame.display.set_caption(PredictionWindow._WINDOW_CAPTION)
        #  Render the screen title.
        title_text = self._font.render(
         PredictionWindow._WINDOW_TEXT, True, PredictionWindow._WINDOW_TEXT_COLOR
        )
        #  Fill the window with black.
        self._surface.fill("Black")
        #  Render the title in the screen.
        self._surface.blit(title_text, PredictionWindow._WINDOW_TEXT_POSITION)
        pygame.display.update()
        #  Set the screen to sleep for 2 seconds.
        time.sleep(0.60)
        #  Fill the screen black again
        self._surface.fill("Black")
        #  Update a certain part of the window.
        pygame.display.flip()

    def _surface_to_image(self) -> np.array:
        """Converts the pygame display into a numpy array. This function converts the pygame
        surface into a np array."""
        #  Collect the pixels from the screen.
        pixels = pygame.image.tostring(self._surface, "RGBA")
        #  Create a copy of the image pixels in a buffer.
        image = Image.frombytes("RGBA", RESOLUTION, pixels)
        #  Resize the image to a 28x28 format.
        image = resizeimage.resize_cover(image, [28, 28])
        #  Convert the image to a numpy array object.
        image = np.asarray(image)
        #  Convert the image to a gray scale.
        image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        #  Apply the threshold to the image.
        (_, image) = cv.threshold(image, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        #  Normalize the image.
        image = image / 255
        image = np.reshape(image, (1, 28, 28, 1))
        return image

    def _handle_events(self) -> None:
        """Handles all the events happening in the screen."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                CURRENT_STATE.pop()
                CURRENT_STATE[0].update()


    def _predict_image(self) -> str:
        """"""
        #  Get the image.
        image = self._surface_to_image()
        #  Fit the image into the neural network.
        prediction = PredictionWindow._MODEL.predict(image)
        #  Get the prediction label.
        prediction_idx = np.argmax(prediction)
        print(prediction_idx)
        return PredictionWindow._PREDICTION_LABELS[prediction_idx]

    def _display_prediction(self, prediction: str) -> None:
        """Prompt the number prediction to the user in the screen."""
        #  Create the prediction text.
        text = f"Number is {prediction}"
        prediction_text = self._font.render(
            text, True, PredictionWindow._WINDOW_TEXT_COLOR
        )
        #  Create a prediction text rect center in the middle of the screen.
        prediction_text_rect = prediction_text.get_rect(
            center=(RESOLUTION[0] / 2, RESOLUTION[1] / 2)
        )
        #  Display the prediction.
        self._surface.blit(prediction_text, prediction_text_rect)
        #  Update the screen.
        pygame.display.update()
        #  put the window to sleep for 2 seconds
        time.sleep(0.50)

    def update(self) -> None:
        """Executes the Prediction Window."""
        #  Set the screen to default.
        self._set_default_screen()

        #  Variables to keep track of the user draw.
        window_time = 0
        drawing_time = 0
        drawing = False

        #  Execution loop.
        while True:
            #  User has drawn something in the screen.
            if window_time - drawing_time >= 2 and drawing:
                #  Make a prediction of the digit.
                prediction = self._predict_image()
                #  Prompt the prediction to the user.
                self._display_prediction(prediction)
                #  Set the screen bak to default.
                self._set_default_screen()
                #  Reset the screen timers.
                window_time = 0
                drawing_time = 0
                #  Reset drawing.
                drawing = False
                continue

            #  Get window time.
            window_time = time.process_time()

            #  Check for events.
            self._handle_events()

            #  Check if the user is drawing.
            if pygame.mouse.get_pressed()[0]:
                #  Get the user mouse position.
                mouse_position = pygame.mouse.get_pos()
                #  Draw a circle in the screen.
                pygame.draw.circle(
                    self._surface,
                    PredictionWindow._CIRCLE_COLOR,
                    mouse_position,
                    PredictionWindow._CIRCLE_RADIUS,
                )
                #  Update a portion of the pygame display.
                pygame.display.flip()
                #  Get drawing time.
                drawing_time = time.process_time()
                drawing = True
