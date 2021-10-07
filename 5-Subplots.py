# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 20:32:37 2021

@author: Cennetgül Yılmaz
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\asus\Desktop\Yapay_Zeka_Proje\coronavirus_dataset\covid_19_data.csv")

turkey=df[df["Country/Region"]=="Turkey"]
italy=df[df["Country/Region"]=="Italy"]
spain=df[df["Country/Region"]=="Spain"]


df.plot(subplots=True)

plt.subplot(2,1,1)
plt.plot(turkey.Deaths,turkey.Recovered,color="red",label="Türkiye'de ölen-iyileşen hasta sayıları")
plt.xlabel("Türkiye'deki ölüm sayısı")
plt.ylabel("Türkiye'deki iyileşen hasta sayısı")


plt.subplot(2,1,2)
plt.plot(italy.Deaths,italy.Recovered,color="black",label="İtalya'da ölen-iyileşen hasta sayıları")
plt.xlabel("İtalya'daki ölüm sayısı")
plt.ylabel("İtalya'daki iyileşen hasta sayısı")

plt.show()
