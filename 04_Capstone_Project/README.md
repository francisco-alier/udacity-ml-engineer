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

## [3. Capstone Web App](https://github.com/francisco-alier/udacity-ml-engineer/blob/master/04_Capstone_Project/webapp/index.html)

### Requirements and Environment

#### Environemnt
* AWS Sagemaker
* kernel: conda_pytorch_p36
* Access to AWS services such as Lambda and API Gateway

#### Requirements
* Standard Python Libraries included in the conda package
* `Sagemaker` version `1.72.0`
* `Wordcloud`
* `PyTorch`

### Final Webapp

The user will input the lyrics of a song of his/her choice and the app will output a sentence indicating if the song is positive or negative:
<p align="center">
  <img src="./images/webapp_output_positive.png" width="50%">
</p>
<p align="center">
  <img src="./images/webapp_output_negative.png" width="50%">
</p>