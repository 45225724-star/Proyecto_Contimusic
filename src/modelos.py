# src/modelos.py
INVENTARIO = {
    "Charango": 5,
    "Quena": 10,
    "Zampoña": 3
}

def validar_stock(producto, cantidad):
    """
    Verifica si hay stock suficiente para un producto.
    Lanza ValueError si el producto no existe, la cantidad es inválida o el stock es insuficiente.
    """
    if producto not in INVENTARIO:
        raise ValueError("Producto no encontrado")

    if cantidad <= 0:
        raise ValueError("Cantidad inválida")

    if cantidad > INVENTARIO[producto]:
        raise ValueError("Stock insuficiente")

    return True

