def calcular_area_cuadrado(lado: float) -> float:
    """Calcula el área de un cuadrado dado el lado."""
    area = lado * lado
    return area


# Calcula el área de un pentágono regular dado el lado
def calcular_area_pentagono(lado: float) -> float:
    apotema = (lado / (2 * math.tan(math.pi / 5)))  # Apotema de un pentágono regular
    perimetro = 5 * lado
    area = (perimetro * apotema) / 2
    return area


# Calcula el área de un hexagono regular dado el lado.
def calcular_area_hexagono(lado: float) -> float:
    area = ((3 * math.sqrt(3)) / 2) * (lado ** 2)
    return area


# verfica si el numero es valido y lo transforma de una variabale de texto a numero
def es_numero_valido(input_string: str) -> bool:
    try:
        numero = float(input_string)
        return numero > 0
    except ValueError:
        return False


# Este codigo pertenece al menu de opciones
def mostrar_menu():
    print("\nSeleccione la figura para calcular su área:")
    print("1. Cuadrado")
    print("2. Pentágono")
    print("3. Hexágono")
    print("4. Salir")


def main():
    print("Calculadora del área de diferentes figuras geométricas.")

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")  # Ingreso del un numero valido entre las opciones

        if opcion == '1':
            lado_input = input("Ingrese la longitud del lado del cuadrado: ")  # Ingreso de la longitud
            if es_numero_valido(lado_input):  # si el numero es valido pasa a esta decicion y hace los calculos
                lado = float(lado_input)
                area = calcular_area_cuadrado(lado)
                print(f"El área del cuadrado con lado {lado} es: {area:.2f}")  # el resultado del area de cuadrado
            else:
                print(
                    "Entrada no válida. Por favor, ingrese un número positivo.")  # si el numero no es valido pasa
                # a esta opcion

        elif opcion == '2':  # opcion 2
            lado_input = input("Ingrese la longitud del lado del pentágono: ")  # Ingreso de la longitud
            if es_numero_valido(lado_input):  # si el numero es valido pasa a esta decicion y hace los calculos
                lado = float(lado_input)
                area = calcular_area_pentagono(lado)
                print(f"El área del pentágono con lado {lado} es: {area:.2f}")  # el resultado del area de pentagono
            else:
                print("Entrada no válida. Por favor, ingrese un número positivo.")  # si el numero no es valido pasa
                # a esta opcion

        elif opcion == '3':  # opcion 3
            lado_input = input("Ingrese la longitud del lado del hexágono: ")  # Ingreso de la longitud
            if es_numero_valido(lado_input):  # si el numero es valido pasa a esta decicion y hace los calculos
                lado = float(lado_input)
                area = calcular_area_hexagono(lado)
                print(f"El área del hexágo). ¡Adiós!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
