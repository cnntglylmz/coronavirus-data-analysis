# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:09:04 2021

@author: Cennetgül Yılmaz
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\asus\Desktop\Yapay_Zeka_Proje\coronavirus_dataset\covid_19_data.csv")

turkey=df[df["Country/Region"]=="Turkey"]
italy=df[df["Country/Region"]=="Italy"]
spain=df[df["Country/Region"]=="Spain"]

plt.scatter(turkey.Deaths,turkey.Recovered,color="red",label="Türkiye'deki ölen-kurtulan hasta sayıları")
plt.scatter(italy.Deaths,italy.Recovered,color="blue",label="İtalya'daki ölen-kurtulan hasta sayıları")
plt.scatter(spain.Deaths,spain.Recovered,color="black",label="İspanya'daki ölen-kurtulan hasta sayıları")

plt.xlabel("Ölüm sayısı")
plt.ylabel("Kurtulan hasta sayısı") 
plt.title("Dünyadaki Coronavirüs Analizi") 
plt.legend()
plt.show()  

 
