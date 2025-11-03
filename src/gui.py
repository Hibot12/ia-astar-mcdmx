import tkinter as tk
from tkinter import ttk

class MetroGUI(tk.Tk):
    def __init__(self):
        #inicializamos la ventana de tkinter
        super().__init__()
        #titulo del la GUI de la applicacion
        self.title("Metro Mexico Applicacion")
        #tamaño del GUI
        self.geometry("1024x1024")

        #etiquetas para pedir las estaciones
        self.estacion_orig_label = ttk.Label(self, text="introduzca la estacion de Origen:")
        self.estacion_orig_label.pack(pady=10)
        self.estacion_dest_label = ttk.Label(self, text="introduzca la estacion de Destino:")
        self.estacion_orig_label.pack(pady=10)

        #Esto son las entradas de texto(uno para origen y otro para el destino)
        self.entry_origen = ttk.Entry(self, width=30)
        self.entry_origen.pack(pady=5)

        self.entry_destino = ttk.Entry(self, width=30)
        self.entry_destino.pack(pady=5)

        #Esto es el boton para demostrar lo que el usuario esta escribiendo
        self.boton = ttk.Button(self, text="Buscar la ruta", command=self.mostrar_inputs)
        self.boton.pack(pady=10)

        #Esto son las etiquetas para mostrar los resultados de la ruta
        self.output_estacion_orig = ttk.Label(self, text="")
        self.output_estacion_orig.pack(pady=5)
        self.output_estacion_dest = ttk.Label(self, text="")
        self.output_estacion_dest.pack(pady=5)
    
    def mostrar_inputs(self):
        #esto es la funcion que funciona cuando el usuario pulsa el boton
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()

        #
        self.output_estacion_orig.config(text=f"Origen: {origen}")
        self.output_estacion_dest.config(text=f"Destino: {destino}")

if __name__ == "__main__":
    app = MetroGUI()
    app.mainloop()
