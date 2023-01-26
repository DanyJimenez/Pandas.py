import pandas as pd

fuenteDatos = pd.read_csv("./empleados.csv")
filtroHead = fuenteDatos.head() #primeros 5
print(filtroHead)

print("\n")

filtrar5ultimos = fuenteDatos.tail(5)
print(filtrar5ultimos)

print("\n")

#empleados menores a 23 años (condicionales)
condiciones = fuenteDatos[fuenteDatos["edad"] < 23]
print(condiciones)

print("\n")

nom_salario_edad = fuenteDatos.tail(5)[["nombres", "salario", "edad"]]
print(nom_salario_edad)

print("\n")

filt_5primeros = fuenteDatos.head(5)[["nombres", "salario"]]
print(filt_5primeros)

print("\n")

#promedio de los 5 primeros salarios
promedios = fuenteDatos.head(5)[["salario"]].mean()
print(promedios)

print("\n")

#Calcular la moda 
moda_Edad = fuenteDatos[["edad"]].mode()
print(moda_Edad)

print("\n")

#promedio o media aritmética de los 500 usuarios
media_edad = fuenteDatos[["edad"]].mean()
print(media_edad)

print("\n")

#Datos seleccionados por filas 2, 22, 99 con su respectivo promedio
datosxfilas = fuenteDatos[[ "edad"]].iloc[[2, 22, 99, 77, 490]].mean()
print(datosxfilas)

print("\n")


porc_deducc = fuenteDatos[fuenteDatos["porcentajeDeduccion"] < 1]
print(porc_deducc)

print("\n")

#Número de veces que se repite cada edad
num_veces = fuenteDatos["edad"].value_counts()
print(num_veces)