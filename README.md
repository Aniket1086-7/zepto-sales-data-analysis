# Zepto Sales Data Analysis

## Project Overview

This project analyses a Zepto sales dataset using Python to identify sales patterns, leading products, city-wise performance, delivery trends, and product-category performance.

The dataset contains more than 220,000 sales records.

## Objectives

* Clean missing and duplicate data
* Analyse minimum, maximum, and average order amounts
* Identify the top five products by sales
* Compare total sales across cities
* Calculate average delivery time by city
* Examine monthly sales trends
* Analyse sales across product categories
* Present the findings through charts

## Tools and Technologies

* Python
* Pandas
* Matplotlib
* Seaborn

## Project Structure

| File                    | Purpose                                        |
| ----------------------- | ---------------------------------------------- |
| `load_data.py`          | Loads and explores the datasets                |
| `data_cleaning.py`      | Handles missing values and duplicate records   |
| `data_analysis.py`      | Performs sales and delivery analysis           |
| `data_visualization.py` | Creates charts for the findings                |
| `zepto_sales.csv`       | Contains the sales transaction data            |
| `zepto_products.csv`    | Contains product names, categories, and prices |
| `requirements.txt`      | Lists the required Python libraries            |

## Analysis Performed

* Descriptive analysis of order amounts
* Top five products by total sales
* Total sales by city
* Average delivery time by city
* Monthly sales trend
* Total sales by product category

## Key Findings

* Mumbai generated the highest total sales.
* Handwash was the leading product by total sales.
* Personal Care was the highest-performing product category.
* The analysis revealed differences in sales and delivery performance across cities.
* Monthly sales analysis helped identify changes in sales performance over time.

## Visualizations

The project includes:

* Bar chart of the top five products
* Bar chart of total sales by city
* Line chart of monthly sales
* Pie chart of sales by product category

## How to Run the Project

1. Download or clone this repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the Python files:

```bash
python load_data.py
python data_cleaning.py
python data_analysis.py
python data_visualization.py
```

## Author

Aniket
