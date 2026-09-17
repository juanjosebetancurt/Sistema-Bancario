import sqlite3
from database import crear_tablas
from cliente import Cliente
from cliente_repositorio import ClienteRepositorio
from cuenta import Cuenta
from cuenta_repositorio import CuentaRepositorio
from transaccion import Transaccion
from transaccion_repositorio import TransaccionRepositorio

crear_tablas()

cliente_repo = ClienteRepositorio()
cuenta_repo = CuentaRepositorio()
transaccion_repo = TransaccionRepositorio()

cliente = cliente_repo.buscar_por_id(1)
if cliente is None:
    cliente = Cliente(nombre="Ana García", documento="12345678", email="ana@example.com")
    cliente = cliente_repo.guardar(cliente)

cuenta = cuenta_repo.buscar_por_id(1)
if cuenta is None:
    cuenta = Cuenta(cliente_id=cliente.id, numero_cuenta="001", tipo_cuenta="ahorros", saldo=0.0)
    cuenta = cuenta_repo.guardar(cuenta)

print("Cuenta antes:", cuenta)

cuenta.depositar(75)
cuenta_repo.actualizar_saldo(cuenta)

trans = Transaccion(cuenta_id=cuenta.id, tipo="deposito", monto=75)
transaccion_repo.guardar(trans)

print("Cuenta despues:", cuenta)

historial = transaccion_repo.listar_por_cuenta(cuenta.id)
print("Historial:")
for t in historial:
    print(" -", t)