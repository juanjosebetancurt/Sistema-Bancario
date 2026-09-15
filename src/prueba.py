import sqlite3
import uuid
from cliente import Cliente
from cliente_repositorio import ClienteRepositorio
from cuenta import Cuenta
from cuenta_repositorio import CuentaRepositorio

cliente_repo = ClienteRepositorio()
cuenta_repo = CuentaRepositorio()

# Reutilizamos el cliente que ya existe (id=1), no creamos uno nuevo
nueva_cuenta = Cuenta(
	cliente_id=1,
	numero_cuenta=f"0001-{uuid.uuid4().hex[:8]}",
	saldo=200.0,
)
guardada = cuenta_repo.guardar(nueva_cuenta)
print("Cuenta guardada:", guardada)

guardada.depositar(100)
cuenta_repo.actualizar_saldo(guardada)
print("Saldo actualizado en memoria:", guardada)

recuperada = cuenta_repo.buscar_por_id(guardada.id)
print("Cuenta recuperada de la base de datos:", recuperada)