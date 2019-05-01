Este es un test para la empresa destacame como backend developer en python usando Django

###################################################################################

# Instrucciones de instalación 

Para la correcta instalación de el test primero hay que instalar Python3 en el sistema opertivo de la maquina
Luego descargar el repositorio de Git-Hub y almacenar todo el repositorio en una carpeta ejemplo "C:\develop\python\destacame"
Una vez ya el repositorio en una carpeta se debera crear un entorno virtual, recomiendo usar virtualenv
luego con el terminal de comandos nos movemos a la carpeta destacame (donde se encuenta el proyeto) y ejecutamos el comando:

       >pip virtualenv venv

Ese comando creara una entorno virtual para el proyecto, ahora ejecutamos activamos este repositorio usando el comando:

        >venv/Scripts/activate    

## Nota
la ubicacion del archivo activate varia dependiendo del OS de la maquina, en este ejemplo es para windows
######
Con el entorno virtual activado ahora instalamos las librerias y frameworks que usaremos para el proyecto usando el comando

    (venv)>pip install -r requirements.txt

para instalar todo lo que se encuentra listado en requirements.txt

una vez instalado todo lo que hacemos es ejecutar el comando:

    >python manage.py runserver

para activar el servidor y probar el test

###################################################################################

## Observaciones
Analizando el enunciado, segun mi logica el cliente deberia tener relacion con el trayecto y no con el bus, asi que considerando eso diseñe asi la base de datos.

Logre mostrar de manera individual el promedio total de cada trayecto, aunque mi idea original era mostrar un resultado como la siguiente tabala:

              |  Trayecto | 2019-04-28 | 2019-04-29 | 2019-04-30 |
              | Las Condes|    7.5     |      4     |     3.8    |
              |Providencia|     8      |      1     |      4     |

##############################

Saludos y espero sus respuestas