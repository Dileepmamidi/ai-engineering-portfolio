import pandas as pd

df = pd.read_csv("data/sales_bad.csv")
#Now know about the datatypes of colunm.
df.info()
#Change the datatype of the date into datetime.
df["date"] = pd.to_datetime(df["date"])
#Now see how null coulumns are present in the table.
df.isnull().sum()
#Now remove spaces fro the strings to do that.
df["product"] = df["product"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()
#Now look into the data and decide where you want to drop the data or fill the data in colunms.
#According to my data.
df = df.dropna(subset=["quantity"])
#According to my data,I removed the quantity null row
df["price"]=df["price"].fillna(1500)
#OR
df.loc[(df["product"] == "Keyboard") & (df["price"].isna()),"price"] = 1500
#If we observe the data or table it will float for the int colunms.
#Let has change them into int.
df["quantity"] = df["quantity"].astype(int)
df["price"] = df["price"].astype(int)

total_sales = []
for index,row in df.iterrows():
    total = row["quantity"] * row["price"]
    total_sales.append(total)
df["total_sales"] = total_sales

total_sales = df["total_sales"].sum()
total_quantity = df["quantity"].sum()
average_price = df["price"].mean()
highest_sales = df["total_sales"].max()
lowest_sales = df["total_sales"].min()

#Best_product
product_analysis = df.groupby("product").agg(
    total_sales = ("total_sales","sum"),
    total_quantity = ("quantity","sum"),
    average_price = ("price","mean")
)
product_analysis = product_analysis.sort_values("total_sales",ascending=False)
best_product = product_analysis["total_sales"].idxmax()

#Best_City
city_analysis = df.groupby("city").agg(
    total_sales = ("total_sales","sum"),
    total_quantity = ("quantity","sum"),
    average_price = ("price","mean")
)
city_analysis = city_analysis.sort_values("total_sales",ascending=False)
best_city = city_analysis["total_sales"].idxmax()

print("\n========== SALES SUMMARY ==========")

print("Total Sales : ", total_sales)
print("Total Quantity : ", total_quantity)
print("Average Price : ", average_price)
print("Highest Total Sales : ", highest_sales)
print("Lowest Total Sales : ", lowest_sales)
print("Best Product : ", best_product)
print("Best City : ", best_city)

print("\n========== PRODUCT ANALYSIS ==========")

print(product_analysis)

print("\n========== CITY ANALYSIS ==========")

print(city_analysis)

product_analysis.to_csv("output/product_analysis_bad_data.csv")
city_analysis.to_csv("output/city_analysis_bad_data.csv")
print("\nAnalysis files created successfully!")







