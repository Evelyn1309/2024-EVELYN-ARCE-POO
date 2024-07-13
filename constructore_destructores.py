# Creacion de una computadora utilizando constructores y destructores con pyton
class Componente:
    def __init__(self, nombre):
        # Este  es un constructor de la clase Componente.
        self.nombre = nombre
        print(f"Se ha creado el componente {self.nombre}")

    def __del__(self):
        # Destructor de la clase Componente.
        print(f"El componente {self.nombre} ha sido eliminado.")  # imprime de que el objeto a sido eliminado


class CPU(Componente):
    def __init__(self, nombre, velocidad):  # Construimos el CPU
        super().__init__(nombre)
        self.velocidad = velocidad
        print(f"CPU {self.nombre} inicializada a {self.velocidad} GHz")  # El CPU aqui se ha inicializadizado

    def procesar(self):
        #  Simulacion del  procesamiento de la CPU.
        print(f"La CPU {self.nombre} está procesando datos.")

    def __del__(self):  # Destructor de la clase CPU.
        super().__del__()
        print(f"La CPU {self.nombre} ha sido desactivada.")


class Computadora:
    def __init__(self, nombre):  # Constructor de la clase Computadora.
        self.nombre = nombre
        self.cpu = CPU("Intel Core i3", 3.2)
        print(f"Se ha creado la computadora {self.nombre}")

    def encender(self):  # Método para simular el encendido de la computadora.

        print(f"Encendiendo la computadora {self.nombre}.")
        self.cpu.procesar()

    def apagar(self):  # Método para simular el apagado de la computadora.
        print(f"Apagando la computadora {self.nombre}.")

    def __del__(self):  # Destructor de la clase Computadora.
        self.apagar()
        del self.cpu
        print(f"La computadora {self.nombre} ha sido eliminada.")


# Ejecucion
if __name__ == "__main__":
    # Creamos la  computadora
    mi_pc = Computadora("Mi  Laptop")

    # Encendemos la computadora
    mi_pc.encender()

    # Al finalizar el proceso, la computadora se apaga automáticamente y se  elimina el objeto mi_pc
    del mi_pc
