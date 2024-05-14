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
media_manual = sum(datos) / n
mediana = df[nombre_variable].median()
mediana_manual = sorted(datos)[n//2] if n % 2 != 0 else (sorted(datos)[n//2 - 1] + sorted(datos)[n//2]) / 2
moda = df[nombre_variable].mode()[0]
moda_manual = max(set(datos), key = datos.count)

maximo = df[nombre_variable].max()
minimo = df[nombre_variable].min()

rango = round(maximo - minimo, 2)

varianza = round(df[nombre_variable].var(), 2)
desviacion_estandar = round(math.sqrt(varianza), 2)

print("-----------------------------------")
print("Resultados con Métodos de Pandas")
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