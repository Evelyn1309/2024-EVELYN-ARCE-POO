# Programa con programacion Orientada a Objetos  de datos diarios de
# temperaturas que permita   cálcular el promedio semanal.
class Clima:
    def __init__(self):  # definicion del parametro
        self.tempe = []

    def ingrese_tempe(self):  # funcion para ingresar las temperaturas
        for Dia in range(7):  # definicion de el rango de dias
            temp = float(
                input(f"Ingrese la temperatura del día {Dia + 1}: "))  # ingreso de las temperaturas de lso dias
            self.tempe.append(temp)

    def prom(self): # funcion para obtener el promedio
        total = sum(self.tempe)
        promedio = total / len(self.tempe)
        return promedio


clima1 = Clima()
clima1.ingrese_tempe()
promedio = clima1.prom()
print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C") # resultado del promedio
