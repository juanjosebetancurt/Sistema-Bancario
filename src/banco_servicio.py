from datetime import datetime

from database import obtener_conexion


class BancoServicio:
    def transferir(self, cuenta_origen_id: int, cuenta_destino_id: int, monto: float):
        if monto <= 0:
            raise ValueError("el monto a transferir debe ser mayor a cero")

        if cuenta_origen_id == cuenta_destino_id:
            raise ValueError("No puedes transferir a la misma cuenta")

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT saldo FROM cuentas WHERE id = ?", (cuenta_origen_id,))
            fila_origen = cursor.fetchone()
            if fila_origen is None:
                raise ValueError("La cuenta no existe")
            saldo_origen = fila_origen[0]

            cursor.execute("SELECT id FROM cuentas WHERE id = ?", (cuenta_destino_id,))
            if cursor.fetchone() is None:
                raise ValueError("La cuenta destino no existe")

            if monto > saldo_origen:
                raise ValueError("fondos insuficientes en la cuenta origen")

            cursor.execute(
                "UPDATE cuentas SET saldo = saldo - ? WHERE id = ?",
                (monto, cuenta_origen_id),
            )
            cursor.execute(
                "UPDATE cuentas SET saldo = saldo + ? WHERE id = ?",
                (monto, cuenta_destino_id),
            )

            fecha = datetime.now().isoformat()

            cursor.execute(
                "INSERT INTO transacciones (cuenta_id, tipo, monto, fecha) VALUES (?, ?, ?, ?)",
                (cuenta_origen_id, "transaccion_enviada", monto, fecha),
            )

            cursor.execute(
                "INSERT INTO transacciones (cuenta_id, tipo, monto, fecha) VALUES (?, ?, ?, ?)",
                (cuenta_destino_id, "transaccion_recibida", monto, fecha),
            )

            conexion.commit()

        except Exception:
            conexion.rollback()
            raise
        finally:
            conexion.close()

    def depositar(self, cuenta_id: int, monto: float):
        if monto <= 0:
            raise ValueError("el monto a depositar debe ser mayor a cero")

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT id FROM cuentas WHERE id = ?", (cuenta_id,))
            if cursor.fetchone() is None:
                raise ValueError("La cuenta no existe")

            cursor.execute(
                "UPDATE cuentas SET saldo = saldo + ? WHERE id = ?",
                (monto, cuenta_id),
            )
            cursor.execute(
                "INSERT INTO transacciones (cuenta_id, tipo, monto, fecha) VALUES (?, ?, ?, ?)",
                (cuenta_id, "deposito", monto, datetime.now().isoformat()),
            )
            conexion.commit()
        except Exception:
            conexion.rollback()
            raise
        finally:
            conexion.close()

    def retirar(self, cuenta_id: int, monto: float):
        if monto <= 0:
            raise ValueError("el monto a retirar debe ser mayor a cero")

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT saldo FROM cuentas WHERE id = ?", (cuenta_id,))
            fila = cursor.fetchone()
            if fila is None:
                raise ValueError("La cuenta no existe")

            if monto > fila[0]:
                raise ValueError("fondos insuficientes")

            cursor.execute(
                "UPDATE cuentas SET saldo = saldo - ? WHERE id = ?",
                (monto, cuenta_id),
            )
            cursor.execute(
                "INSERT INTO transacciones (cuenta_id, tipo, monto, fecha) VALUES (?, ?, ?, ?)",
                (cuenta_id, "retiro", monto, datetime.now().isoformat()),
            )
            conexion.commit()
        except Exception:
            conexion.rollback()
            raise
        finally:
            conexion.close()

