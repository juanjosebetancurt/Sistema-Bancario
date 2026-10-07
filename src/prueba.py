from banco_servicio import BancoServicio
from cliente import Cliente
from cliente_repositorio import ClienteRepositorio
from cuenta_repositorio import CuentaRepositorio
from database import crear_tablas
from cuenta import Cuenta


crear_tablas()
cliente_repo = ClienteRepositorio()
servicio = BancoServicio()
cuenta_repo = CuentaRepositorio()

clientes = cliente_repo.listar_todos()
if len(clientes) < 2:
    cliente_1 = Cliente("Cliente 1", "11111111", "cliente1@banco.com")
    cliente_2 = Cliente("Cliente 2", "22222222", "cliente2@banco.com")
    cliente_repo.guardar(cliente_1)
    cliente_repo.guardar(cliente_2)
    clientes = [cliente_1, cliente_2]

cuentas = []
for cliente in clientes[:2]:
    cuenta = cuenta_repo.buscar_por_id(1) if cliente.id == clientes[0].id and cuenta_repo.buscar_por_id(1) is not None else None
    if cuenta is None:
        numero = f"{cliente.id:04d}-0001"
        nueva = Cuenta(cliente_id=cliente.id, numero_cuenta=numero, saldo=0.0)
        cuenta_repo.guardar(nueva)
        cuentas.append(nueva)
    else:
        cuentas.append(cuenta)

if len(cuentas) < 2:
    cuenta_2 = Cuenta(cliente_id=clientes[1].id, numero_cuenta=f"{clientes[1].id:04d}-0002", saldo=0.0)
    cuenta_repo.guardar(cuenta_2)
    cuentas.append(cuenta_2)

cuenta_origen = cuentas[0]
cuenta_destino = cuentas[1]
if cuenta_origen.saldo == 0:
    cuenta_origen.saldo = 100.0
    cuenta_repo.actualizar_saldo(cuenta_origen)
if cuenta_destino.saldo == 0:
    cuenta_destino.saldo = 20.0
    cuenta_repo.actualizar_saldo(cuenta_destino)

print("Nueva cuenta creada con id:", cuenta_origen.id)

try:
    servicio.transferir(cuenta_origen_id=cuenta_origen.id, cuenta_destino_id=cuenta_destino.id, monto=50)
    print("Transferencia exitosa")
except ValueError as error:
    print(f"Transferencia rechazada: {error}")

c1 = cuenta_repo.buscar_por_id(cuenta_origen.id)
c2 = cuenta_repo.buscar_por_id(cuenta_destino.id)
print("Cuenta 1:", c1)
print("Cuenta 2:", c2)