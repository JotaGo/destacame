Este es un test para la empresa destacame como backend developer en python usando Django

##################################################################################################################

## Instrucciones de instalación #

Para la correcta instalación de el test primero hay que instalar Python3 en el sistema opertivo de la maquina
Luego descargar el repositorio de Git-Hub y almacenar todo el repositorio en una carpeta ejemplo "C:\develop\python\destacame"
Una vez ya el repositorio en una carpeta se debera crear un entorno virtual, recomiendo usar virtualenv
luego con el terminal de comandos nos movemos a la carpeta destacame (donde se encuenta el proyeto) y ejecutamos el comando:

       >pip virtualenv venv

Ese comando creara una entorno virtual para el proyecto, ahora ejecutamos activamos este repositorio usando el comando:

        >venv/Scripts/activate    

# Nota
la ubicacion del archivo activate varia dependiendo del OS de la maquina, en este ejemplo es para windows
######
Con el entorno virtual activado ahora instalamos las librerias y frameworks que usaremos para el proyecto usando el comando

    (venv)>pip install -r requirements.txt

para instalar todo lo que se encuentra listado en requirements.txt

una vez instalado todo lo que hacemos es ejecutar el comando:

    >python manage.py runserver

para activar el servidor y probar el test

##########################################################################################################################

# Observaciones
Cambie un poco la base de datos con respecto al enunciado ya que me parece que el pasajero realmente no le importa el bus que tome
lo que le importa es llegar a su destino.

Tambien no pude mostrar una lista con los promedios de cada trayecto, solo logre mostrarlos de manera individual el promedio total
de cada trayecto, pero originalmente queria mostrar una tabla como la siguiente:

               | Trayecto | 2019-04-28 | 2019-04-29 | 2019-04-30 |
               |Las Condes|    7.5     |      4     |     3.8    |
              |Providencia|     8      |      1     |      4     |

Tampoco logre armar un Query para filtrar el % de los pasajeros en los buses de tal manera que ese objetivo del proyecto no lo logre
tenia una idea pero ando corto de tiempo para aplicarla.

Por ultimo no trabaje con el fronted Vue.js, solo trabaje con los templates basicos que fui construyendo.

##############################

Saludos y espero sus respuestas