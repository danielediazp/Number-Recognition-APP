"""Tests use to estimate the model accuracy in a real word situation. """

import pytest
import tensorflow as tf
import numpy as np
import cv2 as cv


#  Load the model.
MODEL = tf.keras.models.load_model("digits_recognition")
#  Variables to keep track of the accuracy
NUM_TEST = 13
NUM_PASS = 0


def test_1_0():
    """Test an image that contain the handwritten number 1."""


def test_1_1():
    """Test an image that contain the handwritten number 1."""


def test_2_0():
    """Test an image that contain the handwritten number 2."""


def test_2_1():
    """Test an image that contain the handwritten number 2."""


def test_3_0():
    """Test an image that contain the handwritten number 3."""


def test_3_1():
    """Test an image that contain the handwritten number 3."""


def test_4():
    """Test an image that contain the handwritten number 4."""


def test_5():
    """Test an image that contain the handwritten number 5."""


def test_6():
    """Test an image that contain the handwritten number 6."""


def test_7():
    """Test an image that contain the handwritten number 7."""


def test_8():
    """Test an image that contain the handwritten number 8."""


def test_9():
    """Test an image that contain the handwritten number 9."""


def test_10():
    """Test an image that contain the handwritten number 10."""
