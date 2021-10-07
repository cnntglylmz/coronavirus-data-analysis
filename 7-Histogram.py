# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:28:31 2021

@author: Cennetgül Yılmaz
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\asus\Desktop\Yapay_Zeka_Proje\coronavirus_dataset\covid_19_data.csv")

turkey=df[df["Country/Region"]=="Turkey"]
italy=df[df["Country/Region"]=="Italy"]
spain=df[df["Country/Region"]=="Spain"]

plt.hist(turkey.Deaths,bins=10)
plt.xlabel("Ölüm sayıları")
plt.ylabel("Değer aralığı")
plt.title("Türkiye Coronavirüs Analizi")
plt.show()

"""
plt.hist(italy.Deaths,bins=10)
plt.xlabel("Ölüm sayıları")
plt.ylabel("Değer aralığı")
plt.title("İtalya Coronavirüs Analizi")
plt.show()

plt.hist(spain.Deaths,bins=10)
plt.xlabel("Ölüm sayıları")
plt.ylabel("Değer aralığı")
plt.title("İspanya Coronavirüs Analizi")
plt.show()
"""