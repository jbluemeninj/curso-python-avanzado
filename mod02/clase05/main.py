from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def get_image(image_file):
    try:
        image = Image.open(image_file)
        print(image.size)
        print(image.format)
        print(image.mode)
        #image.show()
        #image_blackwhite = image.convert("L")
        #mage_blackwhite.show()
        #image_blackwhite.save("fondo_01_bw.jpg")
        font = ImageFont.truetype("Roboto/Roboto-Italic-VariableFont_wdth,wght.ttf", 120)
        draw = ImageDraw.Draw(image)
        draw.text((100, 100), "Hola Mundo", (255, 255, 255), font=font)

        #image.show()
        #image.save("fondo_01_text.jpg")

        #Creacion thumbnail
        image.thumbnail((200, 200))
        image.save("fondo_01_thumbnail.jpg")
        image.show()

    except FileNotFoundError:
        print(f"Error: Image file '{image_file}' not found.")

if __name__ == "__main__":
    get_image("fondo_01.jpg")