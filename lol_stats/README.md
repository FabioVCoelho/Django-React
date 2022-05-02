### Following the how-to from [graphql](https://www.howtographql.com/graphql-python/1-getting-started/)

### Installing django

python -m pip install Django

### Starting project

django-admin startproject lol_stats

### Installing graphql dependencies

pip install graphene-django django-filter django-graphql-jwt

```Successfully installed PyJWT-2.3.0 aniso8601-7.0.0 django-filter-21.1 django-graphql-jwt-0.3.4 graphene-2.1.9 graphene-django-2.15.0 graphql-core-2.3.2 graphql-relay-2.0.1 promise-2.3 rx-1.6.1 singledispatch-3.7.0 six-1.16.0 text-unidecode-1.3```

### Initializing django

```shell
cd lol_stats
python manage.py migrate
python manage.py runserver
```

### Inserting graphql as an app from django

on settings.py

```shell
INSTALLED_APPS = (
    # After the default packages
    'graphene_django',
)
```

to resolve the error just change the import in YOUR_VENV/lib/site-packages/graphene_django/utils/utils.py

```shell
from django.utils.encoding import force_text
to
from django.utils.encoding import force_str
```

### Graphene

TODO

### MongoDb with Django

Following the how-to from [mongodb](https://www.mongodb.com/compatibility/mongodb-and-django)

Before installing the python libraries, is needed to install the following package.

```shell
apt-get install libkrb5-dev
```

Install libraries needed for python connection with mongodb and graphene

```shell
pip install -r requirements.txt
```

### Django Rest

```shell
pip install django-cors-headers
```