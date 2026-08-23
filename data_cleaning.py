import pandas as pd
df_sales = pd.read_csv("zepto_sales.csv")
df_products = pd.read_csv("zepto_products.csv")

# Check for null values in sales data
print("\n--- Null Values in Sales Data ---")
print(df_sales.isnull().sum())
# Handle null values in 'city' and 'delivery_status' by dropping rows
df_sales.dropna(subset=["city", "delivery_status"], inplace=True)
print("\nNulls after dropping rows in city/delivery_status:")
print(df_sales[["city", "delivery_status"]].isnull().sum())
# Handle null values in 'delivery_time_mins' by filling with the mean
mean_delivery_time = df_sales["delivery_time_mins"].mean()
df_sales["delivery_time_mins"].fillna(mean_delivery_time, inplace=True)
print("\nNulls after filling mean in delivery_time_mins:")
print(df_sales["delivery_time_mins"].isnull().sum())
# Check for duplicate records
print("\n--- Duplicate Records in Sales Data ---")
print(f"Number of duplicate rows: {df_sales.duplicated().sum()}")
# Remove duplicate records
df_sales.drop_duplicates(inplace=True)
print(f"Number of rows after removing duplicates: {df_sales.shape[0]}")
# Convert 'order_date' to datetime objects
df_sales["order_date"] = pd.to_datetime(df_sales["order_date"])
