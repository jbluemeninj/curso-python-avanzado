import datetime

def dia_naciemiento(fecha_nacimiento):
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    index_dia = fecha_nacimiento.weekday()
    return dias[index_dia]

if  __name__ == "__main__":
    fecha_sttring = input("Ingrese su fecha de nacimiento en formato YYYY-MM-DD: ")
    fecha_objeto = datetime.datetime.strptime(fecha_sttring, "%Y-%m-%d")
    dia = dia_naciemiento(fecha_objeto)
    print(f"El dia de nacimiento es: {dia}")
