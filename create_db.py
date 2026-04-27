from src.database import Base, engine, SessionLocal
from src.modelos import Producto

print("Creando base de datos...")
Base.metadata.create_all(bind=engine)

# Insertar datos iniciales
session = SessionLocal()
session.add_all([
    Producto(nombre="Charango", precio=150, stock=5),
    Producto(nombre="Quena", precio=50, stock=10),
    Producto(nombre="Zampoña", precio=80, stock=3)
])
session.commit()
session.close()