# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 15:06:41 2018

@author: LUISFERNANDO
"""

import csv
url = open('Libro2.csv')
entrada = csv.reader(url)
reg = next(entrada)
print(reg)
codigo, descripcion = next(entrada)
print((codigo, descripcion))




with open('Libro2.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
        print(', '.join(row))
        print(row)
        
""""      
csvarchivo = open('datos.csv')  # Abrir archivo csv
entrada = csv.reader(csvarchivo)  # Leer todos los registros
reg = next(entrada)  # Leer registro (lista)
print(reg)  # Mostrar registro
nombre, provincia, consumo = next(entrada)  # Leer campos
print(nombre, provincia, consumo)  # Mostrar campos
del nombre, provincia, consumo, entrada  # Borrar objetos
csvarchivo.close()  # Cerrar archivo
del csvarchivo  # Borrar objeto

"""