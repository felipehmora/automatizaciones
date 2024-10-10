# Compresor de Imágenes Python

Este script de Python redimensiona y comprime imágenes en una carpeta específica, convirtiéndolas al formato WebP.

## Características

- Redimensiona imágenes a un tamaño específico (por defecto 800x800 píxeles)
- Comprime imágenes con una calidad ajustable
- Convierte imágenes a formato WebP
- Procesa múltiples formatos de imagen (jpg, jpeg, png, HEIC)

## Requisitos

- Python 3.x
- Pillow (PIL Fork)

Para instalar Pillow, ejecuta:

```
pip install Pillow
```

## Uso

1. Coloca tus imágenes en una carpeta llamada `images` en el mismo directorio que el script.

2. Ejecuta el script:

```
python compresor_imagenes.py
```

3. Las imágenes procesadas se guardarán en una nueva carpeta llamada `imagenes-comprimidas`.

## Configuración

Puedes ajustar las siguientes variables en el script según tus necesidades:

- `input_folder`: Carpeta de entrada (por defecto 'images')
- `output_folder`: Carpeta de salida (por defecto 'imagenes-comprimidas')
- `new_size`: Tamaño de redimensionamiento (por defecto (800, 800))
- `quality`: Calidad de compresión (por defecto 80, rango 1-100)

## Notas

- El script mantendrá la relación de aspecto original de las imágenes al redimensionarlas.
- Las imágenes de salida estarán en formato WebP, que ofrece una buena compresión manteniendo la calidad.
- Los archivos originales no se modifican.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
