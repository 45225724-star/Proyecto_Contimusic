class Carrito:
    def __init__(self):
        self.items = []
        self.IGV_TASA = 0.18

    def agregar(self, instrumento, cantidad):
        if instrumento.stock >= cantidad:
            subtotal = instrumento.precio * cantidad
            self.items.append({
                "nombre": instrumento.nombre,
                "cantidad": cantidad,
                "subtotal": subtotal
            })
            instrumento.stock -= cantidad
            return True
        return False

    def calcular_totales(self):
        base = sum(item['subtotal'] for item in self.items)
        igv = base * self.IGV_TASA
        total = base + igv
        return base, igv, total