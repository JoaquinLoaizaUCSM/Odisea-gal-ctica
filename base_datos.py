import sqlite3


class BaseDeDatosJuego:
    """Clase Base de Datos Juego."""
    def __init__(self):
        self.conexion = sqlite3.connect("datos_juego.db")
        self.cursor = self.conexion.cursor()
        self.inicializar_tablas()

    def inicializar_tablas(self):
        """Inicializa las tablas en la base de datos."""
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS Jugador (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                puntuacion INTEGER,
                fecha DATE
                );
                
            CREATE TABLE IF NOT EXISTS  Ranking (
                id_ranking INTEGER PRIMARY KEY AUTOINCREMENT,
                id_jugador INTEGER);
        ''')
        self.conexion.commit()

    def guardar_puntuacion(self, nombre: str, puntuacion: int, fecha: str):
        """
        Guarda la puntuacion de un jugador en la base de datos si el nombre no se repite.
        :param nombre: Nombre del jugador.
        :param puntuacion: Puntuacion del jugador.
        :param fecha: Fecha de la puntuacion.
        """
        if nombre not in self.obtener_nombres():
            self.cursor.execute("INSERT INTO Jugador (nombre, puntuacion, fecha) VALUES (?, ?, ?)",
                                (nombre, puntuacion, fecha))
            self.conexion.commit()

    def guardar_ranking(self):
        """Actualiza o inserta el ranking del jugador con la puntuacion más alta en la base de datos."""
        if self.mostrar_ranking():
            self.cursor.execute("""UPDATE Ranking SET id_jugador = (
            SELECT id FROM Jugador ORDER BY puntuacion DESC LIMIT 1)""")
        else:
            self.cursor.execute("""INSERT INTO Ranking (id_jugador) VALUES (
            (SELECT id FROM Jugador ORDER BY puntuacion DESC LIMIT 1))""")
        self.conexion.commit()

    def obtener_puntuaciones(self) -> list:
        """Obtiene las puntuaciones de los jugadores de la base de datos."""
        self.cursor.execute("SELECT * FROM Jugador ORDER BY puntuacion DESC")
        return self.cursor.fetchall()

    def obtener_nombres(self) -> list:
        """Obtiene los nombres de los jugadores de la base de datos."""
        self.cursor.execute("SELECT nombre FROM Jugador ORDER BY puntuacion DESC")
        return [nombre[0] for nombre in self.cursor.fetchall()]

    def mostrar_ranking(self) -> list:
        """Obtiene el ranking de la base de datos."""
        self.cursor.execute("SELECT * FROM Ranking ORDER BY id_ranking DESC")
        return self.cursor.fetchall()


# if __name__ == "__main__":
#     # Probar la base de datos
#     base_de_datos = BaseDeDatosJuego()
#
#     # Guardar puntuaciones de prueba
#     base_de_datos.guardar_puntuacion("Jugador 1", 100, "2021-01-01")
#     base_de_datos.guardar_puntuacion("Jugador 2", 200, "2021-01-02")
#     base_de_datos.guardar_puntuacion("Jugador 3", 300, "2021-01-03")
#
#     # Guardar el ranking
#     base_de_datos.guardar_ranking()
#
#     # Imprimir los datos de prueba
#     print(base_de_datos.obtener_puntuaciones())
#     print(base_de_datos.obtener_nombres())
#     print(base_de_datos.mostrar_ranking())
