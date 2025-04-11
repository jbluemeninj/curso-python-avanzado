import decimal

from mod04.clase01 import division

num1 = decimal.Decimal(input("Enter the first number: "))
num2 = decimal.Decimal(input("Enter the second number: "))
print("Suma: ", num1 + num2)
print("Resta: ", num1 - num2)
print("Multiplicacion: ", num1 * num2)
div = num1 / num2

# Redondeo
redondeo_2 = div.quantize(decimal.Decimal('0.00'))
print(" redondeo: ", redondeo_2)

redondeo_alza =  div.quantize(decimal.Decimal('1.00'), rounding=decimal.ROUND_CEILING)
redondeo_baja =  div.quantize(decimal.Decimal('1.00'), rounding=decimal.ROUND_FLOOR)
redondeo_cercano =   div.quantize(decimal.Decimal('1.00'), rounding=decimal.ROUND_HALF_EVEN)
print(" redondeo hacia arriba: ", redondeo_alza)
print(" redondeo hacia abajo: ", redondeo_baja)
print(" redondeo mas cercano: ", redondeo_cercano)