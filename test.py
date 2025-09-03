# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 14:42:23 2025

@author: tuval7
"""

import unittest
from particle import Particle
from simulation import Simulation

"""
Die unittest Klasse testet verschiedenen Fälle der Simulation.
Der erste Test überprüft, ob die Energie bei einer Einteilchensimulation am Ende 
immer noch erhalten bleibt.
Der zweite Test überprüft, ob die Reflektion an den Boxwänden funktioniert,
indem geguckt wird, ob die x- und y-Koordinaten sich alle innerhalb der Box 
(mit kleinem Fehler) befinden.
Der dritte Test überprüft, die Abstoßung unter den Teichen.
Zwei Teilchen die anfangs noch aufeinander zu fliegen sollten am Ende 
der Simulationszeit einen größeren Abstand haben, da sie sich abstoßen, 
bevor sie durch die Reflexion an den Boxwänden wieder aufeinander zu fliegen.
Zum Schluss wird wieder überprüft, ob auch hier die Energie vom Start erhalten bleibt.
Der vierte Test überprüft, ob sich ein Teilchen gleichförmig in x-Richtung bewegt,
wenn es eine Anfangsgeschwindigkeit in dieser Richtung gibt.
"""

class TestSimulation(unittest.TestCase):
    
    def test_free_fall(self):
        particle = Particle(50.0, 90.0, 0.0, 0.0)
        sim = Simulation([particle])
        sim.run()
        df = sim.data
        energy_start = df[0][1]
        energy_end = df[-1][1]
        delta_E = abs(energy_start - energy_end)
        self.assertLess(delta_E, 0.1)
       
    def test_reflection(self):
        particle = Particle(99.0, 50.0, 15.0, 0.0)
        sim = Simulation([particle])
        sim.run()
        x_values = [row[2] for row in sim.data]
        y_values = [row[3] for row in sim.data]
        self.assertTrue(min(x_values) >= -0.05 and max(x_values) <= 100.05)
        self.assertTrue(min(y_values) >= -0.05 and max(y_values) <= 100.05)
     
    def test_particle_repulsion(self):
        particle1 = Particle(40.0, 50.0, 1.0, 0.0)
        particle2 = Particle(60.0, 50.0, -1.0, 0.0)
        sim = Simulation([particle1, particle2])
        sim.run()
        distances = []
        for row in sim.data:
            x1, y1 = row[2], row[3]
            x2, y2 = row[6], row[7]
            dist = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
            distances.append(dist)
        self.assertGreater(distances[-1], distances[0])
        df = sim.data
        energy_start = df[0][1]
        energy_end = df[-1][1]
        delta_E = abs(energy_start - energy_end)
        self.assertLess(delta_E, 0.1)
        
    def test_straight_motion(self):
        particle = Particle(10.0, 10.0, 5.0, 0.0)
        sim = Simulation([particle])
        sim.run()
        x_values = [row[2] for row in sim.data]
        motions = [x_values[i+1] - x_values[i] for i in range(len(x_values)-1)]
        avg_motion = sum(motions) / len(motions)
        self.assertAlmostEqual(motions[0], avg_motion)
    
if __name__ == "__main__":
    unittest.main()