import subprocess
from datetime import datetime

"""
Módulo para ejecutar los tests con pytest y actualizar la sección
"## Estado de los tests" en README.md.

Contiene dos funciones principales:
- run_tests: ejecuta pytest y devuelve un mensaje con el resultado y la marca de tiempo.
- update_readme: inserta el mensaje de estado en el README.md justo después del
    encabezado "## Estado de los tests".

Las docstrings siguen el estilo de documentación de Google.
"""


def run_tests():
    """Ejecuta pytest y devuelve un mensaje con el resultado y la fecha/hora.

    Ejecuta `pytest -q` usando subprocess.check_call. Si pytest devuelve código de
    salida 0, se considera que los tests son correctos; cualquier otra salida
    provoca que se considere que los tests han fallado.

    Returns:
            str: Mensaje con emoji y marca de tiempo en formato "YYYY-MM-DD HH:MM",
                     p. ej. "✅ 2025-10-08 12:34 Tests correctos" o
                     "❌ 2025-10-08 12:34 Tests fallidos".
    """
    dia_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        subprocess.check_call(["pytest", "-q"])
        return f"✅ {dia_hora_actual} Tests correctos"
    except subprocess.CalledProcessError:
        return f"❌ {dia_hora_actual} Tests fallidos"


def update_readme(status: str):
    """Actualiza la sección "## Estado de los tests" en README.md con el estado dado.

    Lee el contenido de README.md, busca la línea que contiene exactamente
    "## Estado de los tests" (ignorando espacios alrededor) y añade la línea de
    estado `status` seguida de una línea en blanco inmediatamente después de ese encabezado.
    Finalmente reescribe README.md con el contenido modificado.

    Args:
            status (str): Texto de estado que se insertará (se añadirá un salto de línea
                                        adicional después del texto).

    Raises:
            FileNotFoundError: Si README.md no existe en el directorio actual.
            OSError: Si ocurre algún otro error de E/S al leer o escribir el archivo.
    """
    new_lines = []

    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        new_lines.append(line)
        if line.strip() == "## Estado de los tests":
            new_lines.append(status + "\n\n")

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    status = run_tests()
    update_readme(status)
