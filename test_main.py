from main import saludo

def test_saludo():
    """Prueba la función saludo.

    Esta prueba verifica si la función saludo devuelve el saludo esperado
    cuando se le proporciona la entrada "Mundo". La salida esperada es "Hola, Mundo!".

    Afirmaciones:
        La salida de saludo("Mundo") debe ser igual a "Hola, Mundo!".
    """
    assert saludo("Mundo") == "Hola, Mundo!"
