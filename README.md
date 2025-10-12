# Mi Proyecto con GitHub Actions
## Estructura del proyecto
#### ⚙️ Automatización e Integración
- **`.github/workflows/git_actions.yaml`** → Define un **workflow de GitHub Actions** que ejecuta tareas automáticas (como tests o commits automáticos).

#### 🧩 Archivos principales
- **`main.py`** → Código principal del proyecto.  
- **`test_main.py`** → Contiene los **tests unitarios** para verificar el correcto funcionamiento del código.  
- **`update_readme.py`** → Script que **ejecuta los tests** y **actualiza el `README.md`** con los resultados.

#### 📄 Documentación
- **`pydoc-markdown.yml`** → Indica:
  - Qué módulos documentar (`main`, `update_readme`, `test_main`).
  - Dónde buscarlos (en el directorio actual).
  - Cómo generar la documentación (`docs/markdown.md` en formato Markdown).
- **`docs/html/`** → Contiene la documentación **HTML generada con Doxygen** a partir del **Doxyfile**.
- **`docs/markdown.md`** → Documentación **Markdown generada automáticamente** con pydoc-markdown.

---

## 1º PARTE
Historial de resultados en el README: en lugar de sobrescribir, añado nuevas líneas con fecha/hora.
Cuando se hago un push en main el workflow ejecuta el script en Python. El script corre los tests y modifica el README.md añadiendo una de los siguientes resultados:

✅ Tests correctos

❌ Tests fallidos

## 2º PARTE
### Descripción general
En este caso, para la generacion de la documentacion en HTML he utilizado Doxyfile, ya que es compatible con bastantes lenguajes de programacion, por lo que puede seguir utilizandose caso de que se siga expandiendo el proyecto.

Ahora, para el markdown he elegido ydoc-markdown ya que no necesitas configuraciones complicadas como en Sphinx o Doxygen. Basta con un archivo de configuración (pydoc-markdown.yml) y un simple comando.


### 1. Estilo y herramientas de documentación
- **Lenguaje:** Python  
- **Estilo de documentación:** reStructuredText  
- **Herramienta principal:** Doxygen, pydoc-markdown 
- **Formatos generados:**
  - 🌐 **HTML** → [Enlace a `docs/html/index.html`](./docs/html/index.html)
  - 📄 **Markdown** → [Enlace a `docs/markdown.md`](./docs/markdown.md)


### 2. Ejemplo de código documentado usando el estilo reStructuredText
Archivo: [`main.py`](./main.py)
```
def saludo(nombre: str) -> str:
    """
    Genera un saludo personalizado.

    :param str nombre: El nombre de la persona a saludar.
    :returns: Un saludo en forma de cadena que incluye el nombre proporcionado.
    :rtype: str
    """
    return f"Hola, {nombre}!"
```

### 3. Generación de documentación local
#### 3.1 Dependencias
Para empezar a generar la documentacion en local, tenemos que instalar todo lo necesario para no tener ningun problema de dependencias de Python, Pydoc y Doxygen.
```
pip install pytest pydoc-markdown
sudo apt install -y doxygen graphviz
```

#### 3.2 Generar configuracion
Ahora tenemos que crear los archivos de configuracion para Doxygen y Pydoc.

Para doxygen tenemos que ejecutar el siguiente comando en ./docs para generar alli el archivo Doxyfile y tener en esa carpeta toda la documentacio:
```
doxygen -g
```
Para Pydoc hay que crear un archivo llamado `pydoc-markdown.yml` en la raiz de nuestro documeto.
```
touch pydoc-markdown.yml
```

#### 3.3 Editar configuracion
Ahora el archivo `docs/Doxyfile` lo tenemos que editar para tener una comfiguracion minima y funcional que nos sirva
| Campo              | Descripción                                | Ejemplo           |
| ------------------ | ------------------------------------------ | ----------------- |
| `PROJECT_NAME`     | Nombre de tu proyecto                      | `"DAW_U1_ACTION"` |
| `OUTPUT_DIRECTORY` | Carpeta donde se guardará la documentación | `./docs`          |
| `INPUT`            | Rutas de los archivos del código fuente    | `.`               |
| `RECURSIVE`        | Indica si buscar en subcarpetas            | `YES`             |
| `GENERATE_HTML`    | Generar documentación en HTML              | `YES`             |
| `GENERATE_LATEX`   | Generar documentación en PDF (opcional)    | `NO`              |

