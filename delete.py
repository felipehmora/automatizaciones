import os
import shutil

def eliminar_archivos(carpeta1, carpeta2):
    # Eliminar archivos en carpeta1
    if os.path.exists(carpeta1):
        for archivo in os.listdir(carpeta1):
            archivo_path = os.path.join(carpeta1, archivo)
            try:
                if os.path.isfile(archivo_path) or os.path.islink(archivo_path):
                    os.unlink(archivo_path)  # Eliminar archivos o enlaces simbólicos
                elif os.path.isdir(archivo_path):
                    shutil.rmtree(archivo_path)  # Eliminar directorios y su contenido
            except Exception as e:
                print(f'Error al eliminar {archivo_path}. Razón: {e}')
    
    # Eliminar archivos en carpeta2
    if os.path.exists(carpeta2):
        for archivo in os.listdir(carpeta2):
            archivo_path = os.path.join(carpeta2, archivo)
            try:
                if os.path.isfile(archivo_path) or os.path.islink(archivo_path):
                    os.unlink(archivo_path)
                elif os.path.isdir(archivo_path):
                    shutil.rmtree(archivo_path)
            except Exception as e:
                print(f'Error al eliminar {archivo_path}. Razón: {e}')

    print("Archivos eliminados de ambas carpetas.")

# Ejemplo de uso
carpeta1 = 'images'
carpeta2 = 'imagenes-comprimidas'

eliminar_archivos(carpeta1, carpeta2)
