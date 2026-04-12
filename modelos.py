class Instrumento:
    def __init__(self, id_prod, nombre, categoria, precio, stock):
        self.id = id_prod
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id} | {self.nombre.ljust(18)} | S/ {self.precio:7.2f} | Stock: {self.stock}"