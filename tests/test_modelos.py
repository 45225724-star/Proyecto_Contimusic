import pytest
from src.database import Base, engine, SessionLocal
from src.modelos import Producto, validar_stock

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Crear tablas en memoria para pruebas
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    session.add(Producto(nombre="Charango", precio=150.0, stock=5))
    session.commit()
    session.close()
    yield
    Base.metadata.drop_all(bind=engine)

def test_stock_suficiente():
    assert validar_stock("Charango", 1) == True

def test_stock_insuficiente():
    with pytest.raises(ValueError, match="Stock insuficiente"):
        validar_stock("Charango", 10)

def test_producto_inexistente():
    with pytest.raises(ValueError, match="Producto no encontrado"):
        validar_stock("Guitarra", 1)
