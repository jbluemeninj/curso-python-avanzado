import numpy as np

numeros = [1,2,3,4]
print(numeros)

#Usando numpy
np_numeros  = list(np.arange(1,10))
print(numeros)

#matrices
lista_matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(lista_matriz)
print(matriz)
print(type(matriz))
suma = matriz[0] + matriz[1]
print(suma)

#suma de un solo valor
suma_valor = matriz[0,0] + matriz[1,2]
print(suma_valor)

#Calculo Estadistico
data = np.array([12,15, 20,18, 25, 30,22,19])

#media
media = np.mean(data)
print("MEDIA: ", media)

#DESVIACION ESTANDAR
desviacion_estandar = np.std(data)
print("DESVIACION ESTANDAR: ", desviacion_estandar)

#Maximo y Minimos
max_val = np.max(data)
max_indice = np.argmax(data)
print("MAXIMO: ", max_val,  "INDICE: ", max_indice)
