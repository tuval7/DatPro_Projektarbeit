# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 17:37:58 2025

@author: tuval7
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from constants import T

"""
Mit Hilfe von matplotlib pyplot und animation lässt sich ein Video aus den Daten erstellen.
Zuerst werden die Dauer des Videos und die Frameanzal fesgelegt.
Außerdem werden die Positiondaten ausgelesen und so aufbereitet, 
dass sie für das Animationupdate nutzbar sind.
Dann wird die Figur mit Koordinatensystem und den Teilchen als blauen Punkten erstellt.
Die Erstellung des Videos läuft über eine update-Funktion, die nach und nach 
die einzelen Frames mit den Punkten zu jedem Zeitpunkt berechnet. 
Diese Bilder werden zu einem Video (gif) zusammen gefügt und abgespeichert.
"""
 
time = T
fps = 30

df = pd.read_csv("output.txt", sep="\t", header=None)
number_of_particles = (df.shape[1] - 2) // 4

x_data = np.array([df[2 +4*i].values for i in range(number_of_particles)])
y_data = np.array([df[3 +4*i].values for i in range(number_of_particles)])

n_frames = int(time * fps)
indices = np.linspace(0, len(df)-1, n_frames, dtype=int)

x_frames = x_data[:, indices]
y_frames = y_data[:, indices]

fig, ax = plt.subplots(figsize=(6, 6))
dots, = ax.plot([], [], "o", color="blue", markersize="5")

ax.set_xlim(-5, 105)
ax.set_ylim(-5, 105)
ax.set_title("Teilchenanimation")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)

def update(frame_idx):
    dots.set_data(x_frames[:, frame_idx], y_frames[:, frame_idx])
    return dots,

ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=1000 / fps, blit=True)

ani.save("Teilchen_Animation.gif", writer="pillow", fps=30)