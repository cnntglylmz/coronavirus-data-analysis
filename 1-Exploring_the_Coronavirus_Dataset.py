# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:04:58 2021

@author: Cennetgül Yılmaz
"""
import pandas as pd
df=pd.read_csv(r"C:\Users\asus\Desktop\Yapay_Zeka_Proje\coronavirus_dataset\covid_19_data.csv")

print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.isnull().sum())
print(df.describe())
print(df["Province/State"].describe())

a=(df.describe(include=["O"]))
print(a)

b=(df["Country/Region"].value_counts())
print(b)

print(df[df["Province/State"]=="Chicago"])

