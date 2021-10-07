# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:30:30 2021

@author: Cennetgül Yılmaz
"""

import pandas as pd
df=pd.read_csv(r"C:\Users\asus\Desktop\Yapay_Zeka_Proje\coronavirus_dataset\covid_19_data.csv")
"""
a1=df.sort_values(by='Deaths',ascending=False).head(20) 
print(a1) 


a1.drop(171774)
print(a1)

a1=a1.drop(171774)
print(a1.sort_values(by='Deaths',ascending=False).head(20))

a1.drop(171014,inplace=True)
print(a1.sort_values(by='Deaths',ascending=False).head(20))

a1=a1.drop("SNo",axis=1)
print(a1.sort_values(by='Deaths',ascending=False).head(20))

a1=a1.drop(columns="Confirmed")
print(a1.columns) 



ort=(df.groupby("Province/State")["Deaths"].mean().head(10))
print(ort)

x1=(df.groupby("Province/State")["Deaths"].max().head(10))
print(x1)

x2=(df.groupby(["Province/State","Country/Region"])["Deaths"].max().head(10))
print(x2)
"""
print(df.isnull().sum())


df["Province/State"].fillna(method="ffill",inplace=True)

print(df.isnull().sum())


#df=df.dropna()