import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import datetime






# Rangos óptimos para las variables
rango_temperatura = (20, 25)
rango_ph = (6, 7.5)
rango_humedad = (60, 80)
rango_luminosidad = (50, 70)
rango_NivelDelAgua = (30, 50)

# Variables para la gráfica
tiempo = []
estado_planta = []

# Función para cargar datos de prueba
def cargar_datos_de_prueba():
    # Simular datos de prueba
    humedad = random.uniform(60, 85)
    ph = random.uniform(6, 8)
    luminosidad = random.uniform(50, 75)
    temperatura = random.uniform(20, 30)
    nivel_de_agua = random.uniform(30, 55)

    # Actualizar las barras de progreso con datos de prueba
    label_humedad_valor.set(humedad)
    label_ph_valor.set(ph)
    label_luminosidad_valor.set(luminosidad)
    label_temperatura_valor.set(temperatura)
    label_NivelDelAgua_valor.set(nivel_de_agua)

    # Clasificar la planta y mostrar el resultado
    resultado = clasificar_planta(temperatura, ph, humedad, luminosidad, nivel_de_agua)
    label_resultado.config(text=resultado)

    # Actualizar la barra de progreso
    if resultado == "Planta saludable":
        progress_bar.config(mode="determinate", value=100)
    else:
        progress_bar.config(mode="determinate", value=0)

    # Agregar datos a la gráfica
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
    # Clasificar la planta
    if (rango_temperatura[0] <= temperatura <= rango_temperatura[1] and
        rango_ph[0] <= ph <= rango_ph[1] and
        rango_humedad[0] <= humedad <= rango_humedad[1] and
        rango_luminosidad[0] <= luminosidad <= rango_luminosidad[1] and
        rango_NivelDelAgua[0] <= nivel_de_agua <= rango_NivelDelAgua[1]):
        return "Planta saludable"
    else:
        return "Planta enferma o inestable"

# Función para actualizar cuadros de texto
def actualizar_cuadros_texto():
    humedad = label_humedad_valor.get()
    ph = label_ph_valor.get()
    luminosidad = label_luminosidad_valor.get()
    temperatura = label_temperatura_valor.get()
    NivelDelAgua = label_NivelDelAgua_valor.get()

    # Actualizar cuadro de texto para la humedad
    if rango_humedad[0] <= humedad <= rango_humedad[1]:
        texto_humedad.set("Humedad óptima")
    else:
        texto_humedad.set("Humedad baja o alta")

    # Actualizar cuadro de texto para el pH
    if rango_ph[0] <= ph <= rango_ph[1]:
        texto_ph.set("pH óptimo")
    else:
        texto_ph.set("pH bajo o alto")

    # Actualizar cuadro de texto para la luminosidad
    if rango_luminosidad[0] <= luminosidad <= rango_luminosidad[1]:
        texto_luminosidad.set("Luminosidad óptima")
    else:
        texto_luminosidad.set("Luminosidad baja o alta")

    # Actualizar cuadro de texto para la temperatura
    if rango_temperatura[0] <= temperatura <= rango_temperatura[1]:
        texto_temperatura.set("Temperatura óptima")
    else:
        texto_temperatura.set("Temperatura baja o alta")

    # Actualizar cuadro de texto para el nivel de agua
    if rango_NivelDelAgua[0] <= NivelDelAgua <= rango_NivelDelAgua[1]:
        texto_NivelDelAgua.set("Nivel de agua óptimo")
    else:
        texto_NivelDelAgua.set("Nivel de agua bajo o alto")

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Aplicación de Control de Maceta Aeropónica")

# Botón para cargar datos de prueba
boton_cargar_prueba = ttk.Button(ventana_principal, text="Cargar Datos de Prueba", command=cargar_datos_de_prueba)
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

# Cuadros de texto para mostrar el estado de cada variable
ttk.Label(ventana_principal, text="Estado de la Humedad:").place(x=30, y=290)
texto_humedad = tk.StringVar()
ttk.Entry(ventana_principal, textvariable=texto_humedad, state="readonly").place(x=30, y=320)

ttk.Label(ventana_principal, text="Estado del pH:").place(x=30, y=350)
texto_ph = tk.StringVar()
ttk.Entry(ventana_principal, textvariable=texto_ph, state="readonly").place(x=30, y=380)

ttk.Label(ventana_principal, text="Estado de la Luminosidad:").place(x=30, y=410)
texto_luminosidad = tk.StringVar()
ttk.Entry(ventana_principal, textvariable=texto_luminosidad, state="readonly").place(x=30, y=440)

ttk.Label(ventana_principal, text="Estado de la Temperatura:").place(x=30, y=470)
texto_temperatura = tk.StringVar()
ttk.Entry(ventana_principal, textvariable=texto_temperatura, state="readonly").place(x=30, y=500)

ttk.Label(ventana_principal, text="Estado del Nivel de Agua:").place(x=30, y=530)
texto_NivelDelAgua = tk.StringVar()
ttk.Entry(ventana_principal, textvariable=texto_NivelDelAgua, state="readonly").place(x=30, y=560)

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
