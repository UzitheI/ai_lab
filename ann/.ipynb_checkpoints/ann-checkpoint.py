import cv
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt 

# Load CIFAR-10 dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Check the shape of the data
print(X_train.shape)  # Should be (50000, 32, 32, 3)
print(y_train.shape)  # Should be (50000, 1)
print(X_test.shape)   # Should be (10000, 32, 32, 3)
print(y_test.shape)   # Should be (10000, 1)

