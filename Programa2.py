import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm # Importamos los mapas de color

# --- Lógica principal para crear la interfaz ---
class VolumetricRoseApp:
    def __init__(self, root):
        """Inicializa la aplicación de la GUI para la rosa volumétrica."""
        self.root = root
        self.root.title("Graficador de Rosas Volumétricas")
        self.root.geometry("800x850") # Tamaño inicial de la ventana

        # --- Creación del Frame principal ---
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # --- Controles de usuario (entrada y botón) ---
        controls_frame = ttk.Frame(main_frame)
        controls_frame.grid(row=0, column=0, pady=10, sticky=(tk.W, tk.E))
        controls_frame.columnconfigure(1, weight=1)

        ttk.Label(controls_frame, text="Valor de k (pétalos):").grid(row=0, column=0, padx=5)
        self.k_value = tk.StringVar(value="5") # Valor inicial
        self.k_entry = ttk.Entry(controls_frame, textvariable=self.k_value, width=10)
        self.k_entry.grid(row=0, column=1, padx=5, sticky=tk.W)

        self.draw_button = ttk.Button(controls_frame, text="Generar Rosa 🌹", command=self.draw_rose)
        self.draw_button.grid(row=0, column=2, padx=10)
        
        # --- Lienzo para la gráfica de Matplotlib ---
        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        canvas_frame = ttk.Frame(main_frame)
        canvas_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.rowconfigure(1, weight=1)
        main_frame.columnconfigure(0, weight=1)

        self.canvas = FigureCanvasTkAgg(self.fig, master=canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Dibujar la primera rosa al iniciar
        self.draw_rose()

    def draw_rose(self):
        """Dibuja la superficie de la rosa en el lienzo 3D."""
        try:
            k = float(self.k_value.get())
            if k <= 0:
                messagebox.showerror("Entrada Inválida", "Por favor, introduce un número positivo para k.")
                return
        except ValueError:
            messagebox.showerror("Entrada Inválida", "Por favor, introduce un número válido para k.")
            return

        self.ax.clear()

        # 1. Crear una malla de coordenadas polares
        # theta es el ángulo, v es un parámetro para recorrer el radio del pétalo (0 a 1)
        n_points = 200
        theta = np.linspace(0, 2 * np.pi, n_points)
        v = np.linspace(-0.5, 0.5, n_points) # v controla el ancho y forma del pétalo
        theta, v = np.meshgrid(theta, v)

        # 2. Ecuación de la rosa para el contorno
        petal_shape = np.cos(k * theta)
        
        # 3. Calcular las coordenadas cartesianas (x, y, z) para la superficie
        # La forma de la rosa se modula en x e y
        x = petal_shape * np.cos(theta) - v * np.sin(theta)
        y = petal_shape * np.sin(theta) + v * np.cos(theta)

        # La altura 'z' da la forma volumétrica y curvatura del pétalo
        # Usamos una combinación de funciones para una apariencia más orgánica
        z = 0.8 * v**2 + 0.2 * np.sin(1.5 * petal_shape * np.pi)

        # 4. Graficar la superficie
        # Usamos un mapa de color rojo-rosa y lo invertimos ('Reds_r')
        # El color de cada punto dependerá de su altura 'z'
        self.ax.plot_surface(x, y, z, cmap=cm.Reds_r, rstride=1, cstride=1, antialiased=True)
        
        # 5. Configuración de la apariencia del gráfico
        self.ax.set_title(f'Rosa Volumétrica (k = {k})', fontsize=16)
        self.ax.set_xlabel('Eje X')
        self.ax.set_ylabel('Eje Y')
        self.ax.set_zlabel('Eje Z')
        
        # Ocultar los planos de los ejes para una vista más limpia
        self.ax.xaxis.pane.fill = False
        self.ax.yaxis.pane.fill = False
        self.ax.zaxis.pane.fill = False
        self.ax.grid(False)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])

        # Ajustar la vista inicial
        self.ax.view_init(elev=40, azim=-75)

        # Actualizar el lienzo
        self.canvas.draw()

# --- Punto de entrada del programa ---
if __name__ == "__main__":
    root = tk.Tk()
    app = VolumetricRoseApp(root)
    root.mainloop()