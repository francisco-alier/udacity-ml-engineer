import numpy as np
import pandas as pd


class MyLogisticRegression():
    
    def __init__( self, alpha, iterations):
        self.alpha = alpha
        self.iteractions = iterations
    

    def fit(self , X, y):
        '''
        Function used for model training
        '''
        self.m, self.n = X.shape
        
        self.X = X
        self.y = y
        self.W = np.zeros(self.n)
        self.bias = 0
        
        # gradient descent
        for i in range(self.iteractions):
            self.update_weights()
    
    
    def calculate_sigmoid(self):
        '''
        Helper function to output result from a sigmoid function
        ------------------------

        '''
        
        sigmoid = 1 / (1 + np.exp(-(self.X.dot(self.W) + self.bias)))
        
        return sigmoid
    
    
    def update_weights( self ):
        '''
        helper function to update weights while performing gradient descent
        '''
        A = self.calculate_sigmoid()
        intr = np.reshape((A - self.y.T), self.m)
        
        dW = np.dot(self.X.T, intr) / self.m
        db = np.sum( intr ) / self.m
        
        #update weights
        self.W = self.W - self.alpha * dW
        self.bias = self.bias - self.alpha * db
        
        return self
        
        
    def predict(self, X, predict_proba = False):
        '''
        Function to predict logistic regression probabilities, or values, based on a treshold
        of 0.5. Needs to work on the test set so we calculate the sigmoid here again
        '''
        Z = 1 / (1 + np.exp(-(X.dot(self.W) + self.bias)))
        
        if predict_proba:
            y = Z
            
        else:
            y = np.where(Z > 0.5, 1, 0)
            
        return y
    