import pandas as pd 
df_sales = pd.read_csv("zepto_sales.csv")
df_products = pd.read_csv("zepto_products.csv")

# Find min, max, and average total amount
min_amount = df_sales["total_amount"].min()
max_amount = df_sales["total_amount"].max()
avg_amount = df_sales["total_amount"].mean()
print(f"\nMin Total Amount: {min_amount:.2f}")
print(f"Max Total Amount: {max_amount:.2f}")
print(f"Average Total Amount: {avg_amount:.2f}")
# Top 5 products by total sales amount
top_products = df_sales.groupby("product_id")["total_amount"].sum().nlargest(5)
print("\n--- Top 5 Products by Sales Amount ---")
print(top_products)
# Merge with product details to get product names
top_products_details = top_products.reset_index().merge(df_products,
on="product_id")
print("\n--- Top 5 Products by Sales Amount (with names) ---")
print(top_products_details[["product_name", "category", "total_amount"]])
# Total sales by city
sales_by_city = df_sales.groupby("city")["total_amount"].sum().sort_values(ascending=False)
print("\n--- Total Sales by City ---")
print(sales_by_city)
# Average delivery time by city
avg_delivery_time_by_city = df_sales.groupby("city")["delivery_time_mins"].mean().sort_values()
print("\n--- Average Delivery Time by City (minutes) ---")
print(avg_delivery_time_by_city)
# Convert order_date into datetime format
df_sales["order_date"] = pd.to_datetime(df_sales["order_date"])

# Calculate monthly sales
df_sales["month"] = df_sales["order_date"].dt.to_period("M")
# Sales trend over time (e.g., monthly sales)
df_sales["month"] = df_sales["order_date"].dt.to_period("M")
monthly_sales = df_sales.groupby("month")["total_amount"].sum()
print("\n--- Monthly Sales Trend ---")
print(monthly_sales)
# Sales by product category
sales_by_category = df_sales.merge(df_products, on="product_id")
sales_by_category = sales_by_category.groupby("category")["total_amount"].sum().sort_values(ascending=False)
print("\n--- Total Sales by Product Category ---")
print(sales_by_category)