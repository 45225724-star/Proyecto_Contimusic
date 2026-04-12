from modelos import Instrumento

def cargar_catalogo():
    """Retorna la lista de productos inicial de ContiMusic."""
    return [
        Instrumento(101, "Charango Pro", "Cuerdas", 450.00, 10),
        Instrumento(102, "Quena Profesional", "Vientos", 120.00, 15),
        Instrumento(103, "Cajón Peruano", "Percusión", 350.00, 5),
        Instrumento(104, "Zampoña", "Vientos", 180.00, 8),
        Instrumento(105, "Guitarra Criolla", "Cuerdas", 600.00, 3)
    ]