import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("dataset/Crop_recommendation.csv")

# Display the first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display the last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Display the shape of the dataset
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Display unique crop names
print("\nUnique Crop Labels:")
print(df['label'].unique())

# Count total crop categories
print("\nNumber of Crop Categories:")
print(df['label'].nunique())

# Count records of each crop
print("\nCrop Counts:")
print(df['label'].value_counts())

# -----------------------------
# Data Visualization
# -----------------------------

# Crop distribution
plt.figure(figsize=(12,6))
sns.countplot(data=df, x='label')
plt.xticks(rotation=90)
plt.title("Crop Distribution")
plt.xlabel("Crop")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.drop('label', axis=1).corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()

# Histograms
df.hist(figsize=(12,10))
plt.tight_layout()
plt.show()

# Boxplots for numerical columns
numeric_columns = ['N','P','K','temperature','humidity','ph','rainfall']

for column in numeric_columns:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.show()

# Pairplot (Optional - takes time)
# sns.pairplot(df, hue='label')
# plt.show()