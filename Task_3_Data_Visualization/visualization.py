import pandas as pd
import matplotlib.pyplot as plt

# Load the Superstore dataset
df = pd.read_csv("superstore.csv")

print(df.head())
print(df.info())
print(df.describe())

# Sales by category
sales = df.groupby("Category")["Sales"].sum()

sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()
# Profit by Category
profit = df.groupby("Category")["Profit"].sum()

profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()
# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()
# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()
# Sales by Segment
segment_sales = df.groupby("Segment")["Sales"].sum()

segment_sales.plot(kind="bar")
plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_segment.png")
plt.show()


# Combined Sales and Profit Dashboard
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Sales by Category
df.groupby("Category")["Sales"].sum().plot(
    kind="bar", ax=axes[0, 0], title="Sales by Category"
)
axes[0, 0].set_ylabel("Total Sales")
axes[0, 0].tick_params(axis="x", rotation=0)

# Profit by Category
df.groupby("Category")["Profit"].sum().plot(
    kind="bar", ax=axes[0, 1], title="Profit by Category"
)
axes[0, 1].set_ylabel("Total Profit")
axes[0, 1].tick_params(axis="x", rotation=0)

# Sales by Region
df.groupby("Region")["Sales"].sum().plot(
    kind="bar", ax=axes[1, 0], title="Sales by Region"
)
axes[1, 0].set_ylabel("Total Sales")
axes[1, 0].tick_params(axis="x", rotation=0)

# Sales by Customer Segment
df.groupby("Segment")["Sales"].sum().plot(
    kind="bar", ax=axes[1, 1], title="Sales by Customer Segment"
)
axes[1, 1].set_ylabel("Total Sales")
axes[1, 1].tick_params(axis="x", rotation=0)

fig.suptitle("Superstore Sales and Profit Dashboard", fontsize=16)
plt.tight_layout()
plt.savefig("superstore_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()

# Actual Business Insights
print("\n--- BUSINESS INSIGHTS ---")

print("\nTotal Sales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False).round(2))

print("\nTotal Profit by Category:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False).round(2))

print("\nTotal Sales by Region:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False).round(2))

print("\nTotal Sales by Customer Segment:")
print(df.groupby("Segment")["Sales"].sum().sort_values(ascending=False).round(2))
print("TEST: BUSINESS INSIGHTS CODE REACHED")

