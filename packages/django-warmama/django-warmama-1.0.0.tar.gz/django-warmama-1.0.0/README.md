# django-warmama

[![build-status-image]][travis]
[![pypi-version]][pypi]

## Overview

Django app for qfusion authentication server

## Installation

Install using `pip`, please use a virtualenv...

```bash
$ pip install django-warmama
```

## Basic Usage

An example project is provided and is sufficient for testing with QFusion.
Just get the server started.

```bash
cd example-project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

To use it with QFusion, you need to add some User, Server and Player models; so
navigate over to the admin page at
[http://localhost:8000/admin/](http://localhost:8000/admin/) and create some.

1. Create some normal django users first, qf clients will use these username
   password combinations to connect.
2. Create warmama Player models. The `login` field must be the username of a
   previously created User.
3. Create warmama Server models. The `login` field here will be the server's
   authtoken. Either `regip` or `regipv6` must be set to the server's ipaddress,
   for local testing `127.0.0.1` is allowed.

Finally configure the QFusion server and clients to use warmama for matchmaking.
For the server, set `sv_mm_enable` to `1` and `sv_mm_authtoken` to the `login`
value of the Server created above. For both the server and client set `mm_url`
to `http://127.0.0.1:8000` (without a trailing slash).

## Advanced Usage

Then configure your django project to use the app, you can override any of the
warmama settings (found in warmama/settings.py) in your project's settings.py
file.

```python
# project/settings.py

INSTALLED_APPS = (
    ...
    'warmama',
)

# project/urls.py
urlpatterns = [
    ...
    url(r'^warmama/', include('warmama.urls', namespace='warmama', app_name='warmama')),
]
```

Finally, run the migrations and (optionally) load the fixtures

```bash
python manage.py migrate
python manage.py loaddata --app warmama gametypes
python manage.py loaddata --app warmama weapons
```

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
$ ./runtests.py
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/)
testing tool to run the tests against all supported versions of Python and
Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```


[build-status-image]: https://secure.travis-ci.org/kalhartt/django-warmama.png?branch=master
[travis]: http://travis-ci.org/kalhartt/django-warmama?branch=master
[pypi-version]: https://pypip.in/version/django-warmama/badge.svg
[pypi]: https://pypi.python.org/pypi/django-warmama
