class Cuenta:
    """"representa una cuenta bancaria asociada a un cliente"""
    
    def __init__(self, cliente_id: int, numero_cuenta: str, tipo_cuenta: str = "ahorros", saldo: float = 0.0, id: int = None):
        self.id = id 
        self.cliente_id = cliente_id
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo
        
    def __str__(self):
        return f"Cuenta(numero='{self.numero_cuenta}', tipo_cuenta='{self.tipo_cuenta}',saldo={self.saldo})"