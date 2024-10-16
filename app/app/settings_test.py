from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB_TEST', default=config('POSTGRES_DB')),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'db_sql',  # Nombre del servicio en Docker
        'PORT': config('POSTGRES_PORT', default='5432')
    },
    # Base de datos MongoDB para pruebas
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': config('MONGO_NAME_TEST', default=config('MONGO_NAME')),
        'HOST': 'db_nosql',  # Nombre del servicio en Docker
        'PORT': config('MONGO_PORT', default='27017'),
    }
}


MIGRATE = False
