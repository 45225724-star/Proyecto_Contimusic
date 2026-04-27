import pytest
from src.modelos import validar_stock

def test_stock_insuficiente():
    with pytest.raises(ValueError, match="Stock insuficiente"):
        validar_stock("Charango", 10)

def test_stock_suficiente():
    assert validar_stock("Charango", 1) == True
