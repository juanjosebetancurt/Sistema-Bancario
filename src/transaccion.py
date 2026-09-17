from datetime import datetime

class Transaccion:
    """"Representa un movimiento registtado sobre la cuenta"""
    
    def __init__(self, cuenta_id: int, tipo: str, monto: float, fecha: str = None, id: int = None):
        self.id = id
        self.cuenta_id = cuenta_id
        self.tipo = tipo
        self.monto = monto
        self.fecha = fecha or datetime.now().isoformat()
    
    def __str__(self):
        return f"Transaccion(tipo='{self.tipo}', monto={self.monto}, fecha='{self.fecha}')"