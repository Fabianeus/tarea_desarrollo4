#!/usr/bin/env python
# coding: utf-8

# In[2]:


import astropy as astropy
import math
import pandas as pd
import numpy as np
from astropy.constants import G


# ## Estrella
# 
# Los atributos principales de una estrella son:
# 
# • Su nombre (por ejemplo, Sirio) (publico).
# 
# • Masa M (protegido).
# 
# • Radio R∗ (protegido).
# 
# • Temperatura superficial Teff (protegido).
# 
# • Distancia d (protegido).
# 
# • Movimiento Propio ∆ (vector de dos dimensiones para la velocidad proyectada en el cielo) 
# (protegido).
# 
# **Se espera que codifique las siguientes funciones para esta clase:**
# 
# • Una función pública (con retorno de tipo flotante) que calcule la 
#   luminosidad total L = 4π*R^2 * Teff.
# 
# • Una función pública (con retorno de tipo flotante) que calcule la 
#   luminosidad de la secuencia principal Lms = LSun · (M/Msun)^3.5
# 
# 
# 
# .
# 
# Utilice las siguientes constantes: L_Sun = 3.828 × 1026 W y M_Sun = 1.9884 ×
# 1030 kg. También puede buscar las constantes en scipy o astropy si así lo desea.

# In[3]:


#Ahora creamos las clases 

#Definimos algunas constanes 
M_sun = 1.9884 * (10**30)
L_sun = 3.828 * (10**26)
G #Constante de gravitacion universal 

class estrellas:
    def __init__(self, name, mass, radius, Temp_superf_Teff, Distancia_d, Mov_indep):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.Temp_superf_Teff = Temp_superf_Teff
        self.Distancia_d = Distancia_d
        self.Mov_indep = Mov_indep
    
    def luminosidad (self):
        L = 4 * np.pi * (self.radius**2) * self.Temp_superf_Teff
        return L #Luminosidad de la estrella, el cual retorna con la variable L
    
    def Lumin_Secuencia (self):
        L_ms  = L_sun * ((self.mass/M_sun)**(3.5))
        return L_ms #Su secuencia principal
    #Gravedad planetaria
    

    def planet_gravity (Masa, Radio):
      Gravity_constant = 6.6743e-11
      Grav_planet = []
    
      for m, rad in zip(Masa, Radio):
          gr = (Gravity_constant * m)/(rad**2)
          Grav_planet.append(gr)
      return Grav_planet

