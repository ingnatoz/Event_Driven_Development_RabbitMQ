<p align="center"><img src="./img.png" width="800"></p>

# Using DRF and Flack with RabbitMQ (EDD)

Flask, Django Rest Framework, RabbitMQ y MySql, junto con Docker para crear dos servicios web que generan contenido de forma dinámica y asíncrona.

## Project Structure

The finished project structure will be as follows:


```
Django Rest Framework:
.
├── apps
│   └── mercado_libre
│   │   ├── confing.ini
│   │   ├── meli.py
│   │   ├── services.py         (important)
│   │   └── ssl_helper.py
│   └── products
│       └── api
│       │    ├── api.py         (important)
│       │    ├── producer.py    (important)
│       │    ├── routers.py
│       │    └── serializers.py
│       ├── admin.py
│       ├── apps.py
│       └── models.py
├── nextia
│   ├── asi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── consumer.py                 (important)
├── Dockerfile
├── docker-compose.yml
├── manege.py
└── requirements.txt
```

```
Flask:
.
├── controllers
│   └── product_controller.py
├── models
│   └── Product.py
├── utils
│   └── db.py
├── app.py
├── config.py
├── consumer.py                 (important)   
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Using Docker to package our application



We pull all of this together with a Docker compose file, `docker-compose.yml`. While early versions of compose needed to expose ports for each service, we can link the services together using the `links` keyword. The `depends` keyword ensures that all of our services start in the correct order.

To create and run the container in case of Django, use:

    docker-compose build
    docker-compose up -d back-django

To create and run the container in case of Flask, use:

    docker-compose build
    docker-compose up -d back-flask

