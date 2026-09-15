import sqlite3
from cliente import Cliente
from cliente_repositorio import ClienteRepositorio

repo = ClienteRepositorio()

nuevo_cliente = Cliente("Juan Perez", "999888", "juan.perez@mail.com")

try:
    guardado = repo.guardar(nuevo_cliente)
    print("Guardado:", guardado)
except sqlite3.IntegrityError as error:
    print(f"No se pudo guardar el cliente: {error}")

todos = repo.listar_todos()
print("Todos los clientes:")
for c in todos:
    print(" -", c)