from src.database import SessionLocal
from src.modelos import Producto

# CREATE
def agregar_producto(nombre, precio, stock):
    session = SessionLocal()
    nuevo = Producto(nombre=nombre, precio=precio, stock=stock)
    session.add(nuevo)
    session.commit()
    session.close()

# READ
def obtener_productos():
    session = SessionLocal()
    productos = session.query(Producto).all()
    session.close()
    return productos

def obtener_producto_por_nombre(nombre):
    session = SessionLocal()
    producto = session.query(Producto).filter_by(nombre=nombre).first()
    session.close()
    return producto

# UPDATE
def actualizar_stock(nombre, nuevo_stock):
    session = SessionLocal()
    producto = session.query(Producto).filter_by(nombre=nombre).first()
    if producto:
        producto.stock = nuevo_stock
        session.commit()
    session.close()

# DELETE
def eliminar_producto(nombre):
    session = SessionLocal()
    producto = session.query(Producto).filter_by(nombre=nombre).first()
    if producto:
        session.delete(producto)
        session.commit()
    session.close()


    from src.operacion import obtener_productos

productos = obtener_productos()
for p in productos:
    print(p.nombre, p.precio, p.stock)