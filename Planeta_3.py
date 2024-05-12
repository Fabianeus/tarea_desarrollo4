#!/usr/bin/env python
# coding: utf-8

# In[2]:


import astropy as astropy
import math
import pandas as pd
import numpy as np
from astropy.constants import G


# # Planeta
# 
# Un planeta es un cuerpo con masa menor que 13 M_jup (masas de Júpiter) que
# orbita una estrella. Los atributos principales de un planeta son:
# 
# • Su estrella anfitriona (protegido).
# 
# • Masa planetaria (protegido, tipo flotante).
# 
# • Su radio (protegido, tipo flotante).
# 
# • Sus elementos orbitales: radio semi mayor de la  ́orbita, a, inclinación de la
#  ́orbita i, excentricidad de la  ́orbita e, y argumento del periastron ω (todos
# protegidos y tipo flotante).
# Para esta clase, se espera que se codifique una función pública que calcule y
# devuelva el período de rotación kepleriana (retorno de tipo flotante),
# 
# $\sqrt{\frac{a^3}{G \cdot M}}$

# In[3]:


class Planetas:
    def __init__(self, estrella_anfritiona, Masa_planetaria, Radius, a, inclinacion_orbita, excentricidad, periastron):
        self.estrella_anfritiona = estrella_anfritiona
        self.Masa_planetaria = Masa_planetaria
        self.Radius = Radius
        self.a = a
        self.inclinacion_orbita = inclinacion_orbita
        self.excentricidad = excentricidad
        self.periastron = periastron
    
    def T_kepleriana (self, G):
        Periodo = 2*np.pi*(((self.a**3)/(G*self.estrella_anfritiona.mass))**(1/2))
        return Periodo

