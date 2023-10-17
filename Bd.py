import sqlite3

# Conectar a la base de datos (creará el archivo si no existe)
conn = sqlite3.connect('datos_aeroponicos.db')

# Crear un cursor
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS datos_sensores
                  (id INTEGER PRIMARY KEY,
                   temperatura REAL,
                   ph REAL,
                   humedad REAL,
                   luminosidad REAL,
                   nivel_agua REAL,
                   timestamp DATETIME)''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
