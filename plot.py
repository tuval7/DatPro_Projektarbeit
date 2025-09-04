# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 13:01:11 2025

@author: tuval7
"""

import pandas as pd
import matplotlib.pyplot as plt 

"""
Dieses Programm liest die outputdatei mit pandas aus und plotet mit matplotlib 
die Gesamtenergie gegen die Zeit, die Bahn des ersten Teilchens isoliert 
und dann die Bahnen aller Teilchen in einem Plot. 
Alle Plots werden abgespeichert.
"""

df = pd.read_csv("output.txt", sep='\t', header=None)
n = (df.shape[1] - 2) // 4

plt.figure()
plt.plot(df[0], df[1])
plt.xlabel("Zeit [s]")
plt.ylabel("Gesamtenergie")
plt.title("Enegieverlauf")
plt.grid()
plt.savefig("Energieverlauf.png")

plt.figure()
plt.plot(df[2], df[3])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Bahn des ersten Teilchens")
plt.axis("equal")
plt.grid()
plt.savefig("Bahn_Teilchen_1")

plt.figure()
for i in range(n):
    x = df[2 + 4*i]
    y = df[3 + 4*i]
    plt.plot(x, y, label=f"Teilchen {i+1}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Bahnen aller Teilchen")
plt.legend()
plt.axis("equal")
plt.grid()
plt.savefig("Bahnen_aller_Teilchen")
