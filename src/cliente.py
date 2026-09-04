class Cliente:
    """"representa a un cliente del banco"""
    
    def __init__(self, nombre: str, documento: str, email: str, id: int = None):
        self.id = id
        self.nombre = nombre
        self.documento = documento
        self.email = email
        
    def __str__(self):
        return f"cliente(id={self.id}, nombre='{self.nombre}', documento='{self.documento}', email='{self.email}')"