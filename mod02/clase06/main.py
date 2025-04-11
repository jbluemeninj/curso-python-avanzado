#Comprensor de Imagenes
from pickletools import optimize

from PIL import Image
import os

def compress_image(images_folder):
    try:
        for file in os.listdir(images_folder):
            file_name, file_extension = os.path.splitext(images_folder + file)
            print("Comprimiendo archivos..." + file_name + file_extension)

            if file_extension == ".jpg":
                file_compress = Image.open(images_folder + file)
                file_compress.save(file_name + "_comprimido.jpg",
                        optimize=True,
                        quality=70)

    except  Exception as e:
        print("Error al comprimir las imagenes: " + str(e))


if __name__ == "__main__":
    images_folder = "D:/cursos/curso_python_avanzado/mod02/clase06/images/"
    compress_image(images_folder)


