# Heart Disease Analysis Project

This project analyzes a dataset on heart disease, providing visualizations and statistical insights to better understand the factors related to heart disease presence. The code cleans the data, performs exploratory data analysis, and generates visualizations that highlight important patterns.

## Requirements

To run this code, the following libraries are required:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```

## Data Source

The dataset is automatically downloaded from Kaggle and consists of patient information, including age, sex, cholesterol levels, blood pressure, and heart disease diagnosis.

## Code Overview

1. **Data Import and Basic Information**  
   The code first imports necessary libraries and reads the heart disease dataset into a DataFrame. It then displays the first few rows, dataset structure, and basic statistical summaries.

2. **Data Cleaning and Preparation**  
   The `clean_data` function:
   - Checks for missing values.
   - Converts certain numeric columns (like `sex` and `target`) to categorical variables for easier interpretation in visualizations.

3. **Data Visualization**

   - **Age Distribution**: Plots a histogram showing age distribution by heart disease status, giving insight into age patterns associated with heart disease.
   - **Cholesterol vs Blood Pressure**: Creates a scatter plot to analyze the relationship between cholesterol levels and resting blood pressure, segmented by disease status and gender.
   - **Correlation Heatmap**: Displays a heatmap of correlations among numerical variables, revealing variables most associated with heart disease.

4. **Additional Statistics**  
   The code computes the correlation of each variable with the `target` (heart disease presence) to identify the most influential factors.

5. **Saving and Downloading Plots**  
   The visualizations are saved as `.png` files and can be downloaded locally for reporting or further analysis.

## Running the Code

To run this code in a Jupyter Notebook or Google Colab environment, follow these steps:

1. Install dependencies with the command provided in the "Requirements" section.
2. Execute each code cell sequentially.
3. The images for the generated plots (`age_distribution.png`, `cholesterol_bp_scatter.png`, and `correlation_heatmap.png`) will be available for download.

## Visualizations and Findings

- **Age Distribution**: Shows the distribution of ages for those with and without heart disease.
- **Cholesterol vs Blood Pressure**: Highlights patterns between cholesterol and blood pressure in relation to gender and heart disease status.
- **Correlation Heatmap**: Helps identify which factors are more strongly associated with heart disease presence.
