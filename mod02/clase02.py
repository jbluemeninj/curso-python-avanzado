"""
PROGRAMA PARA GUARDAR DATOS DE MI PC
"""
import platform,socket
from pathlib import Path

FILE_PATH =  Path("pc.txt")
def guardar_pc_info():

    pc_data = "=== INFO PC ===" + "\n"
    pc_data += "SO : " + platform.system() + "\n"
    pc_data += "VERSION : " + platform.release() + "\n"
    pc_data += "VERSION : " + platform.version() + "\n"
    pc_data += "ARQUITECTURA : " + platform.machine() + "\n"
    pc_data += "NOMBRE : " + socket.gethostname() + "\n"
    pc_data += "IP : " + socket.gethostbyname(socket.gethostname()) + "\n"
    pc_data += "=== FIN INFO PC ===" + "\n"

    with open(FILE_PATH,"w") as pc_file:
        pc_file.write(pc_data)

    print("Se guardo con exito!!!")

def leer_pc_info():
    try:

        with open(FILE_PATH, "r") as pc_file:
            pc_data = pc_file.read()
            print(pc_data)
    except:
        print("No se encontro el archivo")

if __name__ == "__main__":
    #guardar_pc_info()
    leer_pc_info()
