#!/usr/bin/env python
# coding: utf-8

# In[2]:


import astropy as astropy
import math
import pandas as pd
import numpy as np
from astropy.constants import G


# ## Sistema Planetario
# 
# Un sistema planetario es el conjunto de planetas que orbitan una estrella dada.
# El  ́único atributo público que tiene un sistema planetario es su lista de planetas.
# Se espera que se codifique las siguientes funciones para esta clase:
# 
# • Una función pública que devuelva el número de planetas en el sistema
# planetario (tipo entero).
# 
# • Una función pública que devuelva la lista de planetas ordenada según su
# radio semi mayor de la  ́orbita a (tipo lista).

# In[3]:


class Sistema_planetario:
    def __init__(self, estrella, Planeta, Masa):
        self.estrella = estrella 
        self.Planeta = Planeta
        self.Masa = Masa
    def Cantidad (Estrella):
        plantas_count = df['Mass'].notna().sum()
    
    def obtener_planetas_ordenados_por_a(self, sistema_planetas):
        return sorted(sistema_planetas, key=lambda planeta: planeta.a)

