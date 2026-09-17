import pandas as pd
#Read the csv file first
df = pd.read_csv("data/sales.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape of Data:")
print(df.shape)

print("\nData Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

#Add total_sales colume by doing vectorized operation.
df["total_sales"] = df["quantity"] * df["price"]
df["date"] = pd.to_datetime(df["date"])
#Now find the total quality,Average price, and total_sales.
total_sales = df["total_sales"].sum()
total_quantity = df["quantity"].sum()
average_price = df["price"].mean()
highest_sales = df["total_sales"].max()
lowest_sales = df["total_sales"].min()
#Now we move on to best product and city.
product_analysis = df.groupby("product")["total_sales"].sum()
#Here we only consider one coulum that total_sales what if the manger asks best product according to sales,quality,price,Then.
product_analysis = df.groupby("product").agg({
    "total_sales" : "sum",
    "quantity" : "sum",
    "price" : "mean"
    }
)
#We can also do it different way Giving name to the Columns.
product_analysis = df.groupby("product").agg(
    total_quantity = ("quantity","sum"),
    average_price = ("price","mean"),
    total_sales = ("total_sales","sum")
)
#Now sort the product table highest to lowest according to total_sales.
product_analysis = product_analysis.sort_values("total_sales",ascending=False)
best_product = product_analysis.index[0] 
            #OR
best_product1 = product_analysis.idxmax()

#Now same with the Best City
city_analysis = df.groupby("city").agg(
    total_sales = ("total_sales","sum"),
    total_quantity = ("quantity","sum"),
    average_price = ("price","mean")
)
city_analysis = city_analysis.sort_values("total_sales",ascending=False)
best_city = city_analysis.index[0]
#It will give best product from evey colunm like total_sales,average_price,total_quantity without using sorting.
best_city1 = city_analysis.idxmax()

#Print all those things.
print("\n========== SALES SUMMARY ==========")
print("Total Sales : ", total_sales)
print("Total Quantity : ", total_quantity)
print("Average Price : ", average_price)
print("Highest Sales : ", highest_sales)
print("Lowest Sales : ", lowest_sales)


print("\n========== PRODUCT ANALYSIS ==========")

print(product_analysis)

print("\n========== CITY ANALYSIS ==========")

print(city_analysis)

print("Best Products in every cateogry : ", best_product1)
print("Overall Best Product : ", best_product)
print("Best cities in every cateogry : ", best_city1)
print("Overall Best City : ", best_city)

product_analysis.to_csv("output/product_analysis.csv")
city_analysis.to_csv("output/city_analysis.csv")
print("\nAnalysis files created successfully!")