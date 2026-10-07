from database import crear_tablas
from cliente import Cliente
from cliente_repositorio import ClienteRepositorio
from cuenta import Cuenta
from cuenta_repositorio import CuentaRepositorio
from transaccion_repositorio import TransaccionRepositorio
from banco_servicio import BancoServicio

cliente_repo = ClienteRepositorio()
cuenta_repo = CuentaRepositorio()
transaccion_repo = TransaccionRepositorio()
servicio = BancoServicio()

def mostrar_menu():
    print("--- Sistema Bancario ---")
    print("1. Crear cliente")
    print("2. Crear cuenta")
    print("3. Depositar")
    print("4. Retirar")
    print("5. Transferir")
    print("6. Consultar saldo")
    print("7. Historial")
    print("8. Salir")
    
    
def crear_cliente():
    nombre = input("Nombre del cliente: ")
    documento = input("Documento del cliente: ")
    email = input("Email del cliente: ")
    try:
        cliente = Cliente(nombre, documento, email)
        cliente_repo.guardar(cliente)
        print(f"cliente creado con id {cliente.id}")
    except Exception as error:
        print(f"No se puede crear el cliente: {error}")
    
def crear_cuenta():
    try:
        cliente_id = int(input("ID del cliente: "))
        numero_cuenta = input("Numero de cuenta:")
        tipo = input("tipo de cuenta (ahorros/corriente): ")
        cuenta = Cuenta(cliente_id=cliente_id, numero_cuenta=numero_cuenta, tipo_cuenta=tipo)
        cuenta_repo.guardar(cuenta)
        print(f"cuenta creado con ID {cuenta.id}")
    except ValueError:
        print("el ID del cliente debe ser un numero")
    except Exception as error:
        print(f"No se puede crear la cuenta: {error}")

def depositar():
    try:
        cuenta_id = int(input("ID de la cuenta: "))
        monto = float(input("Monto a depositar: "))
        servicio.depositar(cuenta_id, monto)
        print("Depósito realizado con éxito.")
    except ValueError as error:
        print(f"No se puede depositar: {error}")
        
def retirar():
    try:
        cuenta_id = int(input("ID de la cuenta: "))
        monto = float(input("monto a retirar: "))
        servicio.retirar(cuenta_id, monto)
        print("Retiro realizado con éxito.")
    except ValueError as error:
        print(f"No se puede retirar: {error}")

def transferir():
    try:
        origen = int(input("ID de la cuenta de origen: "))
        destino = int(input("ID de la cuenta de destino: "))
        monto = float(input("Monto a transferir: "))
        servicio.transferir(origen, destino, monto)
        print("Transferencia realizada con éxito.")
    except ValueError as error:
        print(f"No se puede transferir: {error}")
        
def consultar_saldo():
    try:
        cuenta_id = int(input("ID de la cuenta: "))
        cuenta = cuenta_repo.buscar_por_id(cuenta_id)
        if cuenta is None:
            print("Cuenta no encontrada.")
        else:
            print(f"saldo actual: {cuenta.saldo}")
    except ValueError:
        print("el ID debe ser un numero")
        
def ver_historial():
    try:
        cuenta_id = int(input("ID de la cuenta: "))
        historial = transaccion_repo.listar_por_cuenta(cuenta_id)
        if not historial:
            print("No hay transacciones registrada para esta cuenta.")
        else:
            for t in historial:
                print(f" - {t.fecha} | {t.tipo} | Monto: {t.monto}")      
    except ValueError:
        print("el ID debe ser un numero")        

def salir():
    print("hasta luego!")
    raise SystemExit


def main():
    crear_tablas()
    opciones = {
        "1": crear_cliente,
        "2": crear_cuenta,
        "3": depositar,
        "4": retirar,
        "5": transferir,
        "6": consultar_saldo,
        "7": ver_historial,
        "8": salir,
        "0": salir,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        accion = opciones.get(opcion)
        if accion is None:
            print("Opción inválida. Intente nuevamente.")
            continue

        accion()


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
