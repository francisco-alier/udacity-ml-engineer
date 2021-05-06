# ML Engineer Capstone Project Repository

## Deploying a webapp to predict positiveness of songs

Project for Udacity ML Engineer Nanodegree program. [Machine Learning Engineer Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t).

This project has the main goal of scrapping music lyrics data, train a Neural Network model, more specifically a [Long-Short Term Memory Neural Network](https://en.wikipedia.org/wiki/Long_short-term_memory). The model is set into production using the [AWS](https://aws.amazon.com/) services.

The repository contains the following main items:

## [1. Notebooks](https://github.com/francisco-alier/udacity-ml-engineer/tree/master/04_Capstone_Project/notebooks)
* [Data Extraction Notebook](https://github.com/francisco-alier/udacity-ml-engineer/blob/master/04_Capstone_Project/notebooks/01_Data_Extraction.ipynb)
* [Data Exploration Notebook](https://github.com/francisco-alier/udacity-ml-engineer/blob/master/04_Capstone_Project/notebooks/02_Data_Exploration_and_Feature_Engineering.ipynb)
* [Model Training and Deployment](https://github.com/francisco-alier/udacity-ml-engineer/blob/master/04_Capstone_Project/notebooks/03_Model_Training_SageMaker.ipynb)


## [2. Deliverables](https://github.com/francisco-alier/udacity-ml-engineer/tree/master/04_Capstone_Project/deliverables)

## [3. Capstone Web App](https://github.com/suryasanchez/machine-learning-engineer-nanodegree/tree/master/P3-capstone-project/index.html)

### Environment

* AWS Sagemaker
* kernel: conda_python3

### Summary of the Capstone Notebook

1. Definition

	* 1.1 Project Overview

	* 1.2. Problem Statement

	* 1.3 Metrics

2. Analysis

	* 2.1 Gathering data
		* CRM connection settings
		* Check the format of the data from the API and explore the content
		* Create the dataset

	* 2.2 Data pre-processing
		* Cleaning the data
		* Export to CSV for labeling
		* Import the labeled CSV
		* Reduce the number of class
		* Detect the language of the text
		* Keep only french text
		* Tokenization
		* Bag-of-Words features
		* Save the processed training dataset locally

	* 2.3 Training and testing the model
		* Uploading the training data
		* XGBoost model
		* Testing the model

	* 2.4 Tuning the Hyperparameters
		* Hyperparameter Tuner

	* 2.5 Binary classification
		* Two categories
		* Training of the model
		* Testing the model
		* Tuning the Hyperparameters

	* 2.6 Deploy the model

	* 2.7 Web application
		* Input testing
		* AWS Lambda
		* HTML web app


3. Conclusion

	* 3.1 Reflection

	* 3.2 Improvement

	* 3.3 Application

4. References