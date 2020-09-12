from matplotlib import pyplot as plt
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np


import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)



def image_visualizer(index):
    first_image = mnist.test.images[index]
    first_image = np.array(first_image, dtype='float')
    pixels = first_image.reshape((28, 28))
    plt.imshow(pixels)
    return plt.show()

for i in range(3):
    image_visualizer(i)



print(f'Number of training set examples are {mnist.train.num_examples}.')
print(f'Number of test set examples are {mnist.test.num_examples}.')
print(f'Number of validation set examples are {mnist.validation.num_examples}.')

# Load data
X_train = mnist.train.images
Y_train = mnist.train.labels
X_test = mnist.test.images
Y_test = mnist.test.labels


                    
total_features = 784         #pixels = 28 * 28


#parameters
num_Nodes_hiddLayer_1 = 500
num_Nodes_hiddLayer_2 = 500
num_Nodes_hiddLayer_3 = 500

classes = 10  #no of classes

batch_size = 100

X = tf.placeholder('float',[None,784]) # 784 is 28*28 ,i.e., the size of mnist images
Y = tf.placeholder('float')


def forward_propagation(x):
    hidden_layer_1 = {'weights' : tf.Variable(tf.random_normal([784, num_Nodes_hiddLayer_1])),
                      'biases' : tf.Variable(tf.random_normal([num_Nodes_hiddLayer_1]))}
    hidden_layer_2 = {'weights' : tf.Variable(tf.random_normal([num_Nodes_hiddLayer_1,num_Nodes_hiddLayer_2])),
                      'biases':tf.Variable(tf.random_normal([num_Nodes_hiddLayer_2]))}
    hidden_layer_3 = {'weights' : tf.Variable(tf.random_normal([num_Nodes_hiddLayer_2,num_Nodes_hiddLayer_3])),
                      'biases':tf.Variable(tf.random_normal([num_Nodes_hiddLayer_3]))}
    output_layer = {'weights' : tf.Variable(tf.random_normal([num_Nodes_hiddLayer_3,classes])),
                    'biases':tf.Variable(tf.random_normal([classes]))}


    Z1 = tf.add(tf.matmul(x,hidden_layer_1['weights']) , hidden_layer_1['biases'])
    A1 = tf.nn.relu(Z1)	# activation func

    Z2 = tf.add(tf.matmul(A1,hidden_layer_2['weights']) , hidden_layer_2['biases'])
    A2 = tf.nn.relu(Z2)	# activation func

    Z3 = tf.add(tf.matmul(A2,hidden_layer_3['weights']) , hidden_layer_3['biases'])
    A3 = tf.nn.relu(Z3)	# activation func
    
    #Z4
    output = tf.matmul(A3,output_layer['weights']) + output_layer['biases']
    
    return output


def train_neural_network(X):
    
    costs = [] #FOR GRAPH
    
    prediction = forward_propagation(X)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction,labels=Y))
    
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    hm_epochs = 50 # cycles of feed forward + back

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer()) 

        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples/batch_size)):
                epoch_x,epoch_y = mnist.train.next_batch(batch_size) 
                _,c = sess.run([optimizer, cost], feed_dict = {X: epoch_x, Y: epoch_y})
                epoch_loss += c
            #print('Epoch',epoch,'completed out of',hm_epochs,' loss:',epoch_loss)
            
            if epoch % 5 == 0:
                print (f"Cost after epoch {epoch} / {hm_epochs}: {epoch_loss} ")
            if epoch % 5 == 0:
                costs.append(epoch_loss)

            
        plt.plot(np.squeeze(costs))
        plt.ylabel('cost')
        plt.xlabel('iterations (per fives)')
        plt.title("Learning rate =" + str(learning_rate))
        plt.show()

        correct = tf.equal(tf.argmax(prediction,1),tf.argmax(Y,1))
        accuracy = tf.reduce_mean(tf.cast(correct,'float'))
        # cast changes the datatype in tensorflow, in this case it will be changed to float type.
        print ("Train Accuracy:", accuracy.eval({X : mnist.train.images, Y : mnist.train.labels}))
        print ("Test Accuracy:", accuracy.eval({X : mnist.test.images, Y : mnist.test.labels}))


train_neural_network(X)