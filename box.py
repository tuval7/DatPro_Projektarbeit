# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 13:56:31 2025

@author: tuval7
"""

import numpy as np
from constants import box_xmin, box_xmax, box_ymin, box_ymax, dt

class Box:
    def __init__(self, simulation):
        self.sim = simulation
        
    def reflect(self, particle, old_state, index):
        x0, y0, _, _ = old_state
        x1, y1, _, _ = particle.state
        portion_x = portion_y = 1.0
        
        if x1 < box_xmin or x1 > box_xmax:
            dx = x1 -x0
            if dx != 0:
                portion_x = (box_xmin - x0) / dx if x1 < box_xmin else (box_xmax -x0) / dx
                
        if y1 < box_ymin or y1 > box_ymax:
            dy = y1 - y0
            if dy != 0:
                portion_y = (box_ymin - y0) / dy if y1 < box_ymin else (box_ymax -y0) / dy
                
        portion_hit = min(portion_x, portion_y)
        
        if portion_hit < 1.0:
            dt_hit = portion_hit * dt
            dt_rest = dt - dt_hit
            particle.state = old_state.copy()
            
            def f(state):
                x, y, vx, vy = state
                a = self.sim.acceleration(index, (x, y))
                return np.array([vx, vy, a[0], a[1]])
            
            particle.state = self.sim.rk4_step(f, particle.state, dt_hit)
            
            x, y, vx, vy = particle.state
            if x <= box_xmin or x >= box_xmax:
                vx *= -1 
            if y <= box_ymin or y >= box_ymax:
                vy *= -1 
            
            particle.state = np.array([
                np.clip(x, box_xmin, box_xmax),
                np.clip(y, box_ymin, box_ymax),
                vx, vy])
            
            particle.state = self.sim.rk4_step(f, particle.state, dt_rest)