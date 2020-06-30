import numpy as np
import uproot
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.layers import Input, Flatten, Dense, Dropout
from keras.models import Model

# Load and prepare the MNIST dataset and convert the samples
# from integers to floating-point numbers
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the keras model using the functional API
inputs = Input(shape=x_train.shape[1:])
x = Flatten()(inputs)
x = Dense(512, activation=tf.nn.relu)(x)
x = Dropout(0.2)(x)
predictions = Dense(10, activation=tf.nn.softmax)(x)

model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train and evaluate the model loss and accuracy
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
# Save the full model architecture, weights, and optimizer state
model.save('tf_example_model.h5')
