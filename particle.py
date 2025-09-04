# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 13:37:50 2025

@author: tuval7
"""

import numpy as np
from constants import mass, charge

"""
Grundlegende Klasse die die einzelene Teilchen als state-Vektoren abspeichert. 
Außerdem eine repr-Methode und eine Routine zum Kopieren der Zustände.
"""

class Particle:
    def __init__(self, x, y, vx, vy, m=mass, q=charge):
        self.state = np.array([x, y, vx, vy], dtype=float)
        self.m = m
        self.q = q
        
    def __repr__(self):
        return f"Particle(state={self.state}"
    
    def copy(self):
        return Particle(self.state)
