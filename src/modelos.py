# Validacion que se comunica con la Base de datos
def validar_stock(producto, cantidad):
    session = SessionLocal()
    p = session.query(Producto).filter_by(nombre=producto).first()
    session.close()

    if not p:
        raise ValueError("Producto no encontrado")
    if cantidad <= 0:
        raise ValueError("Cantidad inválida")
    if cantidad > p.stock:
        raise ValueError("Stock insuficiente")
    return True




# Consulta BD
from sqlalchemy import Column, Integer, String, Float
from src.database import Base, SessionLocal

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    precio = Column(Float)
    stock = Column(Integer)

    def __repr__(self):
        return f"<Producto(nombre={self.nombre}, precio={self.precio}, stock={self.stock})>"
