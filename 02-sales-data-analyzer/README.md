# 🟢 Project 2 — Sales Data Analyzer

A beginner-friendly sales data analysis project built with **Python and Pandas**.

The project demonstrates how raw sales data can be inspected, cleaned, transformed, analyzed, and exported into useful business summaries.

This project includes both **clean data** and **intentionally bad data** to practice real-world data cleaning.

---

## 🎯 Project Objective

The goal of this project is to build a simple Sales Data Analyzer that can answer questions such as:

- What are the total sales?
- How many products were sold?
- What is the average product price?
- What was the highest-value sale?
- What was the lowest-value sale?
- Which product generated the most sales?
- Which city generated the most sales?

The project also demonstrates how to handle common problems found in real-world datasets.

---

## 📂 Project Structure

```text
02-sales-data-analyzer/
│
├── data/
│   ├── sales.csv
│   └── sales_bad.csv
│
├── output/
│   ├── city_analysis.csv
│   ├── city_analysis_bad_data.csv
│   ├── product_analysis.csv
│   └── product_analysis_bad_data.csv
│
├── analysis_sales.py
├── analysis_sales_bad_data.py
└── README.md
📊 Dataset

The dataset contains the following columns:

Column	Description
date	Date of the sale
product	Product sold
quantity	Number of units sold
price	Unit price of the product
city	City where the sale occurred

Example:

date,product,quantity,price,city
2026-01-01,Laptop,2,60000,Hyderabad
2026-01-01,Mouse,5,800,Delhi
2026-01-02,Keyboard,3,1500,Mumbai
🟢 Clean Data Analysis

The clean dataset is:

data/sales.csv

The analysis is performed using:

analysis_sales.py

The clean dataset is used to understand the basic Pandas analysis workflow.

sales.csv
    ↓
Pandas
    ↓
DataFrame
    ↓
Calculate total_sales
    ↓
Analyze
    ↓
Product Analysis
    ↓
City Analysis
    ↓
CSV Output

Generated files:

output/
├── product_analysis.csv
└── city_analysis.csv
🔴 Bad Data Analysis

The bad dataset is:

data/sales_bad.csv

This dataset was intentionally created with common real-world data problems.

The analysis is performed using:

analysis_sales_bad_data.py
🧹 Data Cleaning

The bad dataset contains:

Leading/trailing spaces
Inconsistent capitalization
Missing quantity
Missing price
Incorrect numeric data types caused by missing values
Text Cleaning
df["product"] = df["product"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()

This standardizes values such as:

" Keyboard"  → "Keyboard"
"laptop"     → "Laptop"
" Hyderabad" → "Hyderabad"
Handling Missing Quantity

Rows with missing quantity were removed because a missing quantity makes it impossible to reliably calculate the transaction's total sales.

df = df.dropna(subset=["quantity"])
Handling Missing Price

The missing Keyboard price was filled using known information from the dataset.

df.loc[
    (df["product"] == "Keyboard") & (df["price"].isna()),
    "price"
] = 1500

This demonstrates that missing values should not always be filled with an arbitrary value. The correct approach depends on the meaning of the data and available information.

🔢 Data Type Conversion

The date column was converted into a Pandas datetime type:

df["date"] = pd.to_datetime(df["date"])

After handling missing values, the numeric columns were converted to integers:

df["quantity"] = df["quantity"].astype(int)
df["price"] = df["price"].astype(int)
💰 Total Sales Calculation

Total sales for each transaction are calculated using:

Total Sales = Quantity × Price

In Pandas:

df["total_sales"] = df["quantity"] * df["price"]

This uses a vectorized Pandas operation rather than manually processing every row.

Example:

Quantity = 2
Price = ₹60,000

Total Sales = 2 × ₹60,000
            = ₹1,20,000
📈 Analysis Performed
Overall Sales Analysis

The program calculates:

total_sales = df["total_sales"].sum()
total_quantity = df["quantity"].sum()
average_price = df["price"].mean()
highest_sales = df["total_sales"].max()
lowest_sales = df["total_sales"].min()

These provide:

Total sales
Total quantity
Average price
Highest transaction value
Lowest transaction value
📦 Product Analysis

Products are grouped and analyzed using:

product_analysis = df.groupby("product").agg(
    total_sales=("total_sales", "sum"),
    total_quantity=("quantity", "sum"),
    average_price=("price", "mean")
)

The results are sorted by total sales:

product_analysis = product_analysis.sort_values(
    "total_sales",
    ascending=False
)

The product with the highest total sales can then be identified using:

best_product = product_analysis["total_sales"].idxmax()
🌆 City Analysis

The same approach is used to analyze sales by city:

city_analysis = df.groupby("city").agg(
    total_sales=("total_sales", "sum"),
    total_quantity=("quantity", "sum"),
    average_price=("price", "mean")
)

The results are sorted by total sales:

city_analysis = city_analysis.sort_values(
    "total_sales",
    ascending=False
)

The city with the highest total sales can be identified using:

best_city = city_analysis["total_sales"].idxmax()
📁 Output

The analysis results are exported as CSV files.

Clean Data
output/
├── product_analysis.csv
└── city_analysis.csv
Bad Data
output/
├── product_analysis_bad_data.csv
└── city_analysis_bad_data.csv
🛠️ Technologies Used
Python
Pandas
CSV
Git
GitHub
🧠 Pandas Concepts Learned

This project introduced and practiced:

read_csv()
DataFrame
Series
columns
rows

head()
tail()
shape
info()
describe()

iloc
loc
Boolean filtering

isnull()
isna()
dropna()
fillna()

str.strip()
str.title()

pd.to_datetime()
astype()

sum()
mean()
max()
min()

sort_values()
groupby()
agg()
idxmax()

iterrows()
Vectorized operations

to_csv()
💡 Key Learning

One of the main lessons from this project was that data analysis starts with data quality.

Before calculating statistics, the data needs to be:

Raw Data
   ↓
Inspect
   ↓
Clean
   ↓
Handle Missing Values
   ↓
Fix Data Types
   ↓
Calculate
   ↓
Analyze
   ↓
Export

The project also demonstrated why missing values should be handled according to the meaning of the data rather than blindly applying dropna() or fillna().

🚀 Future Improvements

Possible improvements for future versions include:

Analyze sales by date
Analyze monthly sales
Add visualizations using Matplotlib
Create automated reports
Read multiple sales files
Add data validation
Export results to Excel
Build a dashboard
Process larger datasets

These improvements will be explored in later projects in this portfolio.

📚 Learning Context

This project is part of my AI Engineering Portfolio, where projects are developed progressively from Python fundamentals toward data engineering, machine learning, and AI engineering.

The focus is not only on completing the project but also on understanding:

Why each technology is used
How the code works
Data-cleaning decisions
Alternative approaches
Error handling
Real-world applications
Possible improvements
👨‍💻 Project Status

🟢 Completed

Project: Sales Data Analyzer
Level: Beginner+
Main Technology: Python + Pandas