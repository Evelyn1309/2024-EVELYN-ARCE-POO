# Programa con programacion tradicional  de datos diarios de
# temperaturas que permita   cálcular el promedio semanal.
def ingrese_temp():  # funcion para ingresar las temperaturas
    temperaturas = []
    for dia in range(7):  # definicion de el rango de dias
        temperatura = float(
            input(f"Ingresar la temperatura de este día {dia + 1} :    "))  # ingreso de las temperaturas de los dias
        temperaturas.append(temperatura)
    return temperaturas


def prom(temperaturas): # funcion para obtener el promedio
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio


temperaturas = ingrese_temp()
promedio = prom(temperaturas)

print(f"El promedio de esta seman en  el clima es: {promedio} ª") # resultado del promedio
