# SE-3, 20, Suraj Jagtap

#Python Experiment No. 12

"""Write a python program to read data from excel file and perform following operations:
Display the first 5 and last 5 recordsCheck types for all the columnsCalculate 
the min, max, count, sum, prod, mean, median, mode, standard deviation for the Spending Score 
columnCalculate the average Annual IncomeFind out the subsets of rows of all the 
columns whose Annual Income value is greater than meanTo calculate the Average Annual Income 
of each GenderSelect only those rows that contain female customersCreate a new data 
frame from the original sorted by the Spending Score
Note: Use Mall_Customer dataset from www.kaggle.com"""

import pandas as pd
import numpy as np

df = pd.read_csv('Mall_Customers.csv')
df.to_excel('Mall_Customers.xlsx', index=False)

print("First 5 Records:\n", df.head(), "\n")
print("Last 5 Records:\n", df.tail(), "\n")

print("Data Types of all the Columns:\n", df.dtypes, "\n")

print("Min Value of Spending Score Column:", df['Spending Score (1-100)'].min())
print("Max Value of Spending Score Column:", df['Spending Score (1-100)'].max())
print("Count of Spending Score Column:", df['Spending Score (1-100)'].count())
print("Sum of Spending Score Column:", df['Spending Score (1-100)'].sum())
print("Product of Spending Score Column:", np.prod(df['Spending Score (1-100)']))
print("Mean of Spending Score Column:", df['Spending Score (1-100)'].mean())
print("Median of Spending Score Column:", df['Spending Score (1-100)'].median())
print("Mode of Spending Score Column:", df['Spending Score (1-100)'].mode())
print("Standard Deviation of Spending Score Column:", df['Spending Score (1-100)'].std(), "\n")

print("Average Annual Income:", df['Annual Income (k$)'].mean(), "\n")

df_subset = df[df['Annual Income (k$)'] > df['Annual Income (k$)'].mean()]
print("Subsets of Rows of all Columns whose Annual Income value is greater than Mean:\n", df_subset, "\n")

df_gender = df.groupby('Gender')['Annual Income (k$)'].mean()
print("Average Annual Income of Each Gender:\n", df_gender, "\n")

df_female = df[df['Gender'] == 'Female']
print("Rows with Female Customers:\n", df_female, "\n")

df_sorted = df.sort_values(by=['Spending Score (1-100)'])
print("Data Frame Sorted by Spending Score:\n", df_sorted)
