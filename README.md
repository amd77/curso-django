# Curso Django

## Pasos previos

### Descargas

Git: [Descargar](https://git-scm.com/download/)

Python: [Descargar](https://www.python.org/downloads/) | 
[Tutorial castellano](https://docs.python.org/es/3/tutorial/index.html)

Django: [Descargar](https://www.djangoproject.com/download/) |
[Tutorial castellano](https://docs.djangoproject.com/es/4.0/intro/) |
[Documentación](https://docs.djangoproject.com/es/4.0/)

Editores código: [Atom](https://atom.io/) |
[VSCodium](https://vscodium.com/) |
[Pyzo](https://pyzo.org/)

Otros editores código: [VSCode](https://code.visualstudio.com/) | 
[Pycharm](https://www.jetbrains.com/pycharm/) |
[Sublime](https://www.sublimetext.com/)

Editores Markdown: [GhostWriter](https://wereturtle.github.io/ghostwriter/) |
[Remarkable](https://remarkableapp.github.io/)

Instaladores para Windows: [Winget](https://github.com/microsoft/winget-cli) |
[Chocolatey](https://community.chocolatey.org/packages) 


### GIT

La primera vez:

* Descargar repositorio: `git clone [repo]`

El día a dia:

* Descargar actualizaciones (al empezar): `git pull` (opción `--rebase`)
* Ver lo que hemos editado: `git status`
* Agregar al repositorio ficheros si son nuevos: `git add fichero1 ficheroN`
* Ver diferencias: `git diff`
* Generar un cambio con ficheros sueltos: `git commit -m 'Mensaje' fichero1 ficheroN`
* Generar un cambio con todo: `git commit -a -m 'Mensaje'`
* Subir cambios: `git push`

Otros comandos:

* Ver histórico de cambios: `git log`
* Deshacer cambios: `git reset HEAD --hard`

![](https://miro.medium.com/max/5416/1*cnADY2zzrb0gEZqUkV6gxQ.png)

[Branching models](https://duckduckgo.com/?q=branching+models+git&iar=images) y [git flow](https://duckduckgo.com/?q=git+flow&iar=images) lo obviamos de momento. Usaremos [linear history](https://duckduckgo.com/?q=git+linear+history&iar=images) Todo será master (main).

* Listar ramas: `git branch -l`
* Cambiar de rama:  `git checkout [rama]`


### Mensajes de commit

[Descripción filosofía y discusión](https://salferrarello.com/rules-for-writing-git-commit-messages/)

Preferimos cambios pequeños y líneas sencillas, [prefijos estándares](https://www.conventionalcommits.org/en/v1.0.0/#summary), y versionado semántico MAJOR.MINOR.PATCH:

* `xxx!:` breaking change (cambiaria MAJOR.y.z)
* `feat:` agrega una caracteristica (cambiaria x.MINOR.z)
* `fix:` arregla un fallo (cambiaria x.y.PATCH)
* `refactor:` ni arregla ni agrega caracteristicas
* `revert:` revierte el commit #xxxxxx
* `build:` cambio en compilacion o dependencias
* `ci:` cambio en los ficheros/scripts de ci
* `docs:` cambios de documentacion solamente
* `test:` agregar o corregir tests
* `style:` espaciado, formateado, sintaxis
* `perf:` aumenta performance
* `chore:` limpieza de funciones no usadas


### Visual Studio Code

* [Tutorial oficial Microsoft](https://code.visualstudio.com/docs/python/tutorial-django)
* Con putty generar claves y registrar la clave publica en [github](https://github.com/settings/ssh/new)


### Creacion de entorno virtual

```
python -m venv .venv  # Crear en una carpeta "aislado"
python -m venv .venv --system-site-packages  # o usando lo que hay en el sistema
source .venv/bin/activate  # Esto lo activa
. .venv/bin/activate  # Esto tambien (en linux se puede poner .)
deactivate  # Esto lo desactiva
```

### Instalación de librerias y paquetes

```
pip freeze  # ver paquetes instalados
pip install django  # instalar ultima version
pip install 'django < 4'  # instalar ultima con limite
pip install 'django == 3.2.11'  # instalar version concreta
pip install -r requirements.txt  # instalar versiones desde un fichero
```

### Primeros pasos en django

```
django-admin startproject nombre_del_proyecto
mv nombre_del_proyecto src
cd src
python manage.py
python manage.py migrate  # Crea la base de datos
python ./manage.py createsuperuser  # Crea usuario admin
python ./manage.py runserver  # ver con http://localhost:8000/
python ./manage.py runserver 0.0.0.0:8000   # ver desde toda la LAN
```

### Management commands

Para trabajar con bases de datos o cambios en los modelos:

* `./manage.py showmigrations`: muestra migraciones y si estan aplicadas o no
* `./manage.py makemigrations [app]`: crea migraciones de cambios en models.py
* `./manage.py migrate`: crea base de datos y aplica las migraciones sin aplicar

* `./manage.py createsuperuser`: crear usuario administrativo
* `./manage.py changepassword [usuario]`: cambiar contraseña usuario
* `./manage.py dbshell`: habre conexion SQL a la base de datos

Para crear o cargar fixtures:

* `./manage.py dumpdata [app1] [app2.modelo] --indent 1 -o fixture.json`: guarda bd en json
* `./manage.py loaddata fixture.json`: carga json en bd

Para el dia a dia:

* `./manage.py runserver`: genera un servidor en http://localhost:8000/
* `./manage.py check`: hace comprobaciones basicas
* `./manage.py startapp [nombre]`: crea una app vacia en el proyecto actual
* `./manage.py shell`: abre un shell de python con django cargado
* `./manage.py diffsettings`: muestra las settings.py que se han cambiado (o extra)
* (`./manage.py collectstatic`: copia estaticos a `STATIC_URL`)

Las de `django_extensions`:

* `./manage.py graph_models [app] -o app.png`: genera grafico modelos (instalar pydotplus)
* `./manage.py dumpscript`: vuelca la base de datos en codigo python
* `./manage.py generate_secret_key`: genera una `SECRET_KEY` aleatoria
* `./manage.py print_settings`: muestra todos los settings (los default y los del settings.py)
* `./manage.py shell_plus`: muestra un shell con todos los modelos cargados
* `./manage.py sqldiff`: muestra discrepancias entre bd y models

### Meta de los modelos:

* `verbose_name`: cambiar el nombre en singular del modelo, p.ej si tiene tildes o simbolos
* `verbose_name_plural`: cambiar el nombre plural del modelo, que por defecto solo le agrega una s
* `ordering`: lista de campos para hacer ordenacion, por ejemplo, `['apell1', 'apell2', 'nombre']`
* `unique_together`: evita filas duplicadas atendiendo a estos criterios multiples (para sencillos, `unique=True` en campo)
* `db_table`: cambiar el nombre de la tabla, que por defecto es `aplicacion_modelo`
* `managed`: se pone a False para decirle que no cree tablas/migraciones para este modelo
* `abstract`: este modelo no genera tabla, es solo para ser el base de una herencia
* `indexes`/`index_together`: crea indices para estos campos para acelerar consultas base de datos
