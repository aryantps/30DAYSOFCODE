import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

########################################### -IMPORTING DATA- #################################################

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

def show_image(index):
    f = plt.figure(figsize=(15, 10))
    plt.imshow(train_images[index],f)
    plt.show()

#show_image(5)

########################################### -PREPROCESS DATASET- #################################################

train_images = train_images / 255.0
test_images = test_images / 255.0

# 3 layers(fully connected network)
# -1st layer – Input Layer – intake an image(Flatten layer that intakes a multi-dimensional array and produces an array of a single dimension)
# -2nd layer - ReLu  => f(x)=max(0,x)
# -3rd layer - Softmax => values in 0-1 range with total sum 1

########################################### -MODEL GENERATION- #################################################

model = keras.Sequential([keras.layers.Flatten(input_shape = (28,28)), 
                            keras.layers.Dense(128, activation=tf.nn.relu), 
                            keras.layers.Dense(128, activation=tf.nn.relu),
                            keras.layers.Dense(10, activation = tf.nn.softmax)])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

########################################### -TRAINING MODEL- #################################################

model.fit(train_images,train_labels,epochs=100)

########################################### -EVALUATE MODEL- #################################################

test_loss, test_accuracy = model.evaluate(test_images,test_labels)
predictions = model.predict(test_images)

print(f'Test accuracy is {test_accuracy * 100} %')

def predictor(index):
    """
    function to predict specific Pokémon.
    input- index of test_data:
    """
    if np.argmax(predictions[index]) == test_labels[index]:
        print(f'This was correctly predicted to be a \"{test_labels[index]}\"!')
    else:
        print(f'This was incorrectly predicted to be a \"{np.argmax(predictions[index])}\". It was actually a \"{test_labels[index]}\".')
        return(predictions)

predictor(100)


