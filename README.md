# DAS_Project
Proyecto final para la materia de Diseño y Arquitectura de Software.

## Como contribuir:
- Hacer un fork al proyecto.
- Todos los Pull Request deben ir a la rama de desarrollo, la cual se llama **development**.
- Todas las subramas deben ser creadas en base a la rama **development**.

## Diagramas
- Este proyecto utiliza una arquitectura hexagonal mostrada en la siguiente image:
![DiagramaHex](DiagramaHex_v2.png)

- El diagrama UML del proyecto es el siguiente:
![DiagramaUML](DiagramaUML_V4.png)

## Tecnologias utilizadas
Para este proyecto se utilizaron distintas tecnologias para poderlo llevar a cabo. A continuacion esta un listado de estas:

### Lenguajes
- python.
- shell.

### Framework
- flask.

### Base de datos
- Mongo DB.

### DBMS
- Mongo-express.

### Otras tecnologias
- docker.
- docker compose.

## Como ejecutar:
### A tomar en consideracion
Para poder ejecutar este proyecto se requiere de tener instalado `docker` y `docker compose`.

### Pasos a seguir
1. Como primer paso a realizar se debe de copiar el repositorio con el siguiente comando: <pre><code>git clone https://github.com/Hanhoeng/DAS_Project.git
</code></pre>

2. Se debe de ubicar en la carpeta base del repositorio y ejecutar el siguiente comando de docker compose:<pre><code>docker-compose up
</code></pre>
Nota: si se revisan los contenedores con <pre><code>docker ps
</code></pre> se podra notar que solo estan los contenedores correspondientes a la base de datos, dbms y API ya que el contenedor con el generador se detiene una vez termine de guardar los libros falsos generados.

Contibuyentes:
* [David Hiroshi Gloria Kawasaki](https://github.com/Hanhoeng)
* [Jose Fernando Perez Arroyo](https://github.com/FernandoPerez-ops)
* [Lucely Liliana Flores Escalante](https://github.com/LucelyFlores)
* [Brandon Emmanuel Delabra Salinas](https://github.com/Andremm303)
* [Cristian edgardo guerrero lopez](https://github.com/KryzHD)