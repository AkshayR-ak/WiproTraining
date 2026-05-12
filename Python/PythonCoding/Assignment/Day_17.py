# Assignment 4: Distribution Analysis (Seaborn)
print("Assignment 4: Distribution Analysis (Seaborn)")
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
tips = sns.load_dataset('tips')

# 1. Histogram with KDE
sns.displot(
    data=tips,
    x='total_bill',
    kde=True,
    color='darkblue'
)
plt.title("Distribution of Total Bill")
plt.show()

# 2. JointPlot with regression line
sns.jointplot(
    data=tips,
    x='total_bill',
    y='tip',
    kind='reg',
    color='purple'
)
plt.show()

# 3. BoxPlot comparing total_bill across days with smoker hue
plt.figure(figsize=(10, 6))
sns.boxplot(
    data=tips,
    x='day',
    y='total_bill',
    hue='smoker'
)
plt.title("Total Bill by Day and Smoker Status")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

print("Assignment 5: Multi-Visual Comparison (Matplotlib)")
# Assignment 5: Multi-Visual Comparison (Matplotlib)

import matplotlib.pyplot as plt

# Dataset
cities = ['Chennai', 'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad']
sales_values = [450, 600, 520, 780, 410]
categories = ['Electronics', 'Fashion', 'Groceries', 'Home Decor']
market_share = [35, 25, 30, 10]

# Create figure with subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1 - Bar Chart
axes[0].bar(cities, sales_values, color='teal')
axes[0].set_title("City Sales Comparison")
axes[0].set_xlabel("Cities")
axes[0].set_ylabel("Sales Values")
axes[0].grid(axis='y')

# Subplot 2 - Pie Chart
explode = [0.1, 0, 0, 0]
axes[1].pie(
    market_share,
    labels=categories,
    autopct='%1.1f%%',
    explode=explode
)
axes[1].set_title("Market Share by Category")

# Main Title
fig.suptitle("Regional Sales & Category Analysis", fontsize=16)
plt.tight_layout()
plt.show()