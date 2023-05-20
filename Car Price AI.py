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
    # Range Fixation
car["kms_driven"]=car["kms_driven"].str.replace(",","")
car["kms_driven"]=car["kms_driven"].str.replace(" kms","")
car=car[car["kms_driven"]!="Petrol"]
car["kms_driven"]=car["kms_driven"].astype(int)
    # Fuel Type Fixation
car=car[~ car["fuel_type"].isna()]
print(car["fuel_type"].isna().sum())
car["fuel_type"]=car["fuel_type"].astype(str)

print(car.info())
print(car["fuel_type"].unique())


