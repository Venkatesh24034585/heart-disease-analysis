# Import required libraries
!pip install pandas numpy seaborn matplotlib scikit-learn

# Import the libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('heart.csv')

# Display first few rows and basic information
print("First few rows of the dataset:")
display(df.head())

print("\nDataset Info:")
display(df.info())

print("\nBasic Statistics:")
display(df.describe())

# Data Cleaning and Preparation
def clean_data(df):
    # Check for missing values
    print("\nMissing Values:")
    display(df.isnull().sum())

    # Convert categorical variables
    df['sex'] = df['sex'].map({1: 'MALE', 0: 'FEMALE'})
    df['target'] = df['target'].map({1: 'Disease', 0: 'No Disease'})

    return df

df = clean_data(df)
