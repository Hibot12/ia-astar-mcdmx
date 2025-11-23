"""
Script para obtener las coordenadas exactas de cada estación
Haz clic en cada estación para obtener sus coordenadas (x, y)
"""
import tkinter as tk
from PIL import Image, ImageTk
import os

class CoordinatePicker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Selector de Coordenadas - Metro CDMX")
        
        # Cargar imagen
        script_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_dir, "Metro.png")
        
        if not os.path.exists(img_path):
            img_path = "Metro.png"
        
        self.original_img = Image.open(img_path)
        
        # Mostrar dimensiones
        print(f"Dimensiones de la imagen: {self.original_img.width}x{self.original_img.height}")
        
        # Crear canvas
        self.canvas = tk.Canvas(self.root, width=self.original_img.width, 
                               height=self.original_img.height)
        self.canvas.pack()
        
        # Mostrar imagen
        self.photo = ImageTk.PhotoImage(self.original_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
        # Bind click event
        self.canvas.bind("<Button-1>", self.on_click)
        
        # Label para mostrar coordenadas
        self.label = tk.Label(self.root, text="Haz clic en cada estación", 
                             font=("Arial", 12))
        self.label.pack()
        
        # Entry para nombre de estación
        self.name_label = tk.Label(self.root, text="Nombre de la estación:")
        self.name_label.pack()
        
        self.name_entry = tk.Entry(self.root, width=40)
        self.name_entry.pack()
        
        # Botón para guardar
        self.save_btn = tk.Button(self.root, text="Guardar Coordenada", 
                                  command=self.save_coord)
        self.save_btn.pack()
        
        # Almacenar coordenadas
        self.current_coord = None
        self.coordinates = {}
        
        # Mostrar instrucciones
        instructions = """
INSTRUCCIONES:
1. Haz clic en el centro de una estación
2. Escribe el nombre de la estación
3. Haz clic en 'Guardar Coordenada'
4. Repite para todas las estaciones
5. Al cerrar, se imprimirán todas las coordenadas
        """
        self.instructions = tk.Label(self.root, text=instructions, 
                                    justify=tk.LEFT, font=("Arial", 9))
        self.instructions.pack()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    
    def on_click(self, event):
        x, y = event.x, event.y
        self.current_coord = (x, y)
        self.label.config(text=f"Coordenadas: ({x}, {y})")
        
        # Dibujar un punto rojo donde se hizo clic
        self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="red", outline="white")
    
    def save_coord(self):
        if self.current_coord and self.name_entry.get():
            name = self.name_entry.get()
            self.coordinates[name] = self.current_coord
            print(f'"{name}": {self.current_coord},')
            self.name_entry.delete(0, tk.END)
            self.label.config(text=f"✓ Guardada: {name} = {self.current_coord}")
    
    def on_closing(self):
        print("\n" + "="*60)
        print("COORDENADAS FINALES:")
        print("="*60)
        print("self.coords_estacion = {")
        for name, coord in self.coordinates.items():
            print(f'    "{name}": {coord},')
        print("}")
        self.root.destroy()

if __name__ == "__main__":
    CoordinatePicker()
