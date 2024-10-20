import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        print("Intentando conectar a la base de datos...")
        conn = mysql.connector.connect(
            host="localhost", database="bdevaluacion2", user="root", password=""
        )
        print("Conexión exitosa!")
        return conn
    except Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        return None


def crear_tablas():
    conn = conectar()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        print("Creando tablas...")

        # Tabla de Empleados
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(25) NOT NULL,
                direccion VARCHAR(25),
                telefono VARCHAR(20),
                email VARCHAR(25),
                fecha_contrato DATE,
                salario DECIMAL(10,2)
            )
        """)

        # Tabla de Departamentos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS departamentos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                gerente_id INT,
                FOREIGN KEY (gerente_id) REFERENCES empleados(id) ON DELETE SET NULL
            )
        """)

        # Tabla de Proyectos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS proyectos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                descripcion TEXT,
                fecha_inicio DATE
            )
        """)

        # Tabla de Asignación de Empleados a Proyectos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados_proyecto (
                empleado_id INT,
                proyecto_id INT,
                PRIMARY KEY (empleado_id, proyecto_id),
                FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE,
                FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE
            )
        """)

        conn.commit()
        print("Tablas creadas exitosamente!")
    except Error as e:
        print(f"Error al crear tablas: {e}")
    finally:
        cursor.close()
        conn.close()


crear_tablas()
