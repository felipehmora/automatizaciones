from PIL import Image
import os

# Ruta de la carpeta con las imágenes
input_folder = 'images'
output_folder = 'imagenes-comprimidas'

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Tamaño de redimensionamiento (ancho, alto)
new_size = (800, 800)

# Definir la calidad de compresión (1-100, 100 es la mejor calidad)
quality = 80

# Extensiones de archivos que consideraremos imágenes
valid_extensions = ('.jpg', '.jpeg', '.png', '.HEIC')

# Recorrer todos los archivos en la carpeta
for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):
        # Abrir la imagen
        image_path = os.path.join(input_folder, filename)
        with Image.open(image_path) as img:
            # Redimensionar la imagen
            img_resized = img.resize(new_size)

            # Cambiar el formato a WebP y guardar en la carpeta de salida
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_folder, output_filename)
            img_resized.save(output_path, 'webp', quality=quality)
            print(f'Imagen {filename} redimensionada y convertida a {output_filename}')