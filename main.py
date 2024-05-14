import pandas as pd
import math

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

media = df[nombre_variable].mean()
mediana = df[nombre_variable].median()
moda = df[nombre_variable].mode()[0]

maximo = df[nombre_variable].max()
minimo = df[nombre_variable].min()

rango = round(maximo - minimo, 2)

varianza = df[nombre_variable].var()
desviacion_estandar = math.sqrt(varianza)

print("-----------------------------------")
print("Medidas de Tendencia Central")
print("-----------------------------------")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print("-----------------------------------")
print("Medidas de Dispersión")
print("-----------------------------------")
print(f"Rango: {rango}")
print(f"Varianza: {varianza}")
print(f"Desviación Estándar: {desviacion_estandar}")
print("-----------------------------------")