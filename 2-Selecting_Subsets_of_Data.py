# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:51:11 2021

@author: Cennetgül Yılmaz
"""

import pandas as pd
df=pd.read_csv(r"C:\Users\asus\Desktop\Yapay_Zeka_Proje\coronavirus_dataset\covid_19_data.csv")
print(df)

first=df["Province/State"]
print(first)

second=df[["Province/State","Country/Region"]]
print(second)

c1=df.loc[1]
print(c1)

c2=df.loc[1:55]
print(c2)

c3=df.loc[:,"Province/State"]
print(c3)

c4=df.loc[:,["Province/State","Country/Region"]]
print(c4)

c5=df.loc[3:45,["Province/State","Country/Region"]]
print(c5)

c6=df.iloc[5]
print(c6)

c7=df[df.Deaths<10]
print(c7)

c8=df[df.Recovered>55]
print(c8)