import os
import subprocess


def mostrar_codigo_y_ejecutar(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")  # Imprime el codigo de la ruta seleccionada
            print(archivo.read())  # lee el archivo y lo imprime

        print(f"\n--- Ejecutando {ruta_script} ---\n")
        resultado = subprocess.run(['python', ruta_script_absoluta], capture_output=True, text=True)
        print(resultado.stdout)
        if resultado.stderr:
            print("Errores:", resultado.stderr)
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'PARCIAL 1/SO.py',
        '2': 'PARCIAL 1/tarea1.py',
        '3': 'PARCIAL 1/POO.py',
        '4': 'PARCIAL 1/Programacion Tradicional.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo_y_ejecutar(ruta_script)
        else:
            print("Opción no válida. Por favor, vuelve a intentarlo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
