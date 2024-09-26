import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import keras
import numpy as np
def convert_to_one_hot(y_train, num_classes=10):
    y_train_2 = np.zeros([y_train.shape[0],10])
    for c in range(num_classes):
        y_train_2[np.where(y_train==c),c] = 1
    return y_train_2



# Original
mnist = tf.keras.datasets.mnist
# New
#mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Print the size of training and test data
print(f'x_train shape {x_train.shape}')
print(f'y_train shape {y_train.shape}')
print(f'x_test shape {x_test.shape}')
print(f'y_test shape {y_test.shape}')

x_train_reshaped = x_train.reshape(x_train.shape[0], len(x_train[0])**2) #60000x784
x_test_reshaped = x_test.reshape(x_test.shape[0], len(x_test[0])**2) #10000x784

y_train_one_hot= convert_to_one_hot(y_train)
# for c in class_ids:
#     print("c --- ",one_hot_encoded[c])
#     print("one_hot_encoded[c] --- ",x_train_reshaped[y_train == c])

# Model sequential
model = Sequential()

model.add(Dense(5, input_dim=784, activation='sigmoid'))    # Hidden layer with 5 neurons and ReLU activation
model.add(Dense(10, activation='sigmoid'))   # Output layer with 10 neurons for 10 classes

opt = keras.optimizers.SGD(learning_rate=0.1)
model.compile(optimizer=opt, loss='mse', metrics=['mse'])

history = model.fit(x_train_reshaped, y_train_one_hot, epochs=30, verbose=0)
