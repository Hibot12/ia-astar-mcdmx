import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw 

class MetroGUI(tk.Tk):
    def __init__(self):
        #inicializamos la ventana de tkinter
        super().__init__()
        #titulo del la GUI de la applicacion
        self.title("Metro Mexico Applicacion")
        #tamaño del GUI
        self.geometry("1024x1024")

        #Esto crea el contenedor principal con dos columnas left y right
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        #Esto es el fram izquierdo para los controles
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        #Frame derecho para el mapa del metro
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        #etiquetas para pedir las estaciones
        self.estacion_orig_label = ttk.Label(self, text="Introduzca la estacion de Origen:")
        self.estacion_orig_label.pack(pady=10)
        self.estacion_dest_label = ttk.Label(self, text="Introduzca la estacion de Destino:")
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


        #Esto es el frame para mostrar el resultado de la ruta
        result_frame = ttk.LabelFrame(left_frame, text="Informacion de la Ruta", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        #Un widget de texto para mostrar el recorrido completo
        self.result_text = tk.Text(result_frame, width=40, height=25, wrap=tk.WORD, font=("Cardo", 11))
        self.result_text.pack(fill=tk.BOTH, expand=True)

        # esto añade un scrollbar para el widget del texto de informacion de la ruta
        scrollbar = ttk.Scrollbar(result_frame, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        
        #esto crea el canvas para monstrar el mapa del metro
        self.canvas = tk.Canvas(right_frame, bg="White")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        #esto carga el mapa del metro:
        self.load_metro_map()

        #Esto son las coordenadas exactas con respecto a la imagen del metro
        # ------- NOOOO TOCAR !!!!!!!!!!!!! -------------
        self.coords_estacion = {
            "Tacubaya": (179, 305),
            "San Pedro de los Pinos": (178, 371),
            "San Antonio": (179, 411),
            "Mixcoac": (179, 464),
            "Barranca del Muerto": (179, 529),
            "Constituyentes": (179, 236),
            "Auditorio": (178, 165),
            "Polanco": (178, 90),
            "Observatorio": (136, 349),
            "Patriotismo": (269, 305),
            "Chilpancingo": (372, 305),
            "Lazaro Cardenas": (542, 305),  
            "Juanacatlan": (220, 263),  
            "Chapultepec": (257, 226),
            "Sevilla": (299, 185),
            "Insurgentes": (341, 151),
            "Cuauhtemoc": (386, 150), 
            "Balderas": (436, 151),
            "Juarez": (436, 78),  
            "Niños Héroes": (436, 187),  
            "Hospital General": (437, 230),
            "Centro Medico": (436, 304), 
            "Etiopia": (437, 345),  
            "Eugenia": (436, 382),
            "Division del Norte": (437, 422), 
            "Zapata": (436, 463),
            "Coyoacan": (437, 501),  
            "Viveros": (437, 542),
            "Miguel Ángel de Quevedo": (436, 580),  
            "Copilco": (437, 619),
            "Universidad": (437, 658),
            "Parque de los Venados": (535, 461),
            "Eje Central": (596, 553),
            "Insurgentes Sur": (250, 460),
            "Hospital 20 de Noviembre": (336, 463),
        }
        # ------- NOOOO TOCAR !!!!!!!!!!!!! -------------



    
    def load_metro_map(self):
        #este codigo mete el mapa del metro en el GUI
        try:
            self.original_image = Image.open("src/Metro.png")
            self.display_image()
        except Exception as e:
            self.result_text.insert(tk.END, f"Error cargando mapa: {e}\n")

    def display_image(self, path=None):
        #esta funcion muestra el mapa del metro con la ruta
        #si no tiene la imagen original return
        if not hasattr(self, 'original_image'):
            return
        
        #Creamos una copia de la imagen original
        img = self.original_image.copy()

        # Si hay una ruta, la dibujamos en el mapa
        if path and len(path) > 1:
            draw = ImageDraw.Draw(img)

            #dibujamos las lineas de la ruta
            for i in range(len(path)-1):
                estacion1 = path[i]
                estacion2 = path[i+1]

                if estacion1 in self.pathfinder.coords_estacion and estacion2 in self.pathfinder.coords_estacion:
                    x1, y1 = self.pathfinder.coords_estacion[estacion1]
                    x2, y2 = self.pathfinder.coords_estacion[estacion2]

                    #dibujamos la linea para la ruta
                    draw.line([(x1, y1), (x2, y2)], fill="red", width=8)
            
            #Dibujamos circulos en cada estacion de la ruta
            for estacion in path:
                if estacion in self.pathfinder.coords_estacion:
                    x, y = self.pathfinder.coords_estacion[estacion]
                    radio = 10

                    #Hacemos que la estacion de origen sea verde y la de destino sea azul
                    if estacion == path[0]:
                        #Verde
                        color = "00FF00"
                    if estacion == path[-1]:
                        #Azul
                        color == "0000FF"
                    else: 
                        #rojo
                        color == "FF0000"

                    draw.ellipse([x-radio, y-radio, x+radio, y+radio], 
                               fill=color, outline="white", width=2)
        
        #esto redimensiona la imagen para ajustar al canvas
        #obtenemos el ancho actual del canvas en pixeles
        canvas_width = self.canvas.winfo_width()
        #obtenemos la altura actual del canvas en pixeles
        canvas_height = self.canvas.winfo_height()

        #esto verifica que el canvas tiene dimensiones validas (que sea mayor que 1 pixel)
        if canvas_width > 1 and canvas_height > 1:
            #Calculamos la proporcion de aspecto de la imagen (ancho/alto)
            img_ratio = img.width / img.height
            #Calculamos la proporcion de aspecto del canvas
            canvas_ratio = canvas_width / canvas_height

            #Aqui determinamos como redimensionar la imagen manteniendo su proporsion
            if img_ratio > canvas_ratio:
                #si la imagen es mas ancha proporcionalmente, ajustamos por el ancho
                new_width = canvas_width
                new_height = int(canvas_width / img_ratio)
            else:
                #si la imagen es mas alto proporcionalmente, ajustamos por la altura
                new_height = canvas_height
                new_width = int(canvas_height * img_ratio)
            #redimensionamos la imagen a las nuevas dimensiones
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        #convertimos la imagen a una version que tkinter pueda mostrar
        self.photo = ImageTk.PhotoImage(img)
        #tambien borramos todo el contenido anterior del canvas
        self.canvas.delete("all")
        #Dibujamos la nueva imagen en el canvas en la posición (0, 0)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
    """    
    def mostrar_inputs(self):
        #esto es la funcion que funciona cuando el usuario pulsa el boton
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()

        #
        self.output_estacion_orig.config(text=f"Origen: {origen}")
        self.output_estacion_dest.config(text=f"Destino: {destino}")
    """

    def mostrar_inputs(self):
        """Esto es la funcion que funciona cuando el usuario pulsa el boton"""
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()

        #Actualizamos las etiquetas
        self.output_estacion_orig.config(text=f"Origen: {origen}")
        self.output_estacion_dest.config(text=f"Destino: {destino}")
        
        #limpiamos los resultados anteriores
        self.result_text.delete(1.0, tk.END)
        
        #Verificamos si el usuario ha introducido ambas estaciones la de origen y la de destino
        if not origen or not destino:
            self.result_text.insert(tk.END, "Por favor introduzca ambas estaciones.\n")
            self.display_image()
            return
        
        #Mensaje de error por si el usuario introduce la misma estacion para dest y origen
        if origen == destino:
            self.result_text.insert(tk.END, "El origen y destino son la misma estación.\n")
            self.display_image()
            return
        
        # Buscamos la ruta
        path, length = self.pathfinder.find_shortest_path(origen, destino)
        
        #Si el camino entre el origen y el destino no existe devolvemos mensaje de error
        if path is None:
            self.result_text.insert(tk.END, f"No se encontro una ruta entre:\n")
            self.result_text.insert(tk.END, f"   '{origen}' y '{destino}'\n\n")
            self.result_text.insert(tk.END, "Esto Son las Estaciones disponibles:\n")
            self.result_text.insert(tk.END, "-------------------------------" + "\n")
            
            #Mostramos todas las opciones de las estaciones que hay disponible en el mapa
            stations = sorted(self.pathfinder.graph.nodes())
            for station in stations:
                self.result_text.insert(tk.END, f"{station}\n")
            
            self.display_image()
            return
        
        # Mostrar resultados
        self.result_text.insert(tk.END, "-" * 45 + "\n")
        self.result_text.insert(tk.END, "     RUTA ENCONTRADA \n")
        self.result_text.insert(tk.END, "-" * 45 + "\n\n")
        
        self.result_text.insert(tk.END, f"Origen: {origen}\n")
        self.result_text.insert(tk.END, f"Destino: {destino}\n")
        self.result_text.insert(tk.END, f"Tiempo: {length} minutos\n")
        self.result_text.insert(tk.END, f"Numero de Estaciones: {len(path)}\n\n")
        
        self.result_text.insert(tk.END, "RECORRIDO:\n")
        self.result_text.insert(tk.END, "-" * 45 + "\n")
        
        for i, station in enumerate(path, 1):
            if i == 1:
                self.result_text.insert(tk.END, f" {i:2d}. {station} ------- INICIO \n")
            elif i == len(path):
                self.result_text.insert(tk.END, f" {i:2d}. {station} ------- DESTINO \n")
            else:
                self.result_text.insert(tk.END, f" {i:2d}. {station}\n")
        
        self.result_text.insert(tk.END, "\n" + "-" * 50 + "\n")
        
        # Mostrar en el mapa
        self.display_image(path)

if __name__ == "__main__":
    app = MetroGUI()
    app.mainloop()