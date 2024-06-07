# Industrial_Copper_Modelling
Building a Regression model to predict the selling price of copper and building a Classification model to predict the status of a potential lead. End User can provide necessary details on a Streamlit app and get the predictions | Python | ML | EDA | Sklearn | Seaborn | Matplotlib | Streamlit |

**Introduction**

A copper Industry's data is provided using which a regression model is to be built to predict the selling price of copper and classification model to predict the status of a potential lead customer. A simple Streamlit app is built where user can provide the required details to get the predictions.

![UI](https://github.com/Abinaya-Ganesh/Industrial_Copper_Modelling/assets/162968618/651cd4a0-8a0a-4cf2-a89a-c9407e91b5c7)

**User Guide**

The Streamlit app contains two tabs. One for Price prediction and other for Status prediction. Input all the necessary details and get the predictions. 

**Developer Guide**

**1.Tools required**

  • Python

  • Visual Studio Code

**2.Python libraries to install**
  **a.For dashboard creation**

    • Streamlit

  **b.For Analysis**

    • matplotlib.pyplot

    • Seaborn

    • scipy.stats

    • Numpy

    • Pandas

  **c.For Machine Learning models**

    • Scikit-learn

    • Imblearn

**3. Modules to import**

  a. File handling Libraries

    • import pickle

  b. Pandas Library

    • import pandas

  c. Numerical calculatoins Library

    • import numpy as np

    • from scipy.stats import skew

  d. Visualization Libraries

    • import matplotlib.pyplot as plt

    • import seaborn as sns

  e. Dashboard Libraries

    • import streamlit as st

  f. Machine Learning Libraries

    • from sklearn.preprocessing import LabelEncoder

    • from sklearn.preprocessing import OrdinalEncoder
    
    • from sklearn.model_selection import train_test_split

    • from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier

    • from sklearn.linear_model import LogisticRegression

    • from sklearn.preprocessing import StandardScaler

    • from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score

    • from sklearn.model_selection import GridSearchCV

    • from imblearn.combine import SMOTEENN

  g. Others

    • from collections import Counter

**4.Process**

    • Data is extracted from a csv file and stored as a pandas Dataframe

    • Data cleaning is done and null values are dropped which accounts to less than 1% of data

    • Skewness of continuous variables are calculated and logarthmic transformation is applied as the data is heavily skewed

    • Skewness, distribution and outliers of the continuous variables are visualized and certain negative values present are also dropped

    • Multi variate analysis is performed and heatmap is visualized for the continuous variables

    • Regression model is built using Decision tree which gives an r2 value of 0.93

    • Data which has the status values other than 'Won' and 'Lost' are dropped

    • Classification data is assessed for class imbalance

    • The heavily imbalanced data is resampled and balanced using SMOTE ENN

    • Two Classification models are built using Logistic Regression and Decision tree which are compared using their evaluation metrics

    • The decision tree classifier model which gives 97% accuracy is chosen

    • The selected models are pickled which can be used in the Streamlit app file

    • A simple Streamlit UI is built where user enters the required values and the predictions are printed

    
**NOTE:**

  • The EDA.ipynb file contains the code for data extraction, pre processing, EDA and Machine learning models
    
  • The Copper_dasboard.py file consists of the code for Streamlit dashboard creation

  • Data is provided in the project problem statement pdf as a excel file which is converted to csv for quick data extraction

  • The pickled models are also uploaded which can be used in the Streamlit file
  
