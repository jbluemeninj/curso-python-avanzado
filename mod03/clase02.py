cadena1 = "Mi edad es "
cadena2  = 25
resultado = cadena1  + str(cadena2)
#print(type(resultado))
#print(resultado.upper())

#nombre = input("Ingrese su nombre: ")
#apellido = input("Ingrese su apellido: ")
#edad = int(input("Ingrese su edad: "))
#print("Hola " + nombre + " " + apellido)


#f-string
#print(f"Hola {nombre} {apellido}, tu edad es {edad}")

#concatenar listas
numeros = [1,2,3,4,5]
resultado = ""

for num in numeros:
    resultado += str(num) + " "
print(resultado)

#Concatenacion join
palabras = ["Hola", "Mundo", "Python"]
frase = " ".join(palabras)
print(frase)