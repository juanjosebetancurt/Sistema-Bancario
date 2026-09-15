from database import obtener_conexion
from cuenta import Cuenta 

class CuentaRepositorio:
    
    def guardar(self, cuenta: Cuenta):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO cuentas (cliente_id, numero_cuenta, tipo_cuenta, saldo) VALUES (?, ?, ?, ?)",
            (cuenta.cliente_id, cuenta.numero_cuenta, cuenta.tipo_cuenta, cuenta.saldo)
        )
        
        conexion.commit()
        cuenta.id =  cursor.lastrowid
        conexion.close()
        return cuenta 
    
    def buscar_por_id(self, id: int) -> Cuenta:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, cliente_id, numero_cuenta, tipo_cuenta, saldo FROM cuentas WHERE id = ?",
            (id,)
        )
        
        fila = cursor.fetchone()
        conexion.close()
        
        if fila is None:
            return None
        
        return Cuenta(id=fila[0], cliente_id=fila[1], numero_cuenta=fila[2], tipo_cuenta=fila[3], saldo=fila[4])
    
    def actualizar_saldo(self, cuenta: Cuenta):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE cuentas SET saldo = ? WHERE id = ?",
            (cuenta.saldo, cuenta.id)
        )
        conexion.commit()
        conexion.close()
        