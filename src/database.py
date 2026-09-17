import sqlite3

NOMBRE = "banco.db"

def obtener_conexion():
    conexion = sqlite3.connect(NOMBRE)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

def crear_tablas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS clientes(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT NOT NULL,
                       documento TEXT NOT NULL UNIQUE,
                       email TEXT NOT NULL
                   )
                   """)
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS cuentas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cliente_id integer NOT NULL,
                        numero_cuenta TEXT NOT NULL UNIQUE,
                        tipo_cuenta TEXT NOT NULL,
                        saldo REAL NOT NULL DEFAULT 0,
                        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
                    )
                    """)
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS transacciones (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cuenta_id INTEGER NOT NULL,
                        tipo TEXT NOT NULL,
                        monto REAL NOT NULL,
                        fecha TEXT NOT NULL,
                        FOREIGN KEY (cuenta_id) REFERENCES cuentas (id)
        )
    """)
    conexion.commit()
    conexion.close()    
    print("tablas creadas correctamnente")
    
if __name__ == "__main__":
    crear_tablas()
    