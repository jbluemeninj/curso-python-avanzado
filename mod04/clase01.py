import math

#Constante matematicas

PI = math.pi
E = math.e # Numero de euler
TAU = math.tau #
INF = math.inf #
NAN = math.nan
print(PI)

#Funciones trigonometricas

angulo = math.radians(45)
print(math.sin(angulo))
print(math.cos(angulo))
print(math.tan(angulo))

#Funciones exponenciales
print("Exponencial (e °2) : ", math.exp(2))
print("Logaritmo natural (e °2) : ", math.log(2))
print("Logaritmo base 10 (e °2): ", math.log10(2))
print("Potencia (2 °2) : ", math.pow(2,2))
print("Raiz cuadrada (2 °2) : ", math.sqrt(2))
print("Factorial (2 °2) : ", math.factorial(2))
print("Combinacion (2 °2) : ", math.comb(2, 2))
print("Permutacion (2 °2) : ", math.perm(2, 2))
print("Valor absoluto (2 °2) : ", math.fabs(2))

# Trabajar con fracciones
from fractions import Fraction

frac1 = Fraction(1, 2)
frac2 = Fraction(1, 3)

suma = frac1 + frac2
resta = frac1 - frac2
multiplicacion = frac1 * frac2
division = frac1 / frac2
print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicacion: ", multiplicacion)
print("Division: ", division)
print("Valor real: ", float(suma))

from decimal  import Decimal,  getcontext
num1 = Decimal('0.00000001')
num2 = Decimal('0.2')
print("Suma: ", num1 + num2)
print("Resta: ", num1 - num2)
print("Multiplicacion: ", num1 * num2)
print("Division: ", num1 / num2)
print("Valor real: ", float(num1 + num2))
getcontext().prec = 3
print("Suma: ", num1 + num2)

