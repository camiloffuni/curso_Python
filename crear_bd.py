import sqlite3

# Crea el archivo base_de_datos.db si no existe
conexion = sqlite3.connect("base_de_datos.db")

cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS historial (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT,
    color TEXT,
    docena TEXT,
    columna TEXT,
    par TEXT,
    impar TEXT,
    mayor TEXT,
    menor TEXT
    
)
""")

conexion.commit()
conexion.close()
