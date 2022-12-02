"""Model that identifies handwritten digits. """


import tensorflow as tf  # pip3 install tensorflow-macos
import numpy as np  # pip3 install numpy
import matplotlib.pyplot as plt  # pip3 install matplotlib
import cv2 as cv  # pip3 install opencv-python


#  Load data
mnist = tf.keras.datasets.mnist
#  Split the data into the train tuple and test tuple.
#  Most of the data is contained on the training example, and we
#  use a couple examples to test the model.
#  What is the percentage of data in the examples? 20%
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#  Normalize the data. What scaling down the data means?
#  Scale down the training data
x_train = tf.keras.utils.normalize(x_train, axis=1)
#  Scale down the test data
x_test = tf.keras.utils.normalize(x_test, axis=1)
#  Why we don't scale down the y data? Because this data are the labels


#  Model format: Input layer, 2 hidden layers, Output layer
#  Model type: Sequential
model = tf.keras.models.Sequential()
#  Add layers
#  Converts the 28x28 imagine into
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
# Dense layers. All neurons are connected to the previous layer and the next layer
#  The more neurons you add to the layer the more complicated the layer becomes.
#  Unit "number of neurons"
#  activation "activation function" relu = rectified linear unit activation function.
model.add(tf.keras.layers.Dense(units=100, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=100, activation=tf.nn.relu))
#  Output layer. This layers contains 10 neurons, and it uses the softmax activation function.
#  softmax = takes the output of all the previous neurons and computes the probability.
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))


#  Compile the model.
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
#  Train the model
#  Epochs = How many times the module is going to see the same data.
#  How many times we repeat the process.
model.fit(x_train, y_train, epochs=3)
loss, accuracy = model.evaluate(x_test, y_test)
model.save("digits_recognition")


print(f"The model has an accuracy of {accuracy} with a loss of {loss}")
