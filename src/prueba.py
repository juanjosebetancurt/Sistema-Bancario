from cliente import Cliente
from cuenta import Cuenta 

c1 = Cliente ("juan cuero", "233455655", "juancuero@gmail.com")


cuenta1 = Cuenta(cliente_id=1, numero_cuenta="0001-0001", saldo=100.0)

cuenta1.depositar(50)
print(cuenta1)

cuenta1.retirar(30)
print(cuenta1)

try:
    cuenta1.retirar(1000)
except ValueError as error:
    print(f"No se puede retirar: {error}")
    
print("el programa sigue corriendo normalmente")
print(cuenta1)
