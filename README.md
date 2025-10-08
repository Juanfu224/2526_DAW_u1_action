# Mi Proyecto con GitHub Actions
Mi proyecto contiene varios archivos:
- Un programa principal (main.py).
- Un test unitario (test_main.py).
- Un script (update_readme.py) que ejecuta los tests y modifica el README.md, con el resultado de ejecutar los test.
- Un script básico (ci.yml) que ejecuta y hace commit automático con git-auto-commit-action.

Cuando se hago un push en main el workflow ejecuta el script en Python. El script corre los tests y modifica el README.md añadiendo una de los siguientes resultados:

✅ Tests correctos

❌ Tests fallidos

## 1º PARTE
En este caso he implementado las siguientes mejoras:
- Historial de resultados en el README: en lugar de sobrescribir, añado nuevas líneas con fecha/hora.

## 2º PARTE
Para instalar Sphinx en Linux y poderlo utilizar en el proyecto de Python, he ejecutado el siguiente comando:
```
sudo apt install python3 python3-pip python3-sphinx
```

## Estado de los tests
✅ 2025-09-30 22:55 Tests correctos

❌ 2025-09-30 22:54 Tests fallidos

❌ 2025-09-30 21:25 Tests fallidos

✅ 2025-09-30 21:23 Tests correctos

✅ 2025-09-30 18:38 Tests correctos
✅ Tests correctos
