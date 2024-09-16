# Desarrollar una aplicación de interfaz gráfica de usuario (GUI) que permita a los usuarios interactuar con datos de
# manera visual, utilizando los conceptos aprendidos sobre GUI.
import tkinter as tk  # Importa la librería Tkinter para crear la GUI
from tkinter import messagebox  # Importa el módulo para mostrar mensajes emergentes


# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada_texto.get()  # Obtencion del  texto ingresado por el usuario
    if dato:  # Verifica si el campo de texto no está vacío
        lista_datos.insert(tk.END, dato)  # Agrega el dato al final de la lista
        entrada_texto.delete(0, tk.END)  # Borra el contenido del campo de texto
    else:
        # Muestra cada una advertencia si el campo de texto está vacío
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")


# Función que limpiar todos los datos
def limpiar_lista():
    lista_datos.delete(0, tk.END)  # Elimina elementos de la lista


# Crear la ventana principal
ventana = tk.Tk()  # Crea  la ventana
ventana.title(" Gestión de Datos")  # Define el título de la ventana

# Etiqueta para el campo de texto
etiqueta = tk.Label(ventana, text="Ingresar información:",  background='#00BFFF')  # Crea etiqueta descriptiva
etiqueta.pack()  # Coloca la etiqueta en la ventana

# Campo de texto
entrada_texto = tk.Entry(ventana, width=40,
                         background='#7c1324')  # Crea el campo de texto donde el usuario puede ingresar información
entrada_texto.pack()  # Coloca el campo de texto en la ventana

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar",
                          command=agregar_dato)  # Crea el botón "Agregar" y asocia la función 'agregar_dato' al clic
boton_agregar.pack()  # Coloca el botón en la ventana

# Lista para mostrar los datos agregados
lista_datos = tk.Listbox(ventana, width=50, height=10, background='#81F7F3')  # Crea una lista para mostrar los datos
# con tamaño especificado
lista_datos.pack()  # Coloca la lista en la ventana

# Botón para limpiar la lista de datos
boton_limpiar = tk.Button(ventana, text="Limpiar",
                          command=limpiar_lista)  # Crea el botón "Limpiar" y asocia la función 'limpiar_lista' al clic
boton_limpiar.pack()  # Coloca el botón en la ventana

# Iniciar el loop principal de la ventana
ventana.mainloop()  # Inicia el bucle principal que mantiene la ventana abierta y espera interacciones
