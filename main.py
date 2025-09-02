# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 13:59:24 2025

@author: tuval7
"""

from particle import Particle
from simulation import Simulation

"""
Die Mainmethode startet die Simulation und hier lassen sich die Startwerte der
beliebig vielen Teilchen eingeben.
"""

if __name__ == "__main__":

    particle_list = [
        Particle(1.0, 45.0, 10.0, 0.0),
        Particle(99.0, 55.0, -10.0, 0.0),
        Particle(10.0, 50.0, 15.0, -15.0),
        Particle(20.0, 30.0, -15.0, -15.0),
        Particle(80.0, 70.0, 15.0, 15.0),
        Particle(80.0, 60.0, 15.0, 15.0),
        Particle(80.0, 50.0, 15.0, 15.0)]
    
    sim = Simulation(particle_list)
    sim.run()
    