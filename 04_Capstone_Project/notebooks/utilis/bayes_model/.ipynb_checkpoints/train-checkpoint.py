from __future__ import print_function

import argparse
import os
import pandas as pd
import numpy as np

# Import joblib package directly
import sklearn.externals
import joblib

from sklearn.naive_bayes import GaussianNB

# Load function
def model_fn(model_dir):
    """Load model from the model_dir. This is the same model that is saved
    in the main if statement.
    """
    print("Loading model.")
    
    # load using joblib
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    print("Done loading model.")
    
    return model

# custom predict function
def predict_fn(input_data, model):
    """
    custom predict function to get probabilties from Bayes model
    """
    #prediction = model.predict(input_data)
    pred_prob = model.predict_proba(input_data)
    
    return np.array(pred_prob)


# Main Code
if __name__ == '__main__':
    
    # Here we set up an argument parser to easily access the parameters
    parser = argparse.ArgumentParser()

    # SageMaker parameters, like the directories for training data and saving models; set automatically
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--data-dir', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
        
    # args holds all passed-in arguments
    args = parser.parse_args()

    # Read in csv training file
    training_dir = args.data_dir
    train_data = pd.read_csv(os.path.join(training_dir, "train.csv"), header=None, names=None)

    # Labels are in the first column
    train_y = train_data.iloc[:,0]
    train_x = train_data.iloc[:,1:]    

    # Define base model - Gaussian NB
    model = GaussianNB()
    
    model.fit(train_x, train_y)    

    # Save the trained model
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))
    

