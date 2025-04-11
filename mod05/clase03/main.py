from geometria import areas as ar
from geometria import perimetros
from geometria.perimetros import (perimetro_rombo,
                                  perimetro_circulo,
                                  perimetro_rectangulo)

area = ar.area_cuadrado(4)
perimetro = perimetros.perimetro_cuadrado(4)
perimetro_rombo = perimetro_rombo(4)
perimetro_circulo = perimetro_circulo(4)
perimetro_rectangulo = perimetro_rectangulo(4, 2)

print(f"El area del cuadrado es: {area}")
print(f"El perimetro del cuadrado es: {perimetro}")
print(f"El perimetro del rombo es: {perimetro_rombo}")
print(f"El perimetro del circulo es: {perimetro_circulo}")
print(f"El perimetro del rectangulo es: {perimetro_rectangulo}")