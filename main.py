import pandas as pd
import math
import matplotlib.pyplot as plt

print("-----------------------------------")
print("Calculadora de Medidas de Tendencia Central y de Dispersión") 
print("-----------------------------------")

nombre_variable = input("Ingrese el nombre de la variable a evaluar: ")

n = int(input("Ingrese la cantidad de datos que desea ingresar: "))

datos = []

for i in range(n):
    dato = float(input(f"Ingrese el dato {i+1}: "))
    datos.append(dato)

df = pd.DataFrame({nombre_variable: datos})

