import pandas as pd
# Load the datasets
df_sales = pd.read_csv("zepto_sales.csv")
df_products = pd.read_csv("zepto_products.csv")
# Display basic information for sales data
print("\n--- Sales Data Info ---")
df_sales.info()
print("\n--- Sales Data Description ---")
print(df_sales.describe())
print("\n--- Sales Data Shape ---")
print(df_sales.shape)
print("\n--- Sales Data Head ---")
print(df_sales.head())
print("\n--- Sales Data Tail ---")
print(df_sales.tail())
# Display basic information for products data
print("\n--- Products Data Info ---")
df_products.info()
print("\n--- Products Data Description ---")
print(df_products.describe())
print("\n--- Products Data Head ---")
print(df_products.head())

