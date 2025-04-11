# Trabajo con fechas y horas

import  datetime

fecha_hora_actual = datetime.datetime.now()
print("Fecha y hora actual: ", fecha_hora_actual)

#Formatear fechas y horas
formato = "%d/%m/%Y %H:%M:%S"
fecha_formato = fecha_hora_actual.strftime(formato)
print("Fecha y hora actual: ", fecha_formato)

#Fecha Especifica
fecha_especifica = datetime.datetime(2023, 12, 31, 23, 59, 59)
print("Fecha Especifica: ", fecha_especifica.strftime(formato))

#Calculo de fechas
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=23)
diff_days = tomorrow - today
yesterday = today - datetime.timedelta(days=1)
print("Hoy: ", today)
print("Mañana: ", tomorrow)
print("Ayer: ", yesterday)
print("Diferencia de dias: ", diff_days)

#Zonas horarias
import pytz
zona_horaria = pytz.timezone('America/New_York')
fecha_hora_actual = datetime.datetime.now(zona_horaria)
print("Fecha y hora actual en New York: ", fecha_hora_actual.strftime(formato))

#Convertir string a fecha
fecha_string = "2023-12-31 18:30:00"
fecha_objeto = datetime.datetime.strptime(fecha_string, "%Y-%m-%d %H:%M:%S")
print("Fecha de String a fecha: ", fecha_objeto.strftime(formato))
print(type(fecha_objeto))