En Pydoc hay que incluir las siguientes lineas en el archivo `pydoc-markdown.yml`:
```
loaders:
  - type: python   # Tipo de loader: carga módulos de Python
    search_path: ["."]  # Ruta donde buscar los módulos (aquí, la carpeta raíz)
    modules:
      - main          # Documenta el módulo main.py
      - update_readme # Documenta el módulo update_readme.py
      - test_main     # Documenta el módulo test_main.py

renderer:
  type: markdown        # Tipo de renderer: genera documentación en Markdown
  filename: docs/markdown.md  # Archivo de salida donde se guardará la documentación
```

#### 3.4 Generar documentacion
Para generar la documentacion de Doxygen y Pydoc a partir de los archivos de configuracion que hemos hecho, tenemos que ejecutar los siguientes comandos:
```
doxygen docs/Doxyfile
pydoc-markdown
```
Esto generará una pagina web donde podremos ver el resultado en `./docs/html/index.html` y un markdown en `docs/markdown.md`


## Estado de los tests
✅ 2025-10-12 10:25 Tests correctos

✅ 2025-10-12 01:02 Tests correctos

✅ 2025-10-12 00:46 Tests correctos

✅ 2025-10-12 00:31 Tests correctos

✅ 2025-10-12 00:29 Tests correctos

✅ 2025-10-12 00:25 Tests correctos

✅ 2025-10-12 00:20 Tests correctos

✅ 2025-10-12 00:13 Tests correctos

✅ 2025-10-11 23:49 Tests correctos

✅ 2025-10-11 23:45 Tests correctos

✅ 2025-10-11 23:30 Tests correctos

✅ 2025-10-11 23:26 Tests correctos

✅ 2025-10-11 23:17 Tests correctos

✅ 2025-10-11 21:55 Tests correctos

✅ 2025-10-11 21:45 Tests correctos

✅ 2025-10-11 19:13 Tests correctos

✅ 2025-10-11 19:06 Tests correctos

✅ 2025-10-09 22:26 Tests correctos

✅ 2025-10-09 22:07 Tests correctos

✅ 2025-10-09 22:02 Tests correctos

✅ 2025-10-09 22:00 Tests correctos

✅ 2025-10-09 21:56 Tests correctos

✅ 2025-10-09 21:54 Tests correctos

✅ 2025-10-09 21:49 Tests correctos

✅ 2025-10-09 21:47 Tests correctos

✅ 2025-10-09 21:41 Tests correctos

✅ 2025-10-09 21:19 Tests correctos

✅ 2025-10-09 20:46 Tests correctos

✅ 2025-10-09 20:37 Tests correctos

✅ 2025-10-09 20:27 Tests correctos

✅ 2025-10-09 20:23 Tests correctos

✅ 2025-10-09 20:18 Tests correctos

✅ 2025-10-09 20:17 Tests correctos

✅ 2025-10-09 20:15 Tests correctos

✅ 2025-10-09 20:10 Tests correctos

✅ 2025-10-09 20:06 Tests correctos

✅ 2025-10-09 19:24 Tests correctos

✅ 2025-10-09 19:12 Tests correctos

✅ 2025-10-09 19:07 Tests correctos

✅ 2025-10-09 19:01 Tests correctos

✅ 2025-10-09 18:58 Tests correctos

✅ 2025-10-09 18:50 Tests correctos

✅ 2025-10-09 18:13 Tests correctos

✅ 2025-10-09 18:09 Tests correctos

✅ 2025-10-09 18:05 Tests correctos

✅ 2025-10-09 17:53 Tests correctos

✅ 2025-10-09 09:42 Tests correctos

✅ 2025-10-09 09:37 Tests correctos

✅ 2025-10-09 08:51 Tests correctos

✅ 2025-10-09 08:45 Tests correctos

✅ 2025-10-09 08:30 Tests correctos

✅ 2025-09-30 22:55 Tests correctos

❌ 2025-09-30 22:54 Tests fallidos

❌ 2025-09-30 21:25 Tests fallidos

✅ 2025-09-30 21:23 Tests correctos

✅ 2025-09-30 18:38 Tests correctos
✅ Tests correctos
