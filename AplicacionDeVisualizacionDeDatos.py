import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import datetime

def actualizar_datos_periodicamente():
    mostrar_datos()  # Llama a la función para mostrar los datos

    # Programa la próxima actualización en 30 minutos (1800000 ms)
    ventana_principal.after(1800000, actualizar_datos_periodicamente)

# Rangos óptimos para las variables
rango_temperatura = (20, 25)
rango_ph = (6, 7.5)
rango_humedad = (60, 80)
rango_luminosidad = (50, 70)
rango_NivelDelAgua = (30, 50)

# Variables para la gráfica
tiempo = []
estado_planta = []

# Función para mostrar datos de la base de datos
def mostrar_datos():
    conexion = sqlite3.connect("datos_sensores.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM datos_sensor ORDER BY id DESC LIMIT 1")
    fila = cursor.fetchone()
    conexion.close()

    if fila:
        humedad, ph, luminosidad, temperatura, NivelDelAgua = fila[1], fila[2], fila[3], fila[4], fila[5]
        label_humedad_valor.set(humedad)
        label_ph_valor.set(ph)
        label_luminosidad_valor.set(luminosidad)
        label_temperatura_valor.set(temperatura)
        label_NivelDelAgua_valor.set(NivelDelAgua)

        resultado = clasificar_planta(temperatura, ph, humedad, luminosidad, NivelDelAgua)
        label_resultado.config(text=resultado)
        if resultado == "Planta saludable":
            progress_bar.config(mode="determinate", value=100)
        else:
            progress_bar.config(mode="determinate", value=0)
        tiempo.append(datetime.datetime.now())
        estado_planta.append(resultado)
        actualizar_grafica()
# Función para actualizar la gráfica
def actualizar_grafica():
    if len(tiempo) > 1:
        ax.clear()
        ax.plot(tiempo, estado_planta, marker='o', linestyle='-', color='b')
        ax.set_title("Estado de la Planta a lo largo del tiempo")
        ax.set_xlabel("Tiempo")
        ax.set_ylabel("Estado de la Planta")
        figure_canvas.draw()

# Función para clasificar la planta
def clasificar_planta(temperatura, ph, humedad, luminosidad, nivel_de_agua):
    if (rango_temperatura[0] <= temperatura <= rango_temperatura[1] and
        rango_ph[0] <= ph <= rango_ph[1] and
        rango_humedad[0] <= humedad <= rango_humedad[1] and
        rango_luminosidad[0] <= luminosidad <= rango_luminosidad[1] and
        rango_NivelDelAgua[0] <= nivel_de_agua <= rango_NivelDelAgua[1]):
        return "Planta saludable"
    else:
        return "Planta enferma o inestable"



# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Aplicación de Control de Maceta Aeropónica")

# Botón para cargar datos de prueba
boton_cargar_prueba = ttk.Button(ventana_principal, text="Mostrar Datos", command=mostrar_datos)
boton_cargar_prueba.pack()

# Etiquetas y barras de progreso para sensores
ttk.Label(ventana_principal, text="Humedad:").pack()
label_humedad_valor = tk.DoubleVar()
ttk.Progressbar(ventana_principal, variable=label_humedad_valor, length=200, mode="determinate").pack()

ttk.Label(ventana_principal, text="pH:").pack()
label_ph_valor = tk.DoubleVar()
ttk.Progressbar(ventana_principal, variable=label_ph_valor, length=200, mode="determinate").pack()

ttk.Label(ventana_principal, text="Luminosidad:").pack()
label_luminosidad_valor = tk.DoubleVar()
ttk.Progressbar(ventana_principal, variable=label_luminosidad_valor, length=200, mode="determinate").pack()

ttk.Label(ventana_principal, text="Temperatura:").pack()
label_temperatura_valor = tk.DoubleVar()
ttk.Progressbar(ventana_principal, variable=label_temperatura_valor, length=200, mode="determinate").pack()

ttk.Label(ventana_principal, text="Nivel de Agua:").pack()
label_NivelDelAgua_valor = tk.DoubleVar()
ttk.Progressbar(ventana_principal, variable=label_NivelDelAgua_valor, length=200, mode="determinate").pack()

# Barra de progreso en el Label de resultado
ttk.Label(ventana_principal, text="Estado de la planta:").pack()
label_resultado = ttk.Label(ventana_principal, text="", foreground="red")
label_resultado.pack()
progress_bar = ttk.Progressbar(ventana_principal, mode="determinate", maximum=100, length=200)
progress_bar.pack()











# Gráfica para el estado de la planta a lo largo del tiempo
fig = Figure(figsize=(6, 4))
ax = fig.add_subplot(111)
ax.set_title("Estado de la Planta a lo largo del tiempo")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Estado de la Planta")
figure_canvas = FigureCanvasTkAgg(fig, master=ventana_principal)
figure_canvas.get_tk_widget().pack()

# Iniciar la aplicación
ventana_principal.mainloop()
# Inicia la actualización de la ventana cada 30 minutos
ventana_principal.after(0, actualizar_datos_periodicamente)
ventana_principal.mainloop()
