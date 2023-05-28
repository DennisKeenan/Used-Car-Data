import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from pickle import dump
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
# print(car["fuel_type"].isna().sum())
car["fuel_type"]=car["fuel_type"].astype(str)
    # Car Name Slciing 
car["name"]=car["name"].str.split(" ").str.slice(0,3).str.join(" ")
    # Car Data Fixation
car=car[car["Price"]<1000000000].reset_index(drop=True)
car=car[car["kms_driven"]<300000].reset_index(drop=True)
car=car[car["fuel_type"]!="LPG"].reset_index(drop=True)
car=car[~((car["name"]=="Maruti Suzuki Zen") & (car["kms_driven"]==0))].reset_index(drop=True)
# print(car.info())


# # Relations
#     # Relation between company and prices
# plot.subplots(figsize=(15,7))
# ax=sb.boxplot(x="company",y="Price",data=car)
# ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha="right")
# plot.ticklabel_format(style="plain",axis="y")
#     # Relation between year and prices 
# plot.subplots(figsize=(15,7))
# ax=sb.boxplot(x="year",y="Price",data=car)
# ax.set_xticklabels(ax.get_xticklabels(),rotation=40,ha="right")
# plot.ticklabel_format(style="plain",axis="y")
#     # Relation between range and prices 
# plot.subplots(figsize=(15,7))
# ax=sb.relplot(x="kms_driven",y="Price",data=car)
#     # Relation between fuel type and prices
# plot.subplots(figsize=(15,7))
# ax=sb.relplot(x="fuel_type",y="Price",data=car)
#     # Relation between company, price, fuel type, and year
# ax=sb.relplot(x="company",y="Price",data=car,hue="fuel_type",size="year",height=7,aspect=2)
# ax.set_xticklabels(rotation=40,ha="right")
# plot.show()


# Car Price Ai
X=car[["name","company","year","kms_driven","fuel_type"]]
Y=car["Price"]
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2)

    # OneHotEncoder Creation
ohe= OneHotEncoder()
ohe.fit(X[["name","company","fuel_type"]])
column_trans=make_column_transformer((OneHotEncoder(categories=ohe.categories_),["name","company","fuel_type"]),remainder="passthrough")
# print(ohe.categories_)
# print("="*100)
# print(column_trans)

    # Linear Regression
lr=LinearRegression()
pipe=make_pipeline(column_trans,lr)
pipe.fit(X_train,Y_train)
# Y_predict=pipe.predict(X_test)
# print(r2_score(Y_test,Y_predict))

    # Score
score=[]
# for i in range(1000):
#     X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.1,random_state=i)
#     lr=LinearRegression()
#     pipe=make_pipeline(column_trans,lr)
#     pipe.fit(X_train,Y_train)
#     Y_predict=pipe.predict(X_test)
#     score.append(r2_score(Y_test,Y_predict))
# print(score[np.argmax(score)])

    # Registering Car
# car_brand=input("Please enter your car's brand: ")
# car_name=input("Please enter your car's name: ")
# car_year=int(input("Please enter your car's year: "))
# car_kms_driven=int(input("Please enter your car's mileage(Km): "))
# car_fuel_type=input("Please enter your car's fuel type: ")
# resultprice=pipe.predict(pd.DataFrame(columns=X_test.columns,data=np.array([car_name,car_brand,car_year,car_kms_driven,car_fuel_type])
#                                       .reshape(1,5)))
# print("According to AI calculations, your car will cost around: ",resultprice)


# File
dump(pipe,open("Car Price AI","wb"))