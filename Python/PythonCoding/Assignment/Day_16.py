# Assignment 1: NumPy Array Surgery
print("Assignment 1: NumPy Array Surgery")
import numpy as np

np.random.seed(42)
data_array = np.random.randint(1, 501, size=(10, 10))
print("Original Array:\n", data_array)

# 1. Find global mean and replace values greater than mean with 0
global_mean = np.mean(data_array)
modified_array = np.where(data_array > global_mean, 0, data_array)
print("\nGlobal Mean:", global_mean)
print("\nModified Array:\n", modified_array)

# 2. Column sum and row standard deviation
column_sum = np.sum(modified_array, axis=0)
row_std = np.std(modified_array, axis=1)
print("\nColumn Sum:\n", column_sum)
print("\nRow Standard Deviation:\n", row_std)

# 3. Extract center 4x4 sub-matrix and flatten
sub_matrix = modified_array[3:7, 3:7]
flat_array = sub_matrix.flatten()
print("\n4x4 Sub-Matrix:\n", sub_matrix)
print("\nFlattened Array:\n", flat_array)

# Assignment 2: Pandas Data Cleaning & Transformation
print("Assignment 2: Pandas Data Cleaning & Transformation")

import pandas as pd
raw_data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Laptop', 'Mouse', None],
    'Revenue': [1200, 25, 300, 75, 1150, None, 150],
    'Cost': [800, 10, 200, 40, 850, 15, 100],
    'Date': ['2025-01-10', '2025-02-15', '2025-03-20',
             '2025-10-05', '2025-11-12', '2025-12-25', '2025-06-01']
}
df = pd.DataFrame(raw_data)
print("Original DataFrame:\n", df)

# 1. Handle missing values
median_revenue = df['Revenue'].median()
df['Revenue'] = df['Revenue'].fillna(median_revenue)
df['Product'] = df['Product'].fillna("Unknown")
print("\nAfter Handling Missing Values:\n", df)

# 2. Feature Engineering
df['Profit'] = df['Revenue'] - df['Cost']
df['Margin_Percentage'] = (df['Profit'] / df['Revenue']) * 100
print("\nDataFrame with New Columns:\n", df)

# 3. Convert Date column and filter Q4 products with Profit > 50
df['Date'] = pd.to_datetime(df['Date'])
q4_filtered = df[
    (df['Date'].dt.quarter == 4) &
    (df['Profit'] > 50)
]
print("\nQ4 Products with Profit > 50:\n", q4_filtered)

# Assignment 3: Grouping & Pivot Tables
print("Assignment 3: Grouping & Pivot Tables")

import pandas as pd
employee_data = {
    'Dept': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'Sales'],
    'Status': ['FT', 'FT', 'Contract', 'FT', 'Contract', 'FT', 'Contract', 'FT'],
    'Salary': [95000, 60000, 70000, 80000, 55000, 98000, 72000, 85000]
}
emp_df = pd.DataFrame(employee_data)
print("Employee DataFrame:\n", emp_df)

# 1. Group by Dept
grouped_data = emp_df.groupby('Dept')['Salary'].agg(['mean', 'max'])
print("\nAverage and Maximum Salary by Department:\n", grouped_data)

# 2. Pivot Table
pivot_table = pd.pivot_table(
    emp_df,
    index='Dept',
    columns='Status',
    values='Salary',
    aggfunc='count',
    fill_value=0
)
print("\nPivot Table:\n", pivot_table)

# 3. Sort by Contract workers
sorted_pivot = pivot_table.sort_values(by='Contract', ascending=False)
print("\nDepartments Sorted by Contract Workers:\n", sorted_pivot)