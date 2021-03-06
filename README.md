# ml-pipeline

## Architecture

<img src="docs/architecture.png">

## Directory tree

```
.
├── consumer                             # Faust Consumer
│   ├── Dockerfile
│   ├── main.py                          
│   └── requirements.txt
├── docker-compose.yml
├── frontend                             # ReactJS Frontend
│   ├── Dockerfile
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   ├── favicon.ico
│   │   ├── index.html
│   │   ├── manifest.json
│   │   └── robots.txt
│   └── src
│       ├── App.css
│       ├── App.js
│       └── index.js                     # Simple form
├── nginx_config.conf                    # Nginx server configurations
├── service_1
│   ├── app
│   │   ├── alembic/                     # Database migrations
│   │   ├── alembic.ini
│   │   ├── app
│   │   │   ├── api
│   │   │   │   ├── deps.py              # Data
│   │   │   │   ├── __init__.py
│   │   │   │   └── scores.py            # Routes for api
│   │   │   ├── crud.py                  
│   │   │   ├── database.py              # Database configuration
│   │   │   ├── __init__.py
│   │   │   ├── models.py                
│   │   │   └── schemas.py
│   │   ├── __init__.py
│   │   ├── main.py                      # API main
│   │   └── pipeline.joblib              # Sklearn prediction pipeline
│   ├── Dockerfile
└── └── requirements.txt
```

## Execution

```
docker-compose build
docker-compose up
```