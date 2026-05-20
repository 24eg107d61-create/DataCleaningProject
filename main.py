import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

# Show first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDuplicates Removed!")

# Gender Distribution Graph
plt.figure(figsize=(6,4))
sns.countplot(x='gender', data=df)
plt.title("Gender Distribution")
plt.savefig("gender_distribution.png")
plt.close()

# Math Score Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['math score'], bins=10)
plt.title("Math Score Distribution")
plt.savefig("math_score_distribution.png")
plt.close()

# Heatmap
plt.figure(figsize=(8,5))
sns.heatmap(df.select_dtypes(include=['int64']).corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()

print("\nProject Completed Successfully!")