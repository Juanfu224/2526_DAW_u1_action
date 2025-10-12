<a id="main"></a>

# main

<a id="main.saludo"></a>

#### saludo

```python
def saludo(nombre: str) -> str
```

Genera un saludo personalizado.

**Arguments**:

- `nombre` (`str`): El nombre de la persona a saludar.

**Returns**:

`str`: Un saludo en forma de cadena que incluye el nombre proporcionado.

<a id="update_readme"></a>

# update\_readme

<a id="update_readme.run_tests"></a>

#### run\_tests

```python
def run_tests()
```

Ejecuta pytest y devuelve un mensaje con el resultado y la fecha/hora.

Ejecuta el comando ``pytest -q`` usando :func:`subprocess.check_call`.  
Si pytest devuelve código de salida ``0``, se considera que los tests son correctos.  
Cualquier otra salida provoca que se considere que los tests han fallado.

**Returns**:

`str`: Mensaje con emoji y marca de tiempo en formato ``YYYY-MM-DD HH:MM``.  
Por ejemplo:  
``✅ 2025-10-08 12:34 Tests correctos`` o  
``❌ 2025-10-08 12:34 Tests fallidos``.

<a id="update_readme.update_readme"></a>

#### update\_readme

```python
def update_readme(status: str)
```

Actualiza la sección ``## Estado de los tests`` en README.md con el estado dado.

Lee el contenido de ``README.md``, busca la línea que contiene exactamente
``## Estado de los tests`` (ignorando espacios alrededor) y añade la línea de
estado ``status`` seguida de una línea en blanco inmediatamente después de ese encabezado.  
Finalmente, reescribe ``README.md`` con el contenido modificado.

**Arguments**:

- `status` (`str`): Texto de estado que se insertará (se añadirá un salto de línea adicional después del texto).

**Raises**:

- `FileNotFoundError`: Si ``README.md`` no existe en el directorio actual.
- `OSError`: Si ocurre algún otro error de E/S al leer o escribir el archivo.

<a id="test_main"></a>

# test\_main

<a id="test_main.test_saludo"></a>

#### test\_saludo

```python
def test_saludo()
```

Prueba la función ``saludo``.

Esta prueba verifica si la función ``saludo`` devuelve el saludo esperado
cuando se le proporciona la entrada ``"Mundo"``.  
La salida esperada es ``"Hola, Mundo!"``.

**Raises**:

- `AssertionError`: Si la salida de ``saludo("Mundo")`` no es igual a ``"Hola, Mundo!"``.

