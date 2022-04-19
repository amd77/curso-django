# Curso Django

## Descargas

Python: https://www.python.org/downloads/

Git: https://git-scm.com/download/

Editores: [Atom](https://atom.io/) [VSCodium](https://vscodium.com/) [Pyzo](https://pyzo.org/)

Otros editores: [VSCode](https://code.visualstudio.com/) | 
[Pycharm](https://www.jetbrains.com/pycharm/) |
[Sublime](https://www.sublimetext.com/)

Instaladores: [Winget](https://github.com/microsoft/winget-cli) |
[Chocolatey](https://community.chocolatey.org/packages) 


## GIT

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

[Branching models](https://duckduckgo.com/?q=branching+models+git&iar=images): lo obviamos de momento. Todo será master (main).

* Listar ramas: `git branch -l`
* Cambiar de rama:  `git checkout [rama]`

