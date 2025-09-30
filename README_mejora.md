Mi proyecto contiene varios archivos:
- Un programa principal (main.py).
- Un test unitario (test_main.py).
- Un script (update_readme.py) que ejecuta los tests y modifica el README.md, con el resultado de ejecutar los test.
- Un script básico (ci.yml) que ejecuta y hace commit automático con git-auto-commit-action.

Cuando se hago un push en main el workflow ejecuta el script en Python. El script corre los tests y modifica el README.md añadiendo una de los siguientes resultados:

✅ Tests correctos

❌ Tests fallidos

En este caso he implementado las siguientes mejoras:
- Historial de resultados en el README: en lugar de sobrescribir, añado nuevas líneas con fecha/hora.
