import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import networkx as nx
import os

class MetroPathFinder:
    """
    Clase que maneja la lógica de búsqueda de rutas en el metro.
    """
    def __init__(self):
        self.graph = nx.Graph()
        self._build_network()
        
        # Coordenadas EXACTAS obtenidas por el usuario haciendo clic en la imagen
        self.coords_estacion = {
            "Tacubaya": (179, 305),
            "San Pedro de los Pinos": (179, 371),
            "San Antonio": (179, 411),
            "Mixcoac": (179, 464),
            "Barranca del Muerto": (179, 529),
            "Constituyentes": (179, 236),
            "Auditorio": (179, 165),
            "Polanco": (179, 90),
            "Observatorio": (136, 349),
            "Patriotismo": (269, 305),
            "Chilpancingo": (372, 305),
            "Lazaro Cardenas": (542, 305),
            "Juanacatlan": (220, 263),
            "Chapultepec": (257, 226),
            "Sevilla": (299, 185),
            "Insurgentes": (341, 151),
            "Cuauhtemoc": (386, 151),
            "Balderas": (436, 151),
            "Juarez": (436, 78),
            "Niños Héroes": (436, 187),
            "Hospital General": (436, 230),
            "Centro Medico": (436, 305),
            "Etiopia": (436, 345),
            "Eugenia": (436, 382),
            "Division del Norte": (436, 422),
            "Zapata": (436, 464),
            "Coyoacan": (436, 501),
            "Viveros": (436, 542),
            "Miguel Ángel de Quevedo": (436, 580),
            "Copilco": (436, 619),
            "Universidad": (436, 658),
            "Parque de los Venados": (535, 464),
            "Eje Central": (596, 553),
            "Insurgentes Sur": (250, 464),
            "Hospital 20 de Noviembre": (336, 464),
        }
    
    def _build_network(self):
        """Construye la red del metro"""
        # Línea 1 (Rosa)
        edges_line1 = [
            ("Observatorio", "Tacubaya", 2),
            ("Tacubaya", "Juanacatlan", 3),
            ("Juanacatlan", "Chapultepec", 2),
            ("Chapultepec", "Sevilla", 2),
            ("Sevilla", "Insurgentes", 2),
            ("Insurgentes", "Cuauhtemoc", 2),
            ("Cuauhtemoc", "Balderas", 2),
        ]
        
        # Línea 3 (Verde olivo)
        edges_line3 = [
            ("Juarez", "Balderas", 2),
            ("Balderas", "Niños Héroes", 2),
            ("Niños Héroes", "Hospital General", 2),
            ("Hospital General", "Centro Medico", 2),
            ("Centro Medico", "Etiopia", 2),
            ("Etiopia", "Eugenia", 2),
            ("Eugenia", "Division del Norte", 2),
            ("Division del Norte", "Zapata", 2),
            ("Zapata", "Coyoacan", 2),
            ("Coyoacan", "Viveros", 2),
            ("Viveros", "Miguel Ángel de Quevedo", 2),
            ("Miguel Ángel de Quevedo", "Copilco", 2),
            ("Copilco", "Universidad", 3),
        ]
        
        # Línea 7 (Naranja)
        edges_line7 = [
            ("Polanco", "Auditorio", 2),
            ("Auditorio", "Constituyentes", 2),
            ("Constituyentes", "Tacubaya", 2),
            ("Tacubaya", "San Pedro de los Pinos", 2),
            ("San Pedro de los Pinos", "San Antonio", 2),
            ("San Antonio", "Mixcoac", 2),
            ("Mixcoac", "Barranca del Muerto", 3),
        ]
        
        # Línea 9 (Café)
        edges_line9 = [
            ("Tacubaya", "Patriotismo", 2),
            ("Patriotismo", "Chilpancingo", 2),
            ("Chilpancingo", "Centro Medico", 2),
            ("Centro Medico", "Lazaro Cardenas", 2),
        ]
        
        # Línea 12 (Dorada)
        # Ruta correcta: Mixcoac → Insurgentes Sur → Hospital 20 de Noviembre → Zapata → Parque de los Venados → Eje Central
        edges_line12 = [
            ("Mixcoac", "Insurgentes Sur", 2),
            ("Insurgentes Sur", "Hospital 20 de Noviembre", 2),
            ("Hospital 20 de Noviembre", "Zapata", 2),
            ("Zapata", "Parque de los Venados", 2),
            ("Parque de los Venados", "Eje Central", 2),
        ]
        
        for u, v, w in edges_line1 + edges_line3 + edges_line7 + edges_line9 + edges_line12:
            self.graph.add_edge(u, v, weight=w)
    
    def find_shortest_path(self, origin, destination):
        """Encuentra la ruta más corta"""
        try:
            path = nx.shortest_path(self.graph, origin, destination, weight='weight')
            length = nx.shortest_path_length(self.graph, origin, destination, weight='weight')
            return path, length
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None, None


