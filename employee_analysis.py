import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Employee_Performance_Dataset.csv")

# Display First 5 Rows
print(df.head())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Duplicates
df = df.drop_duplicates()

# Dataset Info
print("\nDataset Information:")
print(df.info())

# Basic Statistics
print("\nStatistical Summary:")
print(df.describe())

# Average Salary by Department
avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:")
print(avg_salary)

# Plot Average Salary
avg_salary.plot(kind='bar')

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# Performance Score Distribution
plt.hist(df["Performance_Score"])

plt.title("Performance Score Distribution")
plt.xlabel("Performance Score")
plt.ylabel("Count")
plt.show()

# Experience vs Salary
plt.scatter(df["Experience_Years"], df["Salary"])

plt.title("Experience vs Salary")
plt.xlabel("Experience Years")
plt.ylabel("Salary")
plt.show()