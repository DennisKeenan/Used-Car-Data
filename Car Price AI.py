import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sb
data=pd.read_csv("Used_Car.csv")


# # Data count
# print(data.shape) 
# print(data["year"].unique())
# print(data["name"].unique())
# print(data["company"].unique())
# print(data["Price"].unique())
# print(data["kms_driven"].unique())
# print(data["fuel_type"].unique())


# Data Duplicate and Fixation
car=data.copy()
    # Year Fixation
car=car[car["year"].str.isnumeric()]
car["year"]=car["year"].astype(int)
    # Price Fixation
car=car[car["Price"]!="Ask For Price"]
car["Price"]=car["Price"].str.replace(",","")
car["Price"]=car["Price"].astype(int)
car["Price"]=car["Price"]*179.91
    # Range Fixation
car["kms_driven"]=car["kms_driven"].str.replace(",","")
car["kms_driven"]=car["kms_driven"].str.replace(" kms","")
car=car[car["kms_driven"]!="Petrol"]
car["kms_driven"]=car["kms_driven"].astype(int)
    # Fuel Type Fixation
car=car[~ car["fuel_type"].isna()]
print(car["fuel_type"].isna().sum())
car["fuel_type"]=car["fuel_type"].astype(str)
    # Car Name Slciing 
car["name"]=car["name"].str.split(" ").str.slice(0,3).str.join(" ")
    # Car Data Fixation
car=car[car["Price"]<1000000000].reset_index(drop=True)
car=car[car["kms_driven"]<300000].reset_index(drop=True)
car=car[car["fuel_type"]!="LPG"].reset_index(drop=True)
car=car[~((car["name"]=="Maruti Suzuki Zen") & (car["kms_driven"]==0))].reset_index(drop=True)
print(car.info())


# Relations
    # Relation between company and prices
plot.subplots(figsize=(15,7))
ax=sb.boxplot(x="company",y="Price",data=car)
ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha="right")
plot.ticklabel_format(style="plain",axis="y")
    # Relation between year and prices 
plot.subplots(figsize=(15,7))
ax=sb.boxplot(x="year",y="Price",data=car)
ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha="right")
plot.ticklabel_format(style="plain",axis="y")
    # Relation between range and prices 
plot.subplots(figsize=(15,7))
ax=sb.relplot(x="kms_driven",y="Price",data=car)
    # Relation between fuel type and prices

plot.show()
