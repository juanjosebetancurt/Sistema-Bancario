import runpy
import os
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'

sys.path.insert(0, str(SRC))


class PruebaScriptTest(unittest.TestCase):
    def test_prueba_debe_ejecutarse_sin_crash_si_la_base_esta_vacia(self):
        directorio_original = Path.cwd()
        with tempfile.TemporaryDirectory() as directorio_temporal:
            try:
                os.chdir(directorio_temporal)
                runpy.run_path(str(SRC / 'prueba.py'), run_name='__main__')
            finally:
                os.chdir(directorio_original)

    def test_transferencia_actualiza_saldos_y_registra_movimientos(self):
        from banco_servicio import BancoServicio
        from database import crear_tablas, obtener_conexion

        directorio_original = Path.cwd()
        with tempfile.TemporaryDirectory() as directorio_temporal:
            try:
                os.chdir(directorio_temporal)
                crear_tablas()
                conexion = obtener_conexion()
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO clientes (nombre, documento, email) VALUES ('A', '1', 'a@test')")
                cursor.execute("INSERT INTO clientes (nombre, documento, email) VALUES ('B', '2', 'b@test')")
                cursor.execute("INSERT INTO cuentas (cliente_id, numero_cuenta, tipo_cuenta, saldo) VALUES (1, '001', 'ahorros', 100)")
                cursor.execute("INSERT INTO cuentas (cliente_id, numero_cuenta, tipo_cuenta, saldo) VALUES (2, '002', 'ahorros', 20)")
                conexion.commit()
                conexion.close()

                BancoServicio().transferir(1, 2, 50)

                conexion = obtener_conexion()
                cursor = conexion.cursor()
                cursor.execute("SELECT saldo FROM cuentas ORDER BY id")
                self.assertEqual(cursor.fetchall(), [(50.0,), (70.0,)])
                cursor.execute("SELECT cuenta_id, tipo, monto FROM transacciones ORDER BY id")
                self.assertEqual(
                    cursor.fetchall(),
                    [(1, 'transaccion_enviada', 50.0), (2, 'transaccion_recibida', 50.0)],
                )
                conexion.close()
            finally:
                os.chdir(directorio_original)


if __name__ == '__main__':
    unittest.main()
