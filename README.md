# Mi Proyecto con GitHub Actions
## 📁 Estructura del proyecto
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
