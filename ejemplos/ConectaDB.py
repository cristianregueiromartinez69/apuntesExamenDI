

import sqlite3

class ConexionBD:
    def __init__(self, rutaBd):
        """Inicializa la conexión a la base de datos y prepara el cursor."""
        self.rutaBd = rutaBd
        self.conexion = None
        self.cursor = None
        self.conectaBD()

    def conectaBD(self):
        """Conecta a la base de datos SQLite."""
        try:
            self.conexion = sqlite3.connect(self.rutaBd)
            self.cursor = self.conexion.cursor()
            print("Conexión de base de datos realizada")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def crear_tabla(self):
        """Crea la tabla 'usuarios' si no existe."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    dni TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    apelido TEXT NOT NULL,
                    numtelf Integer
                )
            """)
            self.conexion.commit()
            print("Tabla usuarios creada correctamente")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")


    def crear_tablaEjemplo2(self):
        """Crea la tabla 'usuarios' si no existe."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios2 (
                    dni TEXT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    idade Integer NOT NULL,
                    genero TEXT NOT NULL,
                    fallecido Integer
                )
            """)
            self.conexion.commit()
            print("Tabla usuarios creada correctamente")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def consultaSenParametros(self, consultaSQL):
        """Realiza una consulta sin parámetros."""
        try:
            self.cursor.execute(consultaSQL)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error en la consulta: {e}")
            return None

    def consultaConParametros(self, consultaSQL, parametros=()):
        """Realiza una consulta con parámetros."""
        try:
            self.cursor.execute(consultaSQL, parametros)
            self.conexion.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error en la consulta con parámetros: {e}")
            return None

    def pechaBD(self):
        """Cierra la conexión con la base de datos."""
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()



    def insertar_usuario(self, datos):
        try:
            self.cursor.execute(
                "INSERT INTO usuarios (dni, name, apelido, numtelf) VALUES(?, ?, ?, ?)",
                datos,
            )
            self.conexion.commit()
            print("Usuario inserido correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar datos usuarios: {e}")

    def insertar_usuario2(self, datos):
        try:
            self.cursor.execute(
                "INSERT INTO usuarios2 (dni, nome, idade, genero, fallecido) VALUES(?, ?, ?, ?, ?)",
                datos,
            )
            self.conexion.commit()
            print("Usuario inserido correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar datos usuarios: {e}")

    def update_usuarios2(self, newGenero, primaryKey):
        try:
            self.cursor.execute(
                "UPDATE usuarios2 SET genero = ? WHERE dni = ?", (newGenero, primaryKey)
            )
            self.conexion.commit()
            print("Usuario actualizado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al actualizar datos usuarios: {e}")


    def update_fallecido(self, newFallecido, primaryKey):
        try:
            self.cursor.execute(
                "UPDATE usuarios2 SET fallecido = ? WHERE dni = ?", (newFallecido, primaryKey)
            )
            self.conexion.commit()
            print("Usuario asesinado o salvado correctamente correctamente.")
        except sqlite3.Error as e:
            print(f"Error al actualizar datos usuarios: {e}")


    def update_data(self, newName, oldDni):
        try:
            self.cursor.execute(
                "UPDATE usuarios SET name = ? WHERE dni = ?",(newName, oldDni)
            )
            self.conexion.commit()
            print("Usuario actualizado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al actualizar datos usuarios: {e}")




