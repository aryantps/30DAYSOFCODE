import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import random

	
mappings = {0:	'T-shirt/top',
            1:	'Trouser',
            2:	'Pullover',
            3:	'Dress',
            4:	'Coat',
            5:	'Sandal',
            6:	'Shirt',
            7:	'Sneaker',
            8:	'Bag',
            9:	'Ankle boot'}
########################################### -IMPORTING DATA- #################################################
def load_dataset():
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    return train_images, train_labels, test_images, test_labels

def show_image():
    train_images, train_labels, test_images, test_labels = load_dataset()
    fig = plt.figure()
    for i in range(10):
        ax = fig.add_subplot(2, 5, i+1)
        ax.imshow(train_images[i])
    
    plt.show()
    #plt.savefig('first9.png')

#show_image()

########################################### -PREPROCESS DATASET- #################################################
def preprocessing(train_images,test_images):
    train_images = train_images.astype('float32')
    test_images = test_images.astype('float32')

    train_images = train_images / 255.0
    test_images = test_images / 255.0
    return train_images,test_images

# 3 layers(fully connected network)
# -1st layer – Input Layer – intake an image(Flatten layer that intakes a multi-dimensional array and produces an array of a single dimension)
# -2nd layer - ReLu  => f(x)=max(0,x)
# -3rd layer - Softmax => values in 0-1 range with total sum 1

########################################### -MODEL GENERATION- #################################################

def build_model():
    model = keras.models.Sequential()
    model.add(keras.layers.Flatten(input_shape = (28,28)))
    model.add(keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(keras.layers.Dense(10, activation = tf.nn.softmax))
    model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    return model

######################################## -TRAINING & EVALUATE MODEL- ##########################################
def model_training():
    train_images, train_labels, test_images, test_labels = load_dataset()
    train_images,test_images = preprocessing(train_images,test_images)
    model = build_model()
    model.fit(train_images,train_labels,epochs=100,verbose=1)
    model.save('final_FMNIST_model.h5')
    test_loss, test_accuracy = model.evaluate(test_images,test_labels)
    print(f'\n\nTest accuracy is {test_accuracy * 100} %\n')

    


########################################### -TESTING- #################################################



def predictor(index):
    """
    function to predict specific Pokémon.
    input- index of test_data:

    """
    _,_,test_images,test_labels = load_dataset()
    model = keras.models.load_model('final_FMNIST_model.h5')
    predictions = model.predict(test_images)

    if np.argmax(predictions[index]) == test_labels[index]:
        category =test_labels[index]
        print(f'This was correctly predicted to be a \"{mappings[category]}\"!\n')
    else:
        predicted_category = np.argmax(predictions[index]) 
        actual_category = test_labels[index]
        print(f'This was incorrectly predicted to be a \"{mappings[predicted_category]}\". It was actually a \"{mappings[actual_category]}\".\n')
        return(predictions)


if __name__ == '__main__':
    model_training()

    sampleTestIndex = random.sample(range(10000),10)
    for i in sampleTestIndex:
        predictor(i)

