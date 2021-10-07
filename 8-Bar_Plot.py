# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:05:21 2021

@author: Cennetgül Yılmaz
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\asus\Desktop\Yapay_Zeka_Proje\coronavirus_dataset\covid_19_data.csv")

turkey=df[df["Country/Region"]=="Turkey"]
italy=df[df["Country/Region"]=="Italy"]
spain=df[df["Country/Region"]=="Spain"]
"""
plt.bar(turkey.Deaths,turkey.Recovered)
plt.show()
"""
ülke=["Türkiye","Abd","Almanya","İtalya","İspanya","Fransa","Güney Kore","Japonya","UK","Çin","Hindistan"]
oran=[40,34.7,29.2,12.5,11.6,10.6,9.7,7.3,6.6,3.6,2.3]
plt.xlabel("Ülkeler")
plt.ylabel("Oranlar")
plt.title("Yoğun Bakım Yatak Sayısı")
plt.bar(ülke,oran)
plt.show()