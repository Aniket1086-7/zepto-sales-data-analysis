
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns # For better aesthetics
df_sales = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Zepto Project\zepto_sales (1).csv")
df_products = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Zepto Project\zepto_products (1).csv")

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# # Plot 1: Top 5 Products by Sales Amount
top_products = df_sales.groupby("product_id")["total_amount"].sum().nlargest(5)
top_products_details = top_products.reset_index().merge(df_products,on="product_id")
plt.figure(figsize=(12, 7))
sns.barplot(x="product_name", y="total_amount", data=top_products_details,
palette="viridis")
plt.title("Top 5 Products by Total Sales Amount")
plt.xlabel("Product Name")
plt.ylabel("Total Sales Amount")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Plot 2: Total Sales by City
sales_by_city = df_sales.groupby("city")["total_amount"].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 7))
sns.barplot(x=sales_by_city.index, y=sales_by_city.values, palette="magma")
plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales Amount")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# # Plot 3: Monthly Sales Trend
df_sales["order_date"] = pd.to_datetime(df_sales["order_date"])
df_sales["month"] = df_sales["order_date"].dt.to_period("M")
monthly_sales = df_sales.groupby("month")["total_amount"].sum()
plt.figure(figsize=(14, 7))
monthly_sales.plot(kind="line", marker="o", color="#3498DB")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales Amount")
plt.grid(True)
plt.tight_layout()
plt.show()

# # Plot 4: Sales by Product Category (Pie Chart)
sales_by_category = df_sales.merge(df_products, on="product_id")
sales_by_category = sales_by_category.groupby("category")["total_amount"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 10))
plt.pie(sales_by_category, labels=sales_by_category.index,
autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
plt.title("Total Sales by Product Category")
plt.axis("equal") # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()

