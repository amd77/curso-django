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