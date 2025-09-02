# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 13:57:39 2025

@author: tuval7
"""

import numpy as np
import pandas as pd
from box import Box
from constants import g, dt, T, charge

class Simulation:
    def __init__(self, particle_list):
        self.particles = particle_list
        self.data = []
        self.box = Box(self)
        
    def acceleration(self, i, pos):
        xi, yi = pos
        a = np.array([0.0, g])
        
        for j, pj in enumerate(self.particles):
            if j == i:
                continue
            xj, yj, *rest = pj.state
            r_vec = np.array([xi - xj, yi - yj])
            r = np.linalg.norm(r_vec)
            if r > 1e-5:
                a += charge**2 * r_vec / (r**3)
        return a
    
    def dgl(self, i):
        def f(state):
            x, y, vx, vy = state
            a = self.acceleration(i, (x, y))
            return np.array([vx, vy, a[0], a[1]])
        return f
        
    def rk4_step(self, f, state, dt):
        k1 = dt * f(state)
        k2 = dt * f(state + 0.5 * k1)
        k3 = dt * f(state + 0.5 * k2)
        k4 = dt * f(state + k3)
        return state + (k1 + 2*k2 + 2*k3 +k4) / 6
    
    def run(self):
        steps = int(T / dt)
        for step in range(steps):
            old_state = [particle.state.copy() for particle in self.particles]
            
            for i, particle in enumerate(self.particles):
                f = self.dgl(i)
                particle.state = self.rk4_step(f, particle.state, dt)
                
            for i, particle in enumerate(self.particles):
                self.box.reflect(particle, old_state[i], i)
                
            t = step * dt
            row = [t]
            for particle in self.particles:
                row.extend(particle.state)
            self.data.append(row)
            
        df = pd.DataFrame(self.data)
        df.to_csv("output.txt", sep='\t', index=False, header=False)
