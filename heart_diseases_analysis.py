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

# Plot 1: Age Distribution (Histogram)
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='age', hue='target', multiple="layer", bins=30)
plt.title('Age Distribution by Heart Disease Status')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('age_distribution.png')
plt.show()

# Plot 2: Cholesterol vs Blood Pressure (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='chol', y='trestbps', hue='target',
                style='sex', s=100)
plt.title('Cholesterol vs Blood Pressure by Disease Status and Gender')
plt.xlabel('Cholesterol (mg/dl)')
plt.ylabel('Resting Blood Pressure (mm Hg)')
plt.savefig('cholesterol_bp_scatter.png')
plt.show()

# Plot 3: Correlation Heatmap
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numerical_cols].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap of Numerical Variables')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.show()

# Save plots for report
from google.colab import files
files.download('age_distribution.png')
files.download('cholesterol_bp_scatter.png')
files.download('correlation_heatmap.png')
