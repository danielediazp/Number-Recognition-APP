"""Tests use to estimate the model accuracy in a real word situation. """

import tensorflow as tf
import numpy as np
import cv2 as cv

#  Load the model.
MODEL = tf.keras.models.load_model("../Number-Recognition-APP/digits_recognition")

#  pylint: disable=locally-disabled, no-member
def test_1_0():
    """Test an image that contain the handwritten number 1."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/one_0.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 1


def test_1_1():
    """Test an image that contain the handwritten number 1."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/one_1.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 1


def test_2_0():
    """Test an image that contain the handwritten number 2."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/two_0.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 2


def test_2_1():
    """Test an image that contain the handwritten number 2."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/two_1.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 2


def test_3_0():
    """Test an image that contain the handwritten number 3."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/three_0.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 3


def test_3_1():
    """Test an image that contain the handwritten number 3."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/three_1.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 3


def test_4():
    """Test an image that contain the handwritten number 4."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/four.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 4


def test_5():
    """Test an image that contain the handwritten number 5."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/five.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 5


def test_6():
    """Test an image that contain the handwritten number 6."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/six.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 6


def test_7():
    """Test an image that contain the handwritten number 7."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/sevent.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 7


def test_8():
    """Test an image that contain the handwritten number 8."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/eight.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 8


def test_9():
    """Test an image that contain the handwritten number 9."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/nine.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 9


def test_10():
    """Test an image that contain the handwritten number 10."""
    #  Load image
    image = cv.imread("../Number-Recognition-APP/test_images/ten.png")[:, :, 0]
    #  Convert the image to a numpy array and invert it
    image = np.invert(np.array([image]))
    #  Request the model prediction.
    prediction = np.argmax(MODEL.predict(image))
    assert prediction == 0
