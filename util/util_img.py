from PIL import ImageTk, Image

# Aca ira la funcionalidad para leer imagenes 

def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))

