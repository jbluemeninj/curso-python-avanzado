#Busqueda y reemplazar palabra en un texto
from itertools import count

texto = """Desde la grandeza de sus nevados, desafiantes e imponentes,
    los mejores jugadores de mundo estan en PERU, CHILE, VENEZUELA Y 
    ARGENTINA"""

palabra_buscada = input("Ingrese la palabra a buscar: ")
index = texto.find(palabra_buscada)
if index != -1:
    print(f"{palabra_buscada} no se encontro en el texto")
    print(f"{palabra_buscada} se encontro en el indice {index}")
    total_encontrados = texto.count(palabra_buscada)
    print(f"{palabra_buscada} se encontro {total_encontrados} veces")

    palabra_reemplazada = input("Ingrese la palabra a reemplazar: ")
    texto = texto.replace(palabra_buscada, palabra_reemplazada,2)
    print(texto)
else :
    print(f"{palabra_buscada} no se encontro en el texto")