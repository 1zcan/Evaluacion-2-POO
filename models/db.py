import mysql.connector
from mysql.connector import Error

class DB:

    mydb = None

    def __init__(self):
        if not DB.mydb:
            try:
                print("Intentando conectar a la base de datos...")
                DB.mydb = mysql.connector.connect(
                    host='localhost',
                    database='ev3',
                    user='root',
                    password='' )
            
            except Error as e:
                print(f"Error al conectar a MariaDB: {e}")

    @staticmethod
    def get_connection():
        return DB.mydb
    
    def close_connection(self):
        if DB.mydb:
            DB.mydb.close()
            DB.mydb = None


def crear_tablas():

    conn = DB().get_connection()
    
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        print("Creando tablas...")

        # Tabla de Empleados
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS empleados (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                direccion VARCHAR(50),
                telefono VARCHAR(20),
                email VARCHAR(50),
                fecha_contrato DATE,
                salario DECIMAL(10,2)
            )
        ''')

        # Tabla de Departamentos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS departamentos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                gerente_id INT,
                FOREIGN KEY (gerente_id) REFERENCES empleados(id) ON DELETE SET NULL
            )
        ''')

        # Tabla de Proyectos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS proyectos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                descripcion TEXT,
                fecha_inicio DATE
            )
        ''')

        # Tabla de Asignación de Empleados a Proyectos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS empleados_proyecto (
                empleado_id INT,
                proyecto_id INT,
                PRIMARY KEY (empleado_id, proyecto_id),
                FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE,
                FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE
            )
        ''')

        # Tabla de Asignaciones
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS asignaciones (
                empleado_id INT,
                departamento_id INT,
                PRIMARY KEY (empleado_id),
                FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE,
                FOREIGN KEY (departamento_id) REFERENCES departamentos(id) ON DELETE CASCADE
            )
        ''')

        # Tabla de Registro de Tiempo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registro_tiempo (
                id INT AUTO_INCREMENT PRIMARY KEY,
                empleado_id INT,
                fecha DATE,
                horas INT,
                descripcion TEXT,
                proyecto_id INT,
                FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE,
                FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                       
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                contrasena VARCHAR(50) NOT NULL         
            )
        ''')
        conn.commit()
        print("Tablas creadas exitosamente!")
    except Error as e:
        print(f"Error al crear tablas: {e}")
    finally:
        cursor.close()
        

crear_tablas()

