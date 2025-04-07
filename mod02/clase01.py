"""
PROGRAMA PARA GUARDAR DATOS DE MI PC
"""
import platform,socket

def guardar_pc_info():

    pc_data = "=== INFO PC ===" + "\n"
    pc_data += "SO : " + platform.system() + "\n"
    pc_data += "VERSION : " + platform.release() + "\n"
    pc_data += "VERSION : " + platform.version() + "\n"
    pc_data += "ARQUITECTURA : " + platform.machine() + "\n"
    pc_data += "NOMBRE : " + socket.gethostname() + "\n"
    pc_data += "IP : " + socket.gethostbyname(socket.gethostname()) + "\n"
    pc_data += "=== FIN INFO PC ===" + "\n"

    pc_file = open("pc.txt","w")
    pc_file.write(pc_data)
    pc_file.close()

    print("Se guardo con exito!!!")

def leer_pc_info():
    try:
        pc_file = open("pc.txt", "r")
        print(pc_file.read())
        pc_file.close()
    except:
        print("No se encontro el archivo")

if __name__ == "__main__":
    #guardar_pc_info()
    leer_pc_info()
