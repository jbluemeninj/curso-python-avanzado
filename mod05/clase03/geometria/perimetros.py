#PERIMETROS

def perimetro_cuadrado(lado):
    return lado * 4

def perimetro_rectangulo(base, altura):
    return base * 2 + altura * 2

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def perimetro_circulo(radio):
    return 2 * 3.1416 * radio

def perimetro_rombo(lado):
    return lado * 4

def perimetro_trapecio(base_mayor, base_menor, lado1, lado2):
    return base_mayor + base_menor + lado1 + lado2

def perimetro_poligono_regular(lado, num_lados):
    return lado * num_lados

def perimetro_paralelogramo(base, altura):
    return base * 2 + altura * 2

def perimetro_cometa(lado1, lado2, lado3, lado4):
    return lado1 + lado2 + lado3 + lado4

def perimetro_octogono(lado):
    return lado * 8

def perimetro_decagono(lado):
    return lado * 10

def perimetro_ellipses(mayor, menor):
    return 2 * 3.1416 * (3 * (mayor + menor) - (mayor - menor) ** 2 ** 0.5)