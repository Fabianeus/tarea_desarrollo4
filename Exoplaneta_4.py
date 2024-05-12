#!/usr/bin/env python
# coding: utf-8

# In[1]:


import astropy as astropy
import math
import pandas as pd
import numpy as np
from astropy.constants import G


# ## Un exoplaneta es un planeta con una estrella anfitriona que no es el Sol. Un
# 
# exoplaneta hereda de planeta. Sin embargo, tiene dos funciones públicas adicionales. 
# La primera determina el método de primer descubrimiento, si por
# ”imagen directa”, ”velocidad radial” o ”tránsito”. 
# La segunda determina si el planeta es similar a Tatooine (por ejemplo, un planeta orbitando una estrella
# binaria). Si el planeta es un tránsito, informa adicionalmente su "parámetro de
# impacto" 
# 
#  $  b = a \cdot \cos(i) \cdot \left( \frac{1 - e^2}{R \cdot (1 + e \cdot \sin(\omega))} \right) $
# 
# **Para un exoplaneta en tránsito, 0 < b < 1.**

# In[2]:


class Exoplaneta:
    def __init__(self, estrella_anfritiona, Masa_planetaria, radius, a, inclinacion_orbita, excentricidad):
        self.estrella_anfritiona = estrella_anfritiona
        self.Masa_planetaria = Masa_planetaria
        self.radius = radius
        self.a = a
        self.inclinacion_orbita = inclinacion_orbita
        self.excentricidad = excentricidad
      
    def parametro_impact_exploplaneta (a, w, R):
        b = a * cos(i)* ((1 - (np.e**2))/(R*(1 + e*(np.sin(w)))))
        return b
    def Density (Radios, Mass):
        Densidad = []
        volumen = []
        for radio, T_mass in zip(Radios, Mass):
            Volumen = ((radio**3) * np.pi)*(4/3)
            volumen.append(Volumen)
        for masa, vol in zip(volumen, Mass):
            Den = (masa/vol)
            Densidad.append(Den)
        return Densidad
   

