import sqlite3


# Clase de Base de Datos
class BaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("datos_juego.db")
        self.cursor = self.conexion.cursor()
        self.inicializar_tabla()

    # Inicializa la tabla en la base de datos
    def inicializar_tabla(self):
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS jugador (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                puntuacion INTEGER,
                fecha DATE
                );
                
            CREATE TABLE IF NOT EXISTS  ranking (
                id_ranking INTEGER PRIMARY KEY AUTOINCREMENT,
                id_jugador INTEGER);
                
        ''')
        self.conexion.commit()

    # Función para guardar puntuaciones en la base de datos
    def guardar_puntuacion(self, nombre, puntuacion, fecha):
        # verificamos que no se repita el nombre
        if nombre in self.obtener_nombre():
            return

        self.cursor.execute("INSERT INTO jugador (nombre, puntuacion, fecha) VALUES (?, ?, ?)",
                            (nombre, puntuacion, fecha))
        self.conexion.commit()

    # Función para guardar el ranking desde la base de datos
    def guardar_ranking(self):
        # Remplacer el valor de id_jugador por el id del jugador con la puntuación más alta
        if self.mostrar_ranking():
            self.cursor.execute("""UPDATE ranking SET id_jugador = (
            SELECT id FROM jugador ORDER BY puntuacion DESC LIMIT 1)""")
            self.conexion.commit()
            return
        else:
            self.cursor.execute("""INSERT INTO ranking (id_jugador) VALUES (
            (SELECT id FROM jugador ORDER BY puntuacion DESC))""")
            self.conexion.commit()

    # Función para obtener las puntuaciones de la base de datos
    def obtener_puntuaciones(self):
        self.cursor.execute("SELECT * FROM jugador ORDER BY puntuacion DESC")
        return self.cursor.fetchall()

    # Función para obtener el nombre del jugador
    def obtener_nombre(self):
        self.cursor.execute("SELECT nombre FROM jugador ORDER BY puntuacion DESC")
        nombres = [nombre[0] for nombre in self.cursor.fetchall()]
        return nombres

    # Función para mostrar el ranking
    def mostrar_ranking(self):
        self.cursor.execute("SELECT * FROM ranking ORDER BY id_ranking DESC")
        return self.cursor.fetchall()


# Probar la base de datos

# base_datos = BaseDatos()
# base_datos.guardar_puntuacion("Jugador 1", 100, "2021-01-01")
# base_datos.guardar_puntuacion("Jugador 2", 200, "2021-01-02")
# base_datos.guardar_puntuacion("Jugador 3", 300, "2021-01-03")
#
# base_datos.guardar_ranking()
#
# print(base_datos.obtener_puntuaciones())
# print(base_datos.obtener_nombre())
# print(base_datos.mostrar_ranking())

