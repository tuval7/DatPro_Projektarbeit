# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 14:07:17 2025

@author: tuval7
"""

import numpy as np
from constants import mass, charge, g

"""
Die Routine total_energy berechnet die Gesamtenergie des Systems. 
Hierzu wird erst die potenzielle und die kinetische Energie berechnet.
Daraufhin werden alle Teilchenpaare durchgegangen und die 
elektrische potenzielle Energie berchnet. 
Wird diese addiert erhält man die Gesamtenergie.
"""

def total_energy(particle_list):
    E = 0.0
    
    for i in range(len(particle_list)):
        x, y, vx, vy = particle_list[i].state
        E += mass * -g * y + 0.5 * mass * (vx**2 + vy**2)
        
        for j in range(i+1, len(particle_list)):
            dx = x - particle_list[j].state[0]
            dy = y - particle_list[j].state[1]
            r = np.hypot(dx, dy)
            E += charge**2 / r
            
    return E
                