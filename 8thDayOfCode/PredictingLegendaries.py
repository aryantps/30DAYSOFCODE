import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing


##########################     ----     FORMATTING DATA    ----          ########################## 
df = pd.read_csv('pokemon_alopez247.csv')
                                                                        # df.columns = Index(['Number', 'Name', 'Type_1', 'Type_2', 'Total', 'HP', 'Attack',
                                                                        #        'Defense', 'Sp_Atk', 'Sp_Def', 'Speed', 'Generation', 'isLegendary',
                                                                        #        'Color', 'hasGender', 'Pr_Male', 'Egg_Group_1', 'Egg_Group_2',
                                                                        #        'hasMegaEvolution', 'Height_m', 'Weight_kg', 'Catch_Rate',
                                                                        #        'Body_Style'],
                                                                        #       dtype='object')
df = df[['isLegendary','Generation', 'Type_1', 'Type_2', 'HP', 'Attack', 'Defense',
         'Sp_Atk', 'Sp_Def', 'Speed','Color','Egg_Group_1','Height_m','Weight_kg','Body_Style']]       




df['isLegendary'] = df['isLegendary'].astype(int)

def coreleation_visualization(categories):
    ndf = df[categories]
    f = plt.figure(figsize=(15, 10))
    plt.matshow(ndf.corr(), fignum=f.number)
    plt.xticks(range(ndf.shape[1]), ndf.columns, fontsize=14, rotation=45)
    plt.yticks(range(ndf.shape[1]), ndf.columns, fontsize=14)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    plt.title('Correlation Matrix\n\n\n', fontsize=20,loc='left');
    plt.savefig('correlation.png')
    #return plt.show()

coreleation_visualization(['isLegendary','Generation', 'HP', 'Attack', 'Defense',
         'Sp_Atk', 'Sp_Def', 'Speed','Height_m','Weight_kg'])

def dummy_creation(df,categories):
    """
    create a dummy DataFrame of category. And concatenate it  original DataFrame. 
    drop the original column
    """
    for i in categories:
        df_dummy = pd.get_dummies(df[i])
        df = pd.concat([df,df_dummy],axis = 1)
        df = df.drop(i,axis=1)
    return df

df = dummy_creation(df, ['Egg_Group_1', 'Body_Style', 'Color','Type_1', 'Type_2'])


##########################         ----   SPILITTING DATA   ----                 ########################## 


#splitting the data by Pokémon generation.
#1st generation of Pokémon (from Pokémon Red, Blue, and Yellow) will be testing data The rest will be our training data
def train_test_splitter(DataFrame, column):
    """takes any Pokémon whose "Generation" label is equal to 1 and putting it into the test dataset, 
    and putting everyone else in the training dataset. 
    It then drops the Generation category from the dataset."""
    df_train = DataFrame.loc[df[column] != 1]
    df_test = DataFrame.loc[df[column] == 1]

    df_train = df_train.drop(column, axis=1)
    df_test = df_test.drop(column, axis=1)

    return(df_train, df_test)

df_train, df_test = train_test_splitter(df, 'Generation')


#separate the labels (the 'islegendary' category) from the rest of the data
def label_delineator(df_train, df_test, label):
    
    """extracts the data from the DataFrame and puts it into arrays that TensorFlow can understand with.values"""


    train_data = df_train.drop(label, axis=1).values
    train_labels = df_train[label].values
    test_data = df_test.drop(label,axis=1).values
    test_labels = df_test[label].values
    return(train_data, train_labels, test_data, test_labels)

train_data, train_labels, test_data, test_labels = label_delineator(df_train, df_test, 'isLegendary')


##########################         ----   NORMALIZING DATA  ----                 ########################## 


def data_normalizer(train_data, test_data):
    """
    Transform features by scaling each feature to a given range. 
    This estimator scales and translates each feature individually such that it is in the given range on the training set
    """
    train_data = preprocessing.MinMaxScaler().fit_transform(train_data)
    test_data = preprocessing.MinMaxScaler().fit_transform(test_data)
    return(train_data, test_data)

train_data, test_data = data_normalizer(train_data, test_data)


#******************************************************************************************************************
##########################                 BUILDING NEURAL NETWORK                       ########################## 
#******************************************************************************************************************

#two fully connected neural layers -  first layer use ReLU
#                                     final layer is softmax layer
costs =[]
length = train_data.shape[1]

model = keras.Sequential()
model.add(keras.layers.Dense(500, activation='relu', input_shape=[length,]))
model.add(keras.layers.Dense(2, activation='softmax'))

#compile the model
#optimizer  -  Stochastic Gradient Descent
model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#model fit on training data
model.fit(train_data, train_labels, epochs=100)

loss_value, accuracy_value = model.evaluate(test_data, test_labels)
print(f'Our test accuracy was {accuracy_value})')



##########################         ----   EVALUATE DATA  ----                 ########################## 


def predictor(test_data, test_labels, index):
    """
    function to predict specific Pokémon.
    input- index of test_data:
    """
    prediction = model.predict(test_data)
    if np.argmax(prediction[index]) == test_labels[index]:
        print(f'This was correctly predicted to be a \"{test_labels[index]}\"!')
    else:
        print(f'This was incorrectly predicted to be a \"{np.argmax(prediction[index])}\". It was actually a \"{test_labels[index]}\".')
        return(prediction)


predictor(test_data, test_labels, 100)
