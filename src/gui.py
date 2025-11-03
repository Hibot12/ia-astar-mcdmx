import tkinter as tk
from tkinter import ttk


class MetroGUI(tk.Tk):
    def __init__(self):
        # Inicializamos la ventana de Tkinter.
        super().__init__()
        # Configuramos el título de la aplicación.
        self.title("Metro México Aplicación")
        # Establecemos las dimensiones de la ventana principal.
        self.geometry("1024x1024")

        # Etiquetas para solicitar las estaciones de origen y destino.
        self.estacion_orig_label = ttk.Label(
            self, text="Introduzca la estación de origen:"
        )
        self.estacion_orig_label.pack(pady=10)
        self.estacion_dest_label = ttk.Label(
            self, text="Introduzca la estación de destino:"
        )
        self.estacion_dest_label.pack(pady=10)

        # Campos de texto para capturar origen y destino.
        self.entry_origen = ttk.Entry(self, width=30)
        self.entry_origen.pack(pady=5)

        self.entry_destino = ttk.Entry(self, width=30)
        self.entry_destino.pack(pady=5)

        # Botón que activa la búsqueda cuando el usuario hace clic.
        self.boton = ttk.Button(
            self, text="Buscar la ruta", command=self.mostrar_inputs
        )
        self.boton.pack(pady=10)

        # Etiquetas donde mostraremos los resultados de la búsqueda.
        self.output_estacion_orig = ttk.Label(self, text="")
        self.output_estacion_orig.pack(pady=5)
        self.output_estacion_dest = ttk.Label(self, text="")
        self.output_estacion_dest.pack(pady=5)

    def mostrar_inputs(self):
        # Función de callback que lee las entradas y actualiza la salida.
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()

        # Refrescamos los textos con los valores proporcionados por el usuario.
        self.output_estacion_orig.config(text=f"Origen: {origen}")
        self.output_estacion_dest.config(text=f"Destino: {destino}")
