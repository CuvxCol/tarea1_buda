# Postulación a desarrollador de Buda.com
## [Tarea 1](https://budapuntocom.notion.site/Spread-API-2fb7f25ef5344d3081c48259da05ae94)

## Features

- Calcular el spread de cualquiera de los mercados de Buda.com
- Necesitamos obtener el spread de todos los mercados en una sola llamada.
- Necesitamos guardar un spread de “alerta” el cual en el futuro consultaremos por medio de polling si el spread es mayor o menor de ese spread.

## Documentación del API

Para esto se realizó a través de la herramienta Postman

- [Doccumentación](https://documenter.getpostman.com/view/7096348/VV4uwwzY)

## Ejecución

Para ello, se puede realizar a travez de dos opciones:

### Dockerfile

Dentro del repositorio junto al Dockerfile realizar:
```sh
docker build  -t tarea1_buda:0.0.1 .
docker run -dti --name tarea1_buda_v0.0.1 -p 8000:8000 tarea1_buda:0.0.1
```

### Imagen Docker

```sh
docker pull ghcr.io/cuvxcol/tarea1_buda/buda_tarea1:0.0.1
docker run -dti --name tarea1_buda_v0.0.1 -p 8000:8000 ghcr.io/cuvxcol/tarea1_buda/buda_tarea1:0.0.1
```

### Desde el repositorio (Sin docker)
Para este procedimiento, debe tener instalado python:3.8.10 y pip actualizado y preferiblemente en un entorno virtual: Realizá la instalación de los paquetes en el archivo requerements.txt con el comando:
```sh
pip install -r requirements.txt
```

y ejecuta con 
```sh
python manage.py runserver 0.0.0.0:8000
```

## Desarrollador:
Henry David Diaz Velandia
[GitHub](https://github.com/CuvxCol)
[Linkedin](https://www.linkedin.com/in/hddiazv/)
