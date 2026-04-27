from src.operacion import agregar_producto, obtener_productos, actualizar_stock, eliminar_producto

def test_crud_producto():
    # CREATE
    agregar_producto("Quena", 50.0, 10)
    productos = obtener_productos()
    assert any(p.nombre == "Quena" for p in productos)

    # UPDATE
    actualizar_stock("Quena", 20)
    productos = obtener_productos()
    assert any(p.stock == 20 for p in productos if p.nombre == "Quena")

    # DELETE
    eliminar_producto("Quena")
    productos = obtener_productos()
    assert not any(p.nombre == "Quena" for p in productos)