class MetroGUI(tk.Tk):
    def __init__(self):
        # Inicializamos la ventana de tkinter
        super().__init__()
        # Titulo del la GUI de la aplicacion
        self.title("Metro Mexico Applicacion")
        # Tamaño del GUI
        self.geometry("1400x900")
        
        # Inicializar el pathfinder
        self.pathfinder = MetroPathFinder()
        
        # Esto crea el contenedor principal con dos columnas left y right
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Esto es el frame izquierdo para los controles
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        # Frame derecho para el mapa del metro
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Etiquetas para pedir las estaciones
        self.estacion_orig_label = ttk.Label(left_frame, text="Introduzca la estacion de Origen:")
        self.estacion_orig_label.pack(pady=10)
        
        # Esto son las entradas de texto (uno para origen y otro para el destino)
        self.entry_origen = ttk.Entry(left_frame, width=30)
        self.entry_origen.pack(pady=5)
        
        self.estacion_dest_label = ttk.Label(left_frame, text="Introduzca la estacion de Destino:")
        self.estacion_dest_label.pack(pady=10)

        self.entry_destino = ttk.Entry(left_frame, width=30)
        self.entry_destino.pack(pady=5)

        # Esto es el boton para demostrar lo que el usuario esta escribiendo
        self.boton = ttk.Button(left_frame, text="Buscar la ruta", command=self.mostrar_inputs)
        self.boton.pack(pady=10)

        # Esto son las etiquetas para mostrar los resultados de la ruta
        self.output_estacion_orig = ttk.Label(left_frame, text="", font=("Arial", 10, "bold"))
        self.output_estacion_orig.pack(pady=5)
        self.output_estacion_dest = ttk.Label(left_frame, text="", font=("Arial", 10, "bold"))
        self.output_estacion_dest.pack(pady=5)

        # Esto es el frame para mostrar el resultado de la ruta
        result_frame = ttk.LabelFrame(left_frame, text="Informacion de la Ruta", padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Un widget de texto para mostrar el recorrido completo
        self.result_text = tk.Text(result_frame, width=40, height=25, wrap=tk.WORD, font=("Arial", 9))
        self.result_text.pack(fill=tk.BOTH, expand=True)

        # Esto añade un scrollbar para el widget del texto de informacion de la ruta
        scrollbar = ttk.Scrollbar(result_frame, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        
        # Esto crea el canvas para mostrar el mapa del metro
        self.canvas = tk.Canvas(right_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind para redimensionar
        self.canvas.bind('<Configure>', self.on_resize)

        # Esto carga el mapa del metro
        self.load_metro_map()
    
    def load_metro_map(self):
        """Este codigo carga el mapa del metro en el GUI"""
        try:
            # Obtener el directorio donde está este script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            
            # Intentar varias rutas posibles para encontrar Metro.png
            possible_paths = [
                os.path.join(script_dir, "Metro.png"),
                os.path.join(script_dir, "..", "Metro.png"),
                os.path.join(script_dir, "..", "src", "Metro.png"),
                "Metro.png",
            ]
            
            # Intentar cada ruta hasta encontrar el archivo
            image_loaded = False
            for path in possible_paths:
                if os.path.exists(path):
                    self.original_image = Image.open(path)
                    self.display_image()
                    image_loaded = True
                    break
            
            if not image_loaded:
                raise FileNotFoundError("No se encontró Metro.png")
                
        except Exception as e:
            self.result_text.insert(tk.END, f"Error cargando mapa: {e}\n")
    
    def on_resize(self, event):
        """Redibuja el mapa cuando se redimensiona la ventana"""
        self.display_image()

    def display_image(self, path=None):
        """Esta funcion muestra el mapa del metro con la ruta resaltada en ROJO"""
        # Si no tiene la imagen original return
        if not hasattr(self, 'original_image'):
            return
        
        # Creamos una copia de la imagen original
        img = self.original_image.copy()

        # Si hay una ruta, la dibujamos en ROJO sobre el mapa
        if path and len(path) > 1:
            draw = ImageDraw.Draw(img)

            # Dibujamos las lineas de la ruta EN ROJO
            for i in range(len(path)-1):
                estacion1 = path[i]
                estacion2 = path[i+1]

                if estacion1 in self.pathfinder.coords_estacion and estacion2 in self.pathfinder.coords_estacion:
                    x1, y1 = self.pathfinder.coords_estacion[estacion1]
                    x2, y2 = self.pathfinder.coords_estacion[estacion2]

                    # Dibujamos la linea ROJA para la ruta
                    draw.line([(x1, y1), (x2, y2)], fill="#FF0000", width=8)
            
            # Dibujamos circulos en cada estacion de la ruta
            for estacion in path:
                if estacion in self.pathfinder.coords_estacion:
                    x, y = self.pathfinder.coords_estacion[estacion]
                    radio = 10

                    # Hacemos que la estacion de origen sea verde y la de destino sea azul
                    if estacion == path[0]:
                        color = "#00FF00"  # Verde brillante
                    elif estacion == path[-1]:
                        color = "#0000FF"  # Azul brillante
                    else: 
                        color = "#FF0000"  # Rojo

                    draw.ellipse([x-radio, y-radio, x+radio, y+radio], 
                               fill=color, outline="white", width=3)
        
        # Esto redimensiona la imagen para ajustar al canvas
        # Obtenemos el ancho actual del canvas en pixeles
        canvas_width = self.canvas.winfo_width()
        # Obtenemos la altura actual del canvas en pixeles
        canvas_height = self.canvas.winfo_height()

        # Esto verifica que el canvas tiene dimensiones validas (que sea mayor que 1 pixel)
        if canvas_width > 1 and canvas_height > 1:
            # Calculamos la proporcion de aspecto de la imagen (ancho/alto)
            img_ratio = img.width / img.height
            # Calculamos la proporcion de aspecto del canvas
            canvas_ratio = canvas_width / canvas_height

            # Aqui determinamos como redimensionar la imagen manteniendo su proporsion
            if img_ratio > canvas_ratio:
                # Si la imagen es mas ancha proporcionalmente, ajustamos por el ancho
                new_width = canvas_width
                new_height = int(canvas_width / img_ratio)
            else:
                # Si la imagen es mas alto proporcionalmente, ajustamos por la altura
                new_height = canvas_height
                new_width = int(canvas_height * img_ratio)
            
            # Redimensionamos la imagen a las nuevas dimensiones
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Convertimos la imagen a una version que tkinter pueda mostrar
        self.photo = ImageTk.PhotoImage(img)
        # Tambien borramos todo el contenido anterior del canvas
        self.canvas.delete("all")
        # Dibujamos la nueva imagen en el canvas en la posición (0, 0)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
    def mostrar_inputs(self):
        """Esto es la funcion que funciona cuando el usuario pulsa el boton"""
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()

        # Actualizar etiquetas
        self.output_estacion_orig.config(text=f"Origen: {origen}")
        self.output_estacion_dest.config(text=f"Destino: {destino}")
        
        # Limpiar resultados anteriores
        self.result_text.delete(1.0, tk.END)
        
        # Validar entrada
        if not origen or not destino:
            self.result_text.insert(tk.END, "⚠️ Por favor introduzca ambas estaciones.\n")
            self.display_image()
            return
        
        if origen == destino:
            self.result_text.insert(tk.END, "⚠️ El origen y destino son la misma estación.\n")
            self.display_image()
            return
        
        # Buscar la ruta
        path, length = self.pathfinder.find_shortest_path(origen, destino)
        
        if path is None:
            self.result_text.insert(tk.END, f"No se encontró una ruta entre:\n")
            self.result_text.insert(tk.END, f"   '{origen}' y '{destino}'\n\n")
            self.result_text.insert(tk.END, "Estaciones disponibles:\n")
            self.result_text.insert(tk.END, "-------------------------------" + "\n")
            
            stations = sorted(self.pathfinder.graph.nodes())
            for station in stations:
                self.result_text.insert(tk.END, f"• {station}\n")
            
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
        self.result_text.insert(tk.END, "-" * 35 + "\n")
        
        for i, station in enumerate(path, 1):
            if i == 1:
                self.result_text.insert(tk.END, f" {i:2d}. {station} ------- INICIO \n")
            elif i == len(path):
                self.result_text.insert(tk.END, f" {i:2d}. {station} ------- DESTINO \n")
            else:
                self.result_text.insert(tk.END, f" {i:2d}. {station}\n")

        
        # Mostrar en el mapa con la ruta en ROJO
        self.display_image(path)


if __name__ == "__main__":
    app = MetroGUI()
    app.mainloop()