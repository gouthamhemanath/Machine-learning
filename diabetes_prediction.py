# -*- coding: utf-8 -*-
"""Diabetes prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Uuf2PqmCeIk0OfHPS--yl72TKJMn0SX4
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.preprocessing import StandardScaler

diabetes=pd.read_csv('/content/diabetes.zip')
diabetes.head()

"""let us check the number of rows and columns

"""

#checking the number of rows and columns
diabetes.shape

#let we find statistical attributes in this
diabetes.describe()

#checking the diabetes and non diabetes patients
diabetes['Outcome'].value_counts()

#grouping the dataset
diabetes.groupby('Outcome').mean()

x=diabetes.drop(labels='Outcome',axis=1)
y=diabetes['Outcome']
print(x)
print(y)
#seperating the datasets"

#next the range of datas are different so we standardize the data
standardize=StandardScaler()

#now we fit and transform into certain range
fit_data=standardize.fit_transform(x)

print(fit_data)

X=fit_data
Y=diabetes['Outcome']

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=2)

print(X_train.shape,X.shape)

print(X_test.shape)

print(Y_train.shape)

print(Y_test.shape)

#let us train the model
training=svm.SVC(kernel='linear')
training.fit(X_train,Y_train)

#finding the accuracy score
predictor=training.predict(X_train)
accuracy=accuracy_score(predictor,Y_train)

print('Accuracy score of trained dta is:',accuracy
      )

predictor2=training.predict(X_test)
accuracy2=accuracy_score(predictor2,Y_test)
print(accuracy2)

# Let us predict the system
input = np.array([6, 148, 72, 35, 0, 33.6, 0.627, 50])
data_np = np.asarray(input)
data_np_reshape = data_np.reshape(1, -1)
scalar = standardize.fit_transform(data_np_reshape)
diabetes_prediction = training.predict(scalar)
if(diabetes_prediction[0]==0):
  print("The person has no diabetes")
else:
  print("The person has diabetes")

