from database import  obtener_conexion
from cliente import Cliente 

class ClienteRepositorio:
    def guardar(self, cliente: Cliente) -> Cliente:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO clientes (nombre, documento, email) VALUES (?, ?, ?)",
            (cliente.nombre, cliente.documento, cliente.email)
        )
        conexion.commit()
        cliente.id = cursor.lastrowid
        conexion.close()
        return cliente
    
    def buscar_por_id(self , id: int) -> Cliente:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, documento, email FROM clientes WHERE id = ?", (id,))
        fila = cursor.fetchone()
        conexion.close()
        
        if fila is None:
            return None
        
        return Cliente(id=fila[0], nombre=fila[1], documento=fila[2], email=fila[3])
    
    def listar_todos(self) -> list[Cliente]:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, documento, email FROM clientes")
        filas = cursor.fetchall()
        conexion.close()
        
        return [Cliente(id=fila[0], nombre=fila[1], documento=fila[2], email=fila[3]) for fila in filas]
        
        