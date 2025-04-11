#Expresiones regulares

import re

cadena = "Vamos a aprender expresiones regulares con Python"

busqueda = re.search("aprender", cadena)
print(busqueda)

#Busqueda en base a un patron
texto = "La fecha de vencimiento es 2023-12-31 y la fecha de inicio fue 2023-01-15"
patron = r"\d{4}-\d{2}-\d{2}"
fechas = re.findall(patron, texto)
print(fechas)

#Reemplazar de texto basado en un patron
texto = "El telefono es 213-323-5435"
patron = r"\d{3}-\d{3}-\d{4}"
texto_modificado = re.sub(patron, "####", texto)
print(texto_modificado)

#Extraccion de urls de un html
html = '<p> Enlace uno <a href="http://www.gooogle.com">Enlace 1</a>'
patron_url = r'<a href="(.*?)">(.*?)</a>'
urls = re.findall(patron_url, html)
for url in urls:
    url, texto  = url
    print(f"URL: {url}, Texto: {texto}")

