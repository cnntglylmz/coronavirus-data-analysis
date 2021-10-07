# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:43:16 2021

@author: Cennetgül Yılmaz
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\asus\Desktop\Yapay_Zeka_Proje\coronavirus_dataset\covid_19_data.csv")


df.plot()
plt.show()

df=df.drop("SNo",axis=1)
df.plot()
plt.show()


"""
turkey=df[df["Country/Region"]=="Turkey"]
print(turkey.columns)


plt.plot(turkey.Deaths,turkey.Recovered,color="red",label="Türkiye'de ölen-kurtulan hasta sayıları")
plt.xlabel("Ölüm sayısı")
plt.ylabel("Kurtulan hasta sayısı")
plt.title("Türkiye'deki Coronavirüs Analizi")
plt.legend()
plt.show()



italy=df[df["Country/Region"]=="Italy"]
plt.plot(italy.Deaths,italy.Recovered,color="blue",label="İtalya'da ölen-kurtulan hasta sayıları")
plt.xlabel("Ölüm sayısı")
plt.ylabel("Kurtulan hasta sayısı")
plt.title("İtalya'daki Coronavirüs Analizi")
plt.legend()
plt.show()



china=df[df["Country/Region"]=="Mainland China"]
plt.plot(china.Deaths,china.Recovered,color="purple",label="Çin'de ölen-kurtulan hasta sayıları")
plt.xlabel("Ölüm sayısı")
plt.ylabel("Kurtulan hasta sayısı")
plt.title("Çin'deki Coronavirüs Analizi")
plt.legend()
plt.show()



spain=df[df["Country/Region"]=="Spain"]
plt.plot(spain.Deaths,spain.Recovered,color="yellow",label="İspanya'da ölen-kurtulan hasta sayıları")
plt.xlabel("Ölüm sayısı")
plt.ylabel("Kurtulan hasta sayısı")
plt.title("İspanya'daki Coronavirüs Analizi")
plt.legend()
plt.show()


df.plot(grid=True,linestyle=":")
plt.show()

"""