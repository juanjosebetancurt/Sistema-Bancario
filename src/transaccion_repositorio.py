
import database
from transaccion import Transaccion

class TransaccionRepositorio:
    def guardar(self, transaccion: Transaccion):
        conexion = database.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO transacciones (cuenta_id, tipo, monto, fecha) VALUES (?, ?, ?, ?)",
            (transaccion.cuenta_id, transaccion.tipo, transaccion.monto, transaccion.fecha)
        )
        conexion.commit()
        transaccion.id = cursor.lastrowid
        conexion.close()
        return transaccion
    
    def listar_por_cuenta(self, cuenta_id: int) -> list[Transaccion]:
        conexion = database.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
                "SELECT id, cuenta_id, tipo, monto, fecha FROM transacciones WHERE cuenta_id = ? ORDER BY fecha",
                (cuenta_id,)
        )
        filas = cursor.fetchall()
        conexion.close()
        
        return [Transaccion(id=fila[0], cuenta_id=fila[1], tipo=fila[2], monto=fila[3], fecha=fila[4]) for fila in filas]