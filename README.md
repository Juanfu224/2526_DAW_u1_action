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
Sphinx es un framework que nos ayudará a construir la documentación de nuestros proyectos de Python. Este programa lo que hace es transformar archivos reST en archivos HTML o pdf, dándoles un formato más amigable gracias al uso intero de templates.

Lo que queremos con los docstrings que escribimos es que Sphinx los entienda y logre renderizar apropiadamente un archivo en formato HTML o PDF que sea agradable de leer. Para que esto suceda debemos escribir nuestros docstrings en uno de los formatos que Sphinx entiende. En este caso he utilizado reStructuredText (reST)

Para instalar Sphinx en Linux y poderlo utilizar en el proyecto de Python, he ejecutado el siguiente comando:
```
sudo apt install python3 python3-pip python3-sphinx
```

Al comenzar, suponiendo que estamos en el directorio root de nuestro proyecto, nos cambiamos al directorio docs y ejecutamos el siguiente comando
```
sphinx-quickstart
```
![sphinx-quickstart](https://github.com/Juanfu224/2526_DAW_u1_action/blob/ee62e4b93cfc37f115eff96e518018f0d1dc9dce/images/sphinx-quickstart.png)

Dentro de docs tiene que haber la siguente estructura:
![estructura_docs](https://github.com/Juanfu224/2526_DAW_u1_action/blob/f617396b1ff56e66878aa3d1207de91c499f318a/images/estructura_docs.png)



## Estado de los tests
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
