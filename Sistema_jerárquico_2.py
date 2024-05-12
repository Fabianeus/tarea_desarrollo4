#!/usr/bin/env python
# coding: utf-8

# In[1]:


import astropy as astropy
import math
import pandas as pd
import numpy as np
from astropy.constants import G


# # Sistema Jerárquico
# 
# Un sistema jerárquico es un sistema estelar m ́ultiple compuesto por N ≥ 2
# estrellas. Los atributos principales del sistema estelar son:
# 
# • La lista de estrellas que contiene (tipo lista).
# Se espera que se codifique las siguientes funciones para esta clase:
# 
# • Una función p ́ublica que devuelva la lista de estrellas ordenada por masa
# estelar (tipo lista).
# 
# • Una función pública que imprima los nombres de las estrellas seguidos de
# la lista ordenada de letras del alfabeto (por ejemplo, SirioA, SirioB) (tipo
# cadena de texto).

# In[2]:


class sistema_Jerarquico:
    def __init__(self, Estrella):
        self.Estrella = Estrella
    
    def orden_estrella(self): #Estrellas ordenadas por su masa 
         return sorted(self.Estrella, key=lambda estrella: estrella.mass)
         
        
    def orden_alfabetico (self):
        Letras = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        Asignacion = [Estrellas.nombre for Estrellas in self.Estrella]
        for a, Asignacion in enumerate(As): #hacerlo luego
             print(f"{Asignacion}{Letras[a]}")
                
        #En teoria deberia entregarnos la lista de estrellas con una letra respectiva

