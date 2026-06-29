import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Create folder for charts
os.makedirs("visualizations", exist_ok=True)

# Load dataset
df = pd.read_csv("sales_data.csv")

print("========== SALES DATA DASHBOARD ==========\n")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information")
print("-------------------")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nMissing Values")
print(df.isnull().sum())

print("\nSummary Statistics")
print(df.describe())

# Set Seaborn style
sns.set_theme(style="whitegrid")

# -----------------------------
# Box Plot
# -----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(x="Product", y="Price", data=df)
plt.title("Price Distribution by Product")
plt.tight_layout()
plt.savefig("visualizations/boxplot.png")
plt.show()

# -----------------------------
# Violin Plot
# -----------------------------
plt.figure(figsize=(8,5))
sns.violinplot(x="Product", y="Price", data=df)
plt.title("Price Distribution (Violin Plot)")
plt.tight_layout()
plt.savefig("visualizations/violinplot.png")
plt.show()

# -----------------------------
# Heatmap
# -----------------------------
plt.figure(figsize=(6,5))
sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True,
    cmap="Blues"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visualizations/heatmap.png")
plt.show()

# -----------------------------
# Histogram
# -----------------------------
plt.figure(figsize=(7,5))
sns.histplot(df["Quantity"], bins=10, kde=True)
plt.title("Quantity Distribution")
plt.tight_layout()
plt.savefig("visualizations/histogram.png")
plt.show()

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(7,5))
sns.scatterplot(
    x="Price",
    y="Total_Sales",
    hue="Region",
    data=df
)
plt.title("Price vs Total Sales")
plt.tight_layout()
plt.savefig("visualizations/scatterplot.png")
plt.show()

# -----------------------------
# Interactive Plotly Dashboard
# -----------------------------
fig = px.bar(
    df,
    x="Product",
    y="Total_Sales",
    color="Region",
    title="Interactive Sales Dashboard"
)

fig.show()

print("\nAll charts have been generated successfully.")
print("Charts are saved inside the 'visualizations' folder.")
