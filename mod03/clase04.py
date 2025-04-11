#Formateo de cadenas

name =  "Juan"
age = 30
print("Mi nombre es %s y tengo %d años" % (name, age))
print("Mi nombre es {} y tengo {} años".format(name, age+10))

sql_insert = "INSERT INTO usuarios (nombre, edad) VALUES ('{}', '{}')".format(name, age)

print("Nombre : {1} , Edad : {0}".format(age, name))


#print con parametros
producto = "Computadora"
precio = 1000

print("Producto: {prod}, Precio: {pre:.2f}".format(prod = producto, pre = precio))

#Formaterar numeros

numero = 1234567890.123456
print("{:.2f}".format(numero))
print("{:,}".format(numero))
print("{:e}".format(numero))

#Formatear fechas
from datetime import datetime
now = datetime.now()
print("Fecha y Hora: {:%d/%m/%Y %H:%M:%S}".format(now))

#Alineacion y relleno
number = 42
print("Numero: {:>10}".format(number))
print("Numero: {:0<5}".format(number))