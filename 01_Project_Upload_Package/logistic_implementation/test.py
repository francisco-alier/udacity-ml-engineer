# import packages
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from LogisticRegression import MyLogisticRegression

# Importing dataset     
df = pd.read_csv( "dummy_data/heart.csv" ) 

# selecting features and target
X = df.iloc[:,:-1].values 
y = df.iloc[:,-1:].values 
  
# Splitting dataset into train and test set 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123 ) 
print(X_train.shape, y_train.shape)  
print(X_test.shape, y_test.shape)  
# Model training     
model = MyLogisticRegression(alpha = 0.5, iterations = 2000) 

#fit model
model.fit(X_train, y_train)

#predict on test data
y_pred = model.predict(X_test, predict_proba = True)

#get AUC
auc_test = roc_auc_score(y_test, y_pred)

print(f" The AUC on test is {auc_test}")
